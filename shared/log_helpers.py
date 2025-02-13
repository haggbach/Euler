import logging


class LogHelper:
    @staticmethod
    def get_logger(caller_name, log_level=logging.INFO):
        logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s')

        logging.root.setLevel(log_level)
        logger = logging.getLogger(caller_name)

        return logger
