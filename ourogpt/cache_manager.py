import redis
from .config import Config

class CacheManager:
    def __init__(self):
        try:
            self.client = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)
            self.client.ping()
        except Exception:
            self.client = None

    def get(self, key):
        if self.client:
            return self.client.get(key)
        return None

    def set(self, key, value):
        if self.client:
            self.client.set(key, value)
