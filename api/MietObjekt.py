from datetime import datetime

from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

import mysql.connector
from Bauart import Bauart

class MietObjekt:
    def __init__(self, ObjektId: int, bauart, Kennzeichen: str, Baujahr: str, Kraftstoff: str, LetzteInspektion: datetime):
        self.LetzteInspektion = LetzteInspektion
        self.ObjektId = ObjektId
        self.Bauart = bauart
        self.Kennzeichen = Kennzeichen
        self.Baujahr = Baujahr
        self.Kraftstoff = Kraftstoff

    def get_dict(self):
        dicts = {
            'ObjektId': self.ObjektId,
            'Bauart': self.Bauart.get_dict(),
            'Kennzeichen': self.Kennzeichen,
            'LetzteInspektion': str(self.LetzteInspektion),
            'Kraftstoff': self.Kraftstoff,
            'Baujahr': self.Baujahr
        }
        return dicts

    @staticmethod
    def create(connection, bauart, Kennzeichen: str, Baujahr: str, Kraftstoff: str, LetzteInspektion):
        cursor = connection.cursor()
        sql = "INSERT INTO Mietobjekt (BauartID, Kennzeichen, Baujahr, Kraftstoff, LetzteInspektion) VALUES (%s, %s, %s, %s, %s)"
        val = (bauart.BauartId, Kennzeichen, Baujahr, Kraftstoff, LetzteInspektion)
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def get_all(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Mietobjekt")
        results = cursor.fetchall()
        mietobjekte = []
        for row in results:
            bauart = Bauart.get(connection, row[1])
            li = list(row)
            li[1] = bauart
            fahrzeug = MietObjekt(*li)
            mietobjekte.append(fahrzeug)
        return mietobjekte

    @staticmethod
    def get(connection: PooledMySQLConnection | MySQLConnectionAbstract, objekt_id: int):
        cursor = connection.cursor()
        sql = "SELECT * FROM Mietobjekt WHERE ObjektID = %s"
        val = tuple([objekt_id])
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            bauart = Bauart.get(connection, row[1])
            row[1] = bauart
            return MietObjekt(*result)
        else:
            return None

    def update(self, connection: mysql.connector.MySQLConnection):
        cursor = connection.cursor()
        sql = "UPDATE Mietobjekt SET BauartID = %s, Kennzeichen = %s, Baujahr = %s, Kraftstoff = %s, LetzteInspektion = %s WHERE ObjektID = %s"
        val = (self.BauartId, self.Kennzeichen, self.Baujahr, self.Kraftstoff, self.LetzteInspektion, self.ObjektId)
        cursor.execute(sql, val)
        connection.commit()

    def delete(self, connection):
        cursor = connection.cursor()
        sql = "DELETE FROM Mietobjekt WHERE ObjektID = %s"
        val = self.ObjektId
        cursor.execute(sql, val)
        connection.commit()
