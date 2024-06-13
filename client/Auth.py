import base64


class Auth:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getAuth(self):
        return "Basic " + str(base64.b64encode(str(self.username + ':' + self.password).encode("UTF-8")))
