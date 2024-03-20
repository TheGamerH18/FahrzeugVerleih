import mysql.connector

class Inspektion:
    def __init__(self, InspektionID, FahrzeugID, Datum_letzte_Inspektion):
        self.InspektionID = InspektionID
        self.FahrzeugID = FahrzeugID
        self.Datum_letzte_Inspektion = Datum_letzte_Inspektion

    @staticmethod
    def create(connection, FahrzeugID, Datum_letzte_Inspektion):
        cursor = connection.cursor()
        sql = "INSERT INTO Inspektionen (FahrzeugID, Datum_letzte_Inspektion) VALUES (%s, %s)"
        val = (FahrzeugID, Datum_letzte_Inspektion)
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def read(connection, InspektionID):
        cursor = connection.cursor()
        sql = "SELECT * FROM Inspektionen WHERE InspektionID = %s"
        val = InspektionID
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return Inspektion(*result)
        else:
            return None

    def update(self, connection):
        cursor = connection.cursor()
        sql = "UPDATE Inspektionen SET FahrzeugID = %s, Datum_letzte_Inspektion = %s WHERE InspektionID = %s"
        val = (self.FahrzeugID, self.Datum_letzte_Inspektion, self.InspektionID)
        cursor.execute(sql, val)
        connection.commit()

    def delete(self, connection):
        cursor = connection.cursor()
        sql = "DELETE FROM Inspektionen WHERE InspektionID = %s"
        val = self.InspektionID
        cursor.execute(sql, val)
        connection.commit()
