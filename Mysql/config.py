import mysql.connector.pooling
config = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'python'
}
pool = mysql.connector.pooling.MySQLConnectionPool(
    **config,
    pool_size=10
)
con_pool = pool.get_connection()

con = mysql.connector.connect(**config)