import json

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QApplication, QTableWidgetItem, QTableWidget, QStyleFactory
from Auth import Auth
from klassen import Bauart

class BauartenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Miet Objekte")
        self.showMaximized()
        auth = Auth("root", "root")
        request = requests.get('http://localhost:5000/objekte', auth=auth.getAuth())
        json_objekte = request.json()

        tabelle = QTableWidget()
        tabelle.setColumnCount(7)
        tabelle.setHorizontalHeaderLabels(
            ['ObjektId', 'Marke', 'Modell', 'Baujahr', 'Kennzeichen', 'Kraftstoff', 'Letzte Inspektion'])
        tabelle.setRowCount(len(json_objekte))

        for row, item in enumerate(json_objekte):
            tabelle.setItem(row, 0, QTableWidgetItem(str(item['ObjektId'])))
            tabelle.setItem(row, 1, QTableWidgetItem(item['Bauart']['Marke']))
            (tabelle.setItem(row, 2, QTableWidgetItem(item['Bauart']['Modell'] if item['Bauart']['Modell'] else '')))
            tabelle.setItem(row, 3, QTableWidgetItem(item['Baujahr']))
            tabelle.setItem(row, 4, QTableWidgetItem(item['Kennzeichen']))
            tabelle.setItem(row, 5, QTableWidgetItem(item['Kraftstoff']))
            tabelle.setItem(row, 6, QTableWidgetItem(item['LetzteInspektion']))

        tabelle.setAlternatingRowColors(True)
        tabelle.setStyleSheet("alternate-background-color: lightblue; background-color: white;")
        tabelle.horizontalHeader().setSectionResizeMode(3)
        tabelle.verticalHeader().setVisible(False)
        tabelle.setShowGrid(True)
        tabelle.setGridStyle(Qt.SolidLine)
        tabelle.setSelectionBehavior(QTableWidget.SelectRows)
        tabelle.setSelectionMode(QTableWidget.SingleSelection)

        layout = QVBoxLayout()
        layout.addWidget(tabelle)
        self.setLayout(layout)
