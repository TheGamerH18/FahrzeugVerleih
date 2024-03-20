import mysql.connector

class Fahrzeug:
    def __init__(self, FahrzeugID, Art, Modell, Nummernschild_Rahmennummer, Baujahr, Typ, Treibstoff):
        self.FahrzeugID = FahrzeugID
        self.Art = Art
        self.Modell = Modell
        self.Nummernschild_Rahmennummer = Nummernschild_Rahmennummer
        self.Baujahr = Baujahr
        self.Typ = Typ
        self.Treibstoff = Treibstoff

    @staticmethod
    def create(connection, Art, Modell, Nummernschild_Rahmennummer, Baujahr, Typ, Treibstoff):
        cursor = connection.cursor()
        sql = "INSERT INTO Fahrzeuge (Art, Modell, Nummernschild_Rahmennummer, Baujahr, Typ, Treibstoff) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (Art, Modell, Nummernschild_Rahmennummer, Baujahr, Typ, Treibstoff)
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def read(connection, FahrzeugID):
        cursor = connection.cursor()
        sql = "SELECT * FROM Fahrzeuge WHERE FahrzeugID = %s"
        val = FahrzeugID
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return Fahrzeug(*result)
        else:
            return None

    def update(self, connection):
        cursor = connection.cursor()
        sql = "UPDATE Fahrzeuge SET Art = %s, Modell = %s, Nummernschild_Rahmennummer = %s, Baujahr = %s, Typ = %s, Treibstoff = %s WHERE FahrzeugID = %s"
        val = (self.Art, self.Modell, self.Nummernschild_Rahmennummer, self.Baujahr, self.Typ, self.Treibstoff, self.FahrzeugID)
        cursor.execute(sql, val)
        connection.commit()

    def delete(self, connection):
        cursor = connection.cursor()
        sql = "DELETE FROM Fahrzeuge WHERE FahrzeugID = %s"
        val = self.FahrzeugID
        cursor.execute(sql, val)
        connection.commit()
