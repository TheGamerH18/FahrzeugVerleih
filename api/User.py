class User:
    def __init__(self, username: str, password: str, canWrite: bool, isAdmin: bool):
        self.Username = username
        self.Password = password
        self.CanWrite = canWrite
        self.IsAdmin = isAdmin

    @staticmethod
    def load(userId: int, username: str, password: str, canWrite: bool, isAdmin: bool):
        return User(username, password, canWrite, isAdmin)