import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379

redis_client = redis.StrictRedis(host=REDIS_HOST, port = REDIS_PORT, decode_responses=True)