import requests
from client import Auth
class Bauart:
    def __init__(self, BauartId: int, Marke: str, Modell: str, Bauform: str):
        self.BauartId = BauartId
        self.Marke = Marke
        self.Modell = Modell
        self.Bauform = Bauform




    def delete(self, connection):
        pass


    @staticmethod
    def create(connection, Marke, Modell, Bauform):
        pass


    @staticmethod
    def get_all(connection):
        pass


    @staticmethod
    def read(connection, bauart_id):
        pass
