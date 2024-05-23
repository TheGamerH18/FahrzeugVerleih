CREATE DATABASE ausleihen_fahrzeuge;
USE ausleihen_fahrzeuge;

CREATE TABLE IF NOT EXISTS Bauart (
    BauartID INT NOT NULL AUTO_INCREMENT,
    Marke VARCHAR(255),
    Modell VARCHAR(255),
    Bauform VARCHAR(255),
    PRIMARY KEY (BauartID)
);

CREATE TABLE IF NOT EXISTS Users(
    UserName VARCHAR(255),
    Password VARCHAR(255),
    Level INT,
    PRIMARY KEY (UserName)
);

CREATE TABLE IF NOT EXISTS Mietobjekt (
    ObjektID INT NOT NULL AUTO_INCREMENT,
    BauartID INT,
    Kennzeichen VARCHAR(255),
    Baujahr VARCHAR(255),
    Kraftstoff VARCHAR(255),
    LetzteInspektion DATE,
    PRIMARY KEY (ObjektID),
    FOREIGN KEY (BauartID) REFERENCES Bauart(BauartID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Mitarbeiter (
    MitarbeiterID INT NOT NULL AUTO_INCREMENT,
    Vorname VARCHAR(255),
    Nachname VARCHAR(255),
    PRIMARY KEY (MitarbeiterID)
);

CREATE TABLE IF NOT EXISTS Mietvorgang (
    VorgangID INT NOT NULL AUTO_INCREMENT,
    KmStandVorher INT,
    KmStandNachher INT,
    GefahreneKm INT,
    MieteStart DATETIME,
    MieteEnde DATETIME,
    MitarbeiterID INT,
    ObjektID INT,
    PRIMARY KEY (VorgangID),
    FOREIGN KEY (MitarbeiterID) REFERENCES Mitarbeiter(MitarbeiterID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ObjektID) REFERENCES Mietobjekt(ObjektID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Users
    (UserName, Password, Level)
VALUES
    ('root', 'root', 0);


INSERT INTO mitarbeiter
    (Vorname, Nachname)
VALUES
    ('Axel', 'Franz'),
    ('Jonas', 'Schäfer'),
    ('Serap', 'Özdemir'),
    ('Maria', 'Poller'),
    ('Dimos', 'Sokolow'),
    ('Gisela', 'Zelt'),
    ('Eda',	'Yilma'),
    ('Maris', 'Brink'),
    ('Eli', 'Demir');

INSERT INTO Bauart
    (Marke, Modell)
VALUES
    ('Ford', 'Mondeo'),
    ('Ford', 'Kuga'),
    ('Smart', ''),
    ('Zündapp', 'Z517 700c'),
    ('Fischer', 'Trekking E-Bike VIATOR 5.0i');

INSERT INTO Mietobjekt
    (BauartID, Kennzeichen, Baujahr, Kraftstoff, LetzteInspektion)
VALUES
    (1, 'K-MA-278', '2020', 'Diesel', '1000-01-01'),
    (1, 'K-MA-279', '2019', 'Benziner', '2021-05-20'),
    (2, 'K-MA-280', '2021', 'Benziner', '2020-12-19'),
    (3, 'K-MA-281', '2019', 'Hybrid', '2021-08-05'),
    (3, 'K-MA-282', '2019', 'Hybrid', '2020-01-05'),
    (3, 'K-MA-283', '2019', 'Hybrid', '2021-01-05'),
    (4, 'EP14766', '2020', 'Muskelkraft', '2021-01-05'),
    (4, 'EP17816', '2020', 'Muskelkraft', '2021-05-10'),
    (5, '81782', '2021', 'Muskelkraft', '2021-05-10'),
    (5, '58741', '2021', 'Muskelkraft', '2021-05-10');

INSERT INTO Mietvorgang
    (KmStandVorher, KmStandNachher, GefahreneKm, MieteStart, MieteEnde, MitarbeiterID, ObjektID)
VALUES
    (10896, 10923, 27, '2021-08-02 09:00:00', '2021-08-02 12:00:00', 1, 1),
    (10923, 11035, 112, '2021-08-04 00:00:00', '2021-08-05 23:59:59', 2, 1),
    (11035, 11833, 798, '2021-08-09 00:00:00', '2021-08-13 23:59:59', 3, 1),
    (11833, 11885, 52, '2021-08-16 09:00:00', '2021-08-16 14:00:00', 4, 1),
    (11885, 11912, 27, '2021-08-17 09:00:00', '2021-08-17 15:00:00', 1, 1),
    (11912, 11939, 27, '2021-08-21 08:00:00', '2021-08-21 12:00:00', 1, 1),
    (15500, 15649, 149, '2021-08-16 09:00:00', '2021-08-16 14:00:00', 3, 2),
    (9023, 9574, 571, '2021-08-18 09:00:00', '2021-08-18 18:00:00', 5, 3),
    (54194, 55219, 1025, '2021-08-12 09:00:00', '2021-08-12 19:00:00', 6, 4),
    (5519, 5544, 25, '2021-08-14 08:00:00', '2021-08-14 13:00:00', 6, 4),
    (26547, 26572, 25, '2021-08-10 09:00:00', '2021-08-10 19:00:00', 6, 5),
    (4915, 5301, 386, '2021-08-20 11:00:00', '2021-08-20 17:00:00', 7, 6),
    (5092, 5301, 209, '2021-08-27 08:00:00', '2021-08-27 17:00:00', 7, 6),
	(NULL, NULL, NULL, '2021-08-04 00:00:00', '2021-08-05 23:59:59', 8, 7),
    (NULL, NULL, NULL, '2021-08-06 00:00:00', '2021-08-06 23:59:59', 8, 7),
    (Null, NULL, NULL, '2021-08-14 00:00:00', '2021-08-14 23:59:59', 9, 8);