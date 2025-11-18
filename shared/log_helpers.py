import logging
from datetime import datetime

import simplejson as json
import os
ENV = os.getenv('EULER_ENV', 'local')

class JsonFormatter(logging.Formatter):
    """Custom formatter to output logs in JSON format"""
    
    def format(self, record):
        log_entry = {
            # TODO: this assumes local TZ is UTC (please?)
            'timestamp': datetime.now().isoformat() + 'Z',  
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
            
        # Add any extra fields from the log record
        for key, value in record.__dict__.items():
            if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 
                          'filename', 'module', 'lineno', 'funcName', 'created', 
                          'msecs', 'relativeCreated', 'thread', 'threadName', 
                          'processName', 'process', 'message', 'exc_info', 'exc_text', 
                          'stack_info', 'getMessage']:
                log_entry[key] = value
        
        return json.dumps(log_entry)


class LogHelper:
    """
    Returns a formatted logger
    """
    @staticmethod
    def get_logger(caller_name: str, log_level=None, force_json=False):
        """
        Get a configured logger instance
        Will return a logger configured for JSON formatting if the EULER_ENV environment variable
            is set to non-local (or is not set) OR if the force_json parameter is set to true
            This is for easier local debugging - I find it VERY DIFFICULT to read JSON-formatted logs,
            in my terminal window, while cloud logging systems and other production infrastructure find
            it VERY EASY to read JSON-formatted logs. This way, we're both happy (ish)
        
        Args:
            caller_name (str): Name for the logger (typically __name__)
            log_level: Logging level (default: logging.INFO for non-local, logging.DEBUG for local)
            json_format (bool): Whether to use JSON formatting (default: True)
            
        Returns:
            logging.Logger: Configured logger instance
        """
        if log_level is None:
            log_level = logging.DEBUG if ENV == 'local' else logging.INFO

        json_format = False if ENV == 'local' else True
        logger = logging.getLogger(caller_name)
        
        # Avoid adding multiple handlers if logger already configured
        if logger.handlers:
            return logger
            
        # Set the logger level
        logger.setLevel(log_level)
        
        # Create console handler
        handler = logging.StreamHandler()
        handler.setLevel(log_level)
        
        # Set formatter based on json_format parameter
        if json_format or force_json:
            formatter = JsonFormatter()
        else:
            formatter = logging.Formatter(
                '%(asctime)s [%(levelname)s]: %(name)s.%(lineno)s: %(message)s'
            )
        
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Prevent logs from being handled by the root logger
        logger.propagate = False
        
        return logger
