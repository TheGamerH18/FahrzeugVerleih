from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


class User:
    def __init__(self, userId: int, username: str, password: str, role: Role):
        self.UserId = userId
        self.Username = username
        self.Password = password
        self.Role = role

    @staticmethod
    def get(connection: PooledMySQLConnection | MySQLConnectionAbstract, username: str, password: str):
        cursor = connection.cursor()
        sql = 'SELECT * FROM users WHERE UserName = %s AND Password = %s'
        val = (username, password)
        cursor.execute(sql, val)
        row = cursor.fetchone()
        return User(*row)


class Role:
    def __init__(self, roleId: int, roleName: str, permissionLevel: int):
        self.RoleId = roleId
        self.RoleName = roleName
        self.PermissionLevel = permissionLevel

    def get(self, connection, roleId):
        cursor = connection.cursor()
        sql = 'SELECT * FROM roles WHERE RoleId = %s'
        val = [roleId]
        cursor.execute(sql, val)
        row = cursor.fetchone()
        return Role(*row)

