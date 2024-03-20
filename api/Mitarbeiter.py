import mysql.connector


class Mitarbeiter:
    def __init__(self, MitarbeiterID, Vorname, Nachname):
        self.MitarbeiterID = MitarbeiterID
        self.Vorname = Vorname
        self.Nachname = Nachname

    @staticmethod
    def create(connection, Vorname, Nachname):
        cursor = connection.cursor()
        sql = "INSERT INTO Mitarbeiter (Vorname, Nachname) VALUES (%s, %s)"
        val = (Vorname, Nachname)
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def read(connection, MitarbeiterID):
        cursor = connection.cursor()
        sql = "SELECT * FROM Mitarbeiter WHERE MitarbeiterID = %s"
        val = MitarbeiterID
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return Mitarbeiter(*result)
        else:
            return None

    def update(self, connection):
        cursor = connection.cursor()
        sql = "UPDATE Mitarbeiter SET Vorname = %s, Nachname = %s WHERE MitarbeiterID = %s"
        val = (self.Vorname, self.Nachname, self.MitarbeiterID)
        cursor.execute(sql, val)
        connection.commit()

    def delete(self, connection):
        cursor = connection.cursor()
        sql = "DELETE FROM Mitarbeiter WHERE MitarbeiterID = %s"
        val = self.MitarbeiterID
        cursor.execute(sql, val)
        connection.commit()

    @staticmethod
    def get_all(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Mitarbeiter")
        results = cursor.fetchall()
        mitarbeiter = []
        for row in results:
            m = Mitarbeiter(*row)
            mitarbeiter.append(m)
        return mitarbeiter
