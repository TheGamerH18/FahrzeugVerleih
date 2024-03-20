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
