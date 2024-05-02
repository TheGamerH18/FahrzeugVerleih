import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QApplication
import requests


class ObjekteWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Objekte")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.btn_get_objekte = QPushButton("Get Objekte")
        self.btn_get_objekte.clicked.connect(self.get_objekte)
        layout.addWidget(self.btn_get_objekte)

        self.setLayout(layout)

    def get_objekte(self):
        response = requests.get("http://127.0.0.1:5000/objekte?X-API-KEY=YOUR_API_KEY")
        if response.status_code == 200:
            data = response.json()
            self.display_data(data)
        else:
            print("Error:", response.status_code)

    def display_data(self, data):
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))


class MietvertraegeWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mietvertraege")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.btn_get_mietvertraege = QPushButton("Get Mietvertraege")
        self.btn_get_mietvertraege.clicked.connect(self.get_mietvertraege)
        layout.addWidget(self.btn_get_mietvertraege)

        self.setLayout(layout)

    def get_mietvertraege(self):
        response = requests.get("http://127.0.0.1:5000/mietvertraege?X-API-KEY=YOUR_API_KEY")
        if response.status_code == 200:
            data = response.json()
            self.display_data(data)
        else:
            print("Error:", response.status_code)

    def display_data(self, data):
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))


class MitarbeiterWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mitarbeiter")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.btn_get_mitarbeiter = QPushButton("Get Mitarbeiter")
        self.btn_get_mitarbeiter.clicked.connect(self.get_mitarbeiter)
        layout.addWidget(self.btn_get_mitarbeiter)

        self.setLayout(layout)

    def get_mitarbeiter(self):
        response = requests.get("http://127.0.0.1:5000/mitarbeiter?X-API-KEY=YOUR_API_KEY")
        if response.status_code == 200:
            data = response.json()
            self.display_data(data)
        else:
            print("Error:", response.status_code)

    def display_data(self, data):
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ObjekteWindow()
    window.show()
    sys.exit(app.exec_())
