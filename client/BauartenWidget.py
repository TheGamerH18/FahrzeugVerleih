import requests
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QApplication, QTableWidgetItem
import Auth
from klassen import Bauart

class BauartenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Bauarten")
        self.showMaximized()
        auth = Auth("arndt", "zzzzz")
        request = requests.get('localhost:5000/mietvertraege', auth=auth.getAuth())
        data = request.json()

        layout = QVBoxLayout()
        list_bauarten = QTableWidgetItem()
        list_bauarten.data(data)
        layout.addWidget(list_bauarten)
        self.setLayout(layout)