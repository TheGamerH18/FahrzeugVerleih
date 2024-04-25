import mysql.connector

class Bauart:
    def __init__(self, BauartId, Marke, Modell, Bauform):
        self.BauartId = BauartId
        self.Marke = Marke
        self.Modell = Modell
        self.Bauform = Bauform

    @staticmethod
    def create(connection, Marke, Modell, Bauform):
        cursor = connection.cursor()
        sql = "INSERT INTO Bauart(Marke, Modell, Bauform) VALUES (%s, %s, %s)"
        val = (Marke, Modell, Bauform)
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def get_all(connection):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Bauart')
        dbresult = cursor.fetchall()
        bauarten = []
        for row in dbresult:
            bauarten.append(Bauart(*row))
        return bauarten

    @staticmethod
    def read(connection, bauart_id):
        cursor = connection.cursor()
        sql = ("SELECT * FROM Bauart WHERE BauartId = %s", (bauart_id,))
        value = bauart_id
        cursor.execute(sql, value)
        dbresult = cursor.fetchone()
        if dbresult:
            return Bauart(*dbresult)
        else:
            return None