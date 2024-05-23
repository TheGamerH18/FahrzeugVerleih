from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

class User:
    def __init__(self, userId: int, username: str, password: str, level: int):
        self.UserId = userId
        self.Username = username
        self.Password = password
        self.Level = level

    def get_dict(self):
        data = {
            'UserId': self.UserId,
            'Username': self.Username,
            'Password': self.Password,
            'Level': self.Level
        }
        return data

    @staticmethod
    def get(connection: PooledMySQLConnection | MySQLConnectionAbstract, username: str):
        cursor = connection.cursor()
        sql = 'SELECT * FROM users WHERE UserName = %s'
        val = tuple([username])
        cursor.execute(sql, val)
        row = cursor.fetchone()
        return User(*row)

    @staticmethod
    def get_all(connection: PooledMySQLConnection | MySQLConnectionAbstract):
        cursor = connection.cursor()
        sql = 'SELECT * FROM users'
        cursor.execute(sql)
        row = cursor.fetchall()
        return [User(*row) for row in row]