from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

class User:
    def __init__(self, username: str, password: str, level: int):
        self.Username = username
        self.Password = password
        self.Level = level

    def get_dict(self):
        data = {
            'Username': self.Username,
            'Password': self.Password,
            'Level': self.Level
        }
        return data

    def create(self, connection: MySQLConnectionAbstract):
        cursor = connection.cursor()
        sql = "INSERT INTO users (Username, Password, Level) VALUES (%s, %s, %s)"
        val = (self.Username, self.Password, self.Level)
        cursor.execute(sql, val)
        connection.commit()

    def delete(self, connection: MySQLConnectionAbstract):
        cursor = connection.cursor()
        sql = "DELETE FROM users WHERE Username = %s"
        val = tuple([self.Username])
        cursor.execute(sql, val)
        connection.commit()

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
