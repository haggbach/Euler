# Project Euler

https://projecteuler.net/

For the most part, I'm going to attempt a naive solution (not looking for a mathematical theorem to short-cut) and then move on to googling for shortcuts when I'm not happy with the timing. I want to showcase my thought process as well as my googling skills ;p

I am also using this as an exercise in directing Claude Code efficiently and effectively.

I will be attempting to modularize functions and add testing where possible, and I will most likely eventually introduce some kind of caching for certain problems (redis or memcached)

Python 3.12
redis (optional)

## Running Redis with Docker Compose

A docker-compose file is provided in the `external/` directory to run Redis for caching.

To start Redis as a daemon (background process):
```bash
docker-compose -f external/docker-compose.yml up -d
```

To stop the Redis service:
```bash
docker-compose -f external/docker-compose.yml down
```

To view logs:
```bash
docker-compose -f external/docker-compose.yml logs -f redis
```
