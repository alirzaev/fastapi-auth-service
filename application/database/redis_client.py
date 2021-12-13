from redis import Redis

from application.core.config import config

redis_client = Redis.from_url(config.REDIS_URL)
