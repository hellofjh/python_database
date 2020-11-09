import redis

pool = redis.ConnectionPool(host = "localhost", port = 6379, password = '', db = 0, max_connections = 20)

_redis = redis.Redis(
    connection_pool=pool
)