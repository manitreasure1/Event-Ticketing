from unittest.mock import patch


def test_jwt_redis_block_list_connection():
    with patch("redis.asyncio.StrictRedis") as mock_redis:
        from app.db import redis as redis_module
        redis_instance = redis_module.jwt_redis_block_list
        mock_redis.assert_called_with(host='localhost', port=6379, db=0, decode_responses=True)
        assert redis_instance is mock_redis.return_value
