import mysql.connector

class Mietvertrag:
    def __init__(self, MietvertragID, FahrzeugID, MitarbeiterID, Mietzeitraum, Kilometerstand_vorher,
                 Kilometerstand_nachher, Gefahrene_Kilmeter, Mietzeit_tage, Mietzeit_zeit, miet_ende):
        self.MietvertragID = MietvertragID
        self.FahrzeugID = FahrzeugID
        self.MitarbeiterID = MitarbeiterID
        self.Mietzeitraum = Mietzeitraum
        self.Kilometerstand_vorher = Kilometerstand_vorher
        self.Kilometerstand_nachher = Kilometerstand_nachher
        self.Gefahrene_Kilmeter = Gefahrene_Kilmeter
        self.Mietzeit_tage = Mietzeit_tage
        self.Mietzeit_zeit = Mietzeit_zeit
        self.miet_ende = miet_ende

    @staticmethod
    def create(connection, FahrzeugID, MitarbeiterID, Mietzeitraum, Kilometerstand_vorher,
                 Kilometerstand_nachher, Gefahrene_Kilmeter, Mietzeit_tage, Mietzeit_zeit, miet_ende):
        cursor = connection.cursor()
        sql = "INSERT INTO Mietverträge (FahrzeugID, MitarbeiterID, Mietzeitraum, Kilometerstand_vorher, Kilometerstand_nachher, Gefahrene_Kilmeter, Mietzeit_tage, Mietzeit_zeit, miet_ende) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (FahrzeugID, MitarbeiterID, Mietzeitraum, Kilometerstand_vorher, Kilometerstand_nachher, Gefahrene_Kilmeter, Mietzeit_tage, Mietzeit_zeit, miet_ende)
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def read(connection, MietvertragID):
        cursor = connection.cursor()
        sql = "SELECT * FROM Mietverträge WHERE MietvertragID = %s"
        val = MietvertragID
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return Mietvertrag(*result)
        else:
            return None

    def update(self, connection):
        cursor = connection.cursor()
        sql = "UPDATE Mietverträge SET FahrzeugID = %s, MitarbeiterID = %s, Mietzeitraum = %s, Kilometerstand_vorher = %s, Kilometerstand_nachher = %s, Gefahrene_Kilmeter = %s, Mietzeit_tage = %s, Mietzeit_zeit = %s, miet_ende = %s WHERE MietvertragID = %s"
        val = (self.FahrzeugID, self.MitarbeiterID, self.Mietzeitraum, self.Kilometerstand_vorher,
                 self.Kilometerstand_nachher, self.Gefahrene_Kilmeter, self.Mietzeit_tage, self.Mietzeit_zeit, self.miet_ende, self.MietvertragID)
        cursor.execute(sql, val)
        connection.commit()

    def delete(self, connection):
        cursor = connection.cursor()
        sql = "DELETE FROM Mietverträge WHERE MietvertragID = %s"
        val = self.MietvertragID
        cursor.execute(sql, val)
        connection.commit()

    @staticmethod
    def get_all(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Mietverträge")
        results = cursor.fetchall()
        mietvertraege = []
        for row in results:
            mietvertrag = Mietvertrag(*row)
            mietvertraege.append(mietvertrag)
        return mietvertraege
