import mysql.connector

class MietObjekt:
    def __init__(self, ObjektId: int, BauartId: int, Kennzeichen: str, Baujahr: str, Kraftstoff: str, LetzteInspektion):
        self.LetzteInspektion = LetzteInspektion
        self.ObjektId = ObjektId
        self.BauartId = BauartId
        self.Kennzeichen = Kennzeichen
        self.Baujahr = Baujahr
        self.Kraftstoff = Kraftstoff

    @staticmethod
    def create(connection, Bauart: Bauart, Kennzeichen: str, Baujahr: str, Kraftstoff: str, LetzteInspektion: datetime):
        cursor = connection.cursor()
        sql = "INSERT INTO Mietobjekt (BauartID, Kennzeichen, Baujahr, Kraftstoff, LetzteInspektion) VALUES (%s, %s, %s, %s, %s)"
        val = (Bauart.BauartId, Kennzeichen, Baujahr, Kraftstoff, LetzteInspektion)
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
            fahrzeug = MietObjekt(*row)
            mietobjekte.append(fahrzeug)
        return mietobjekte

    @staticmethod
    def read(connection, objekt_id):
        cursor = connection.cursor()
        sql = "SELECT * FROM Mietobjekt WHERE ObjektID = %s"
        val = objekt_id
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return MietObjekt(*result)
        else:
            return None

    def update(self, connection):
        cursor = connection.cursor()
        sql = "UPDATE Mietobjekt SET BauartID = %s, Kennzeichen = %s, Baujahr = %s, Kraftstoff = %s, LetzteInspektion = %s WHERE FahrzeugID = %s"
        val = (self.BauartId, self.Kennzeichen, self.Baujahr, self.Kraftstoff, self.LetzteInspektion, self.ObjektId)
        cursor.execute(sql, val)
        connection.commit()

    def delete(self, connection):
        cursor = connection.cursor()
        sql = "DELETE FROM Mietobjekt WHERE ObjektID = %s"
        val = self.ObjektId
        cursor.execute(sql, val)
        connection.commit()
