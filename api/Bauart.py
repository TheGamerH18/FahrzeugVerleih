import mysql.connector

class Bauart:
    def __init__(self, BauartId: int, Marke: str, Modell: str, Bauform: str):
        self.BauartId = BauartId
        self.Marke = Marke
        self.Modell = Modell
        self.Bauform = Bauform

    def update(self, connection):
        cursor = connection.cursor()
        sql = "UPDATE Bauart SET Marke = %s, Modell = %s, Bauform = %s WHERE BauartId = %s"
        val = (self.Marke, self.Modell, self.Bauform, self.BauartId)
        cursor.execute(sql, val)
        connection.commit()


    def delete(self, connection):
        cursor = connection.cursor()
        sql = "DELETE FROM Bauart WHERE BauartId = %s"
        val = self.BauartId
        cursor.execute(sql, val)
        connection.commit()

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