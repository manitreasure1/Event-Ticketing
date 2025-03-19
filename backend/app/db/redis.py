import aioredis


jwt_redis_block_list = aioredis.StrictRedis(
    host='localhost', port=6379, db=0, decode_responses=True
)