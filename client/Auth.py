import base64

class Auth:
    __username = ""
    __password = ""
    def __init__(self, username, password):
        Auth.__username = username
        Auth.__password = password

    @staticmethod
    def getAuth():
        return (Auth.__username, Auth.__password)
        #return "Basic " + str(base64.b64encode(str(self.username + ':' + self.password).encode("UTF-8")))
