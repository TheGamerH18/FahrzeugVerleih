from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


class User:
    def __init__(self, userId: str, username: str, password: str, canWrite: bool, isAdmin: bool):
        self.UserId = userId
        self.Username = username
        self.Password = password
        self.CanWrite = canWrite
        self.IsAdmin = isAdmin

    @staticmethod
    def get(connection: PooledMySQLConnection | MySQLConnectionAbstract, username: str, password: str):
        cursor = connection.cursor()
        sql = 'SELECT * FROM users WHERE UserName = %s AND Password = %s'
        val = (username, password)
        cursor.execute(sql, val)
        row = cursor.fetchone()
        return User(*row)


