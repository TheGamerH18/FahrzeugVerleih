import mysql.connector
from datetime import datetime

from MietObjekt import MietObjekt

class MietVorgang:
    def __init__(self, VorgangId: int, objekt: MietObjekt, MitarbeiterID, KilometerstandVorher: int, KilometerstandNacher: int, GefahreneKilometer: int, MieteStart: datetime, MieteEnde: datetime):
        self.VorgangId = VorgangId
        self.Objekt = objekt
        self.MitarbeiterID = MitarbeiterID
        self.KmStandVorher = KilometerstandVorher
        self.KmStandNachher = KilometerstandNacher
        self.Gefahrene_Kilometer = GefahreneKilometer
        self.MieteStart = MieteStart
        self.MieteEnde = MieteEnde


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
        val = MietVorgangId
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return MietVorgang(*result)
        else:
            return None

    def update(self, connection):
        cursor = connection.cursor()
        sql = "UPDATE MietVorgang SET ObjektID = %s, MitarbeiterID = %s, KmStandVorher = %s, KmStandNachher = %s, GefahreneKm = %s, MieteStart = %s, MieteEnde = %s WHERE VorgangID = %s"
        val = (self.Objekt, self.MitarbeiterID, self.KmStandVorher, self.KmStandNachher, self.Gefahrene_Kilometer, self.MieteStart, self.MieteEnde, self.VorgangId)
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
        cursor.execute("SELECT VorgangId, ObjektId, MitarbeiterID, KmStandVorher, KmStandNachher, GefahreneKm, MieteStart, MieteEnde FROM MietVorgang")
        results = cursor.fetchall()
        mietvertraege = []
        for row in results:
            li = list(row)
            
            mietvertrag = MietVorgang(*row)
            mietvertraege.append(mietvertrag)
        return mietvertraege
