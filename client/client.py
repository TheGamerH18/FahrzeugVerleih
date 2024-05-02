import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDialog, QLabel
import requests
from dotenv import load_dotenv


class ObjekteWindow(QDialog):
    load_dotenv()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Objekte")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Response:")
        layout.addWidget(self.label)

        self.btn_get_objekte = QPushButton("Get Objekte")
        self.btn_get_objekte.clicked.connect(self.get_objekte)
        layout.addWidget(self.btn_get_objekte)

        self.setLayout(layout)

    def get_objekte(self):
        response = requests.get("http://127.0.0.1:5000/objekte?X-API-KEY=" + str(os.getenv('API_KEY')))
        if response.status_code == 200:
            data = response.json()
            self.label.setText("Response:\n" + str(data))
        else:
            self.label.setText("Error: " + str(response.status_code))


class MietvertraegeWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mietvertraege")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Response:")
        layout.addWidget(self.label)

        self.btn_get_mietvertraege = QPushButton("Get Mietvertraege")
        self.btn_get_mietvertraege.clicked.connect(self.get_mietvertraege)
        layout.addWidget(self.btn_get_mietvertraege)

        self.setLayout(layout)

    def get_mietvertraege(self):
        response = requests.get("http://127.0.0.1:5000/mietvertraege?X-API-KEY=" + str(os.getenv('API_KEY')))
        if response.status_code == 200:
            data = response.json()
            self.label.setText("Response:\n" + str(data))
        else:
            self.label.setText("Error: " + str(response.status_code))


class MitarbeiterWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mitarbeiter")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Response:")
        layout.addWidget(self.label)

        self.btn_get_mitarbeiter = QPushButton("Get Mitarbeiter")
        self.btn_get_mitarbeiter.clicked.connect(self.get_mitarbeiter)
        layout.addWidget(self.btn_get_mitarbeiter)

        self.setLayout(layout)

    def get_mitarbeiter(self):
        response = requests.get("http://127.0.0.1:5000/mitarbeiter?X-API-KEY=" + str(os.getenv('API_KEY')))
        if response.status_code == 200:
            data = response.json()
            self.label.setText("Response:\n" + str(data))
        else:
            self.label.setText("Error: " + str(response.status_code))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("API Manager")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.btn_objekte = QPushButton("Objekte")
        self.btn_objekte.clicked.connect(self.open_objekte_window)
        layout.addWidget(self.btn_objekte)

        self.btn_mietvertraege = QPushButton("Mietvertraege")
        self.btn_mietvertraege.clicked.connect(self.open_mietvertraege_window)
        layout.addWidget(self.btn_mietvertraege)

        self.btn_mitarbeiter = QPushButton("Mitarbeiter")
        self.btn_mitarbeiter.clicked.connect(self.open_mitarbeiter_window)
        layout.addWidget(self.btn_mitarbeiter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_objekte_window(self):
        self.objekte_window = ObjekteWindow()
        self.objekte_window.show()

    def open_mietvertraege_window(self):
        self.mietvertraege_window = MietvertraegeWindow()
        self.mietvertraege_window.show()

    def open_mitarbeiter_window(self):
        self.mitarbeiter_window = MitarbeiterWindow()
        self.mitarbeiter_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
