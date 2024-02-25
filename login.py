from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import sys

os.system("cls")

class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Facebook")
        self.setFixedSize(1920, 1080)
        self.setStyleSheet("""
                            background-color: #F0F2F5;
                            """)
        self.mainLayout = QHBoxLayout(self)

        self.LchildLayout = QVBoxLayout()
        self.LchildLayout.setSpacing(0)
        self.LchildLayout.setContentsMargins(300, 300, 100, 500)
        

        self.Facebook = QLabel("facebook")
        self.Facebook.setFixedSize(500, 100)
        self.Facebook.setFont(QFont("Montserrat", 45, weight= 100))
        self.Facebook.setStyleSheet("""
                                    color: #0866FF;
                                    """)
        self.LchildLayout.addWidget(self.Facebook)

        self.FaLine = QLabel("Connect with friends and the world\naround you on Facebook.")
        self.FaLine.setFont(QFont("Montserrat", 20, weight= 100))
        self.FaLine.setFixedSize(600, 80)
        self.FaLine.setStyleSheet("""
                                    color: black;
                                    """)
        self.LchildLayout.addWidget(self.FaLine)

        self.mainLayout.addLayout(self.LchildLayout)

        self.RchildLayout = QVBoxLayout()
        self.RchildLayout.setContentsMargins(50, 200, 200, 300)

        self.widgLchildLayout = QWidget()
        self.widgLchildLayout.setFixedSize(600, 500)
        self.widgLchildLayout.setStyleSheet("""
                                    background-color: white;
                                    """)
        
        self.layt1 = QVBoxLayout(self.widgLchildLayout)
        self.layt1.setSpacing(10)
        self.layt1.setContentsMargins(25, 100, 0, 100)

        self.lineLogin = QLineEdit()
        self.lineLogin.setPlaceholderText("Email")
        self.lineLogin.setFixedSize(550, 60)
        self.lineLogin.setFont(QFont("Calibri", 18,))
        self.layt1.addWidget(self.lineLogin)


        self.Password = QLineEdit()
        self.Password.setPlaceholderText("Password")
        self.Password.setFixedSize(550, 60)
        self.Password.setFont(QFont("Calibri", 18,))
        self.layt1.addWidget(self.Password)

        self.IcCorEmailOrPass = QLabel()
        self.IcCorEmailOrPass.setFixedSize(550, 60)
        self.IcCorEmailOrPass.setFont(QFont("Calibri", 15, weight=50))
        self.IcCorEmailOrPass.setStyleSheet("""
                                color: red;
                                 """)
        
        self.layt1.addWidget(self.IcCorEmailOrPass)

        self.LogIn = QPushButton("Log In", clicked=lambda: self.IsCorrectUser())
        self.LogIn.setStyleSheet("""
                                background-color: #0866FF;
                                color: white;
                                 """)
        self.LogIn.setFixedSize(550, 60)
        self.LogIn.setFont(QFont("Calibri", 18,))
        self.layt1.addWidget(self.LogIn)


        self.RchildLayout.addWidget(self.widgLchildLayout)
        self.mainLayout.addLayout(self.RchildLayout)
        
        self.show()

    def IsCorrectUser(self):
        if self.checkUser():
            self.IcCorEmailOrPass.setText("")
            MessBox = QMessageBox(self)
            MessBox.setWindowTitle("Log In")
            MessBox.setText("Log in Successfully")
            MessBox.setIcon(QMessageBox.Information)
            MessBox.setStandardButtons(QMessageBox.Ok)

            MessBox.exec_()

        else:
            self.IcCorEmailOrPass.setText("Incorrect Username or password!")

    def checkUser(self) -> bool:
        if not os.path.exists("baza.txt"):
            file = open("baza.txt", "x")
            return False
        with open("baza.txt", "r") as file:
            ls = file.readlines()

            CurEmail = self.lineLogin.text()
            CurPassword = self.Password.text()
            for i in ls:
                i = i.split(" | ")
                print(i)
                if CurEmail == i[3] and CurPassword == i[4][:-1]:
                    return True
        return False

app = QApplication([])
main = Login()
app.exec_()