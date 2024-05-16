import mysql.connector
from datetime import datetime

from MietObjekt import MietObjekt
from Mitarbeiter import Mitarbeiter

class MietVorgang:
    def __init__(self, VorgangId: int,
                 KilometerstandVorher: int,
                 KilometerstandNacher: int,
                 GefahreneKilometer: int,
                 MieteStart: datetime,
                 MieteEnde: datetime,
                 arbeiter: Mitarbeiter,
                 objekt: MietObjekt):
        self.VorgangId = VorgangId
        self.Objekt = objekt
        self.Mitarbeiter = arbeiter
        self.KmStandVorher = KilometerstandVorher
        self.KmStandNachher = KilometerstandNacher
        self.Gefahrene_Kilometer = GefahreneKilometer
        self.MieteStart = MieteStart
        self.MieteEnde = MieteEnde

    def get_dict(self):
        dicts = {
            "VorgangId": self.VorgangId,
            "Objekt": self.Objekt.get_dict(),
            "Mitarbeiter": self.Mitarbeiter.get_dict(),
            "KmStandVorher": self.KmStandVorher,
            "KmStandNachher": self.KmStandNachher,
            "GefahreneKm": self.Gefahrene_Kilometer,
            "MieteStart": self.MieteStart,
            "MieteEnde": self.MieteEnde
        }
        return dicts

    @staticmethod
    def create(connection, ObjektId, MitarbeiterID, KmStandVorher, KmStandNachher, GefahreneKilometer, MieteStart, MieteEnde):
        cursor = connection.cursor()
        sql = "INSERT INTO MietVorgang (ObjektID, MitarbeiterID, KmStandVorher, KmStandNachher, GefahreneKm, MieteStart, MieteEnde) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (ObjektId, MitarbeiterID, KmStandVorher, KmStandNachher, GefahreneKilometer, MieteStart, MieteEnde)
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def read(connection, MietVorgangId):
        cursor = connection.cursor()
        sql = "SELECT * FROM MietVorgang WHERE VorgangID = %s"
        val = [MietVorgangId]
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            result = list(result)
            result[7] = MietObjekt.get(connection, result[7])
            result[6] = Mitarbeiter.read(connection, result[6])
            return MietVorgang(*result)
        else:
            return None

    def update(self, connection):
        cursor = connection.cursor()
        sql = "UPDATE MietVorgang SET ObjektID = %s, MitarbeiterID = %s, KmStandVorher = %s, KmStandNachher = %s, GefahreneKm = %s, MieteStart = %s, MieteEnde = %s WHERE VorgangID = %s"
        val = (self.Objekt, self.Mitarbeiter, self.KmStandVorher, self.KmStandNachher, self.Gefahrene_Kilometer, self.MieteStart, self.MieteEnde, self.VorgangId)
        cursor.execute(sql, val)
        connection.commit()

    def delete(self, connection):
        cursor = connection.cursor()
        sql = "DELETE FROM MietVorgang WHERE VorgangID = %s"
        val = self.VorgangId
        cursor.execute(sql, val)
        connection.commit()

    @staticmethod
    def get_all(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM MietVorgang")
        results = cursor.fetchall()
        mietvertraege = []
        for row in results:
            row = list(row)
            row[7] = MietObjekt.get(connection, row[7])
            row[6] = Mitarbeiter.read(connection, row[6])
            mietvertrag = MietVorgang(*row)
            mietvertraege.append(mietvertrag)
        return mietvertraege
