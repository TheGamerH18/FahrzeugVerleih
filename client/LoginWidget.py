import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QMainWindow, QLineEdit
from BauartenWidget import *
from Auth import Auth

class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button_style = """
                QPushButton {
                    background-color: #4CAF50; 
                    color: white;
                    border-radius: 10px;
                    font-size: 16px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                """

        self.setWindowTitle("Login")
        self.setFixedWidth(500)
        self.setFixedHeight(250)
        self.geometry().center()

        self.tbxBenutzername = QLineEdit()
        self.tbxBenutzername.setPlaceholderText("Benutzername")
        self.tbxBenutzername.setFixedHeight(30)
        self.tbxPasswort = QLineEdit()
        self.tbxPasswort.setPlaceholderText("Passwort")
        self.tbxPasswort.setFixedHeight(30)

        self.btnLogin = QPushButton("Login")
        self.btnLogin.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.tbxBenutzername)
        layout.addWidget(self.tbxPasswort)
        layout.addWidget(self.btnLogin)


        for i in range(layout.count()):
            layout.itemAt(i).widget().setStyleSheet(button_style)

        self.setLayout(layout)
    def login(self):
        Auth(self.tbxBenutzername.text(),self.tbxPasswort.text())
        print(Auth.getAuth())

app = QApplication(sys.argv)
widget = LoginWidget()
widget.show()
sys.exit(app.exec_())