import json
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from main_window import MyWindow


import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "953901313",
    database = "blog_post"
)
print(mydb)




class Tizm(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1700,900)
        self.setStyleSheet("background:#fff;font-size:20px")

        self.h_lbl_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()
        self.v_asos_lyt = QVBoxLayout()
        self.rekursi()

    def rekursi(self):
        self.llbl = QLabel("Tizmga kirish")
        self.llbl.setStyleSheet("font-size:24px;color:rgb(51,51,51)")
        self.ledit = QLineEdit()
        self.ledit.setPlaceholderText("Telefon raqam")
        self.ledit.setStyleSheet("background:lightgray")

        self.pedit = QLineEdit()
        self.pedit.setPlaceholderText("Parol")
        self.pedit.setStyleSheet("background:lightgray")

        self.cledit = QLineEdit()
        self.cledit.setPlaceholderText("Codni kiriting")
        self.cledit.setStyleSheet("background:lightgray")
        self.cledit.hide()

        self.lbtn = QPushButton("Kirish",clicked=self.kirish)
        self.lbtn.setStyleSheet("background:skyblue")

        self.v_main_lyt.addWidget(self.llbl)
        self.v_main_lyt.addWidget(self.ledit)
        self.v_main_lyt.addWidget(self.pedit)
        self.v_main_lyt.addWidget(self.cledit)
        self.v_main_lyt.addWidget(self.lbtn)

        self.h_lbl_lyt.addStretch()
        self.h_lbl_lyt.addLayout(self.v_main_lyt)
        self.h_lbl_lyt.addStretch()

        self.v_asos_lyt.addStretch()
        self.v_asos_lyt.addLayout(self.h_lbl_lyt)
        self.v_asos_lyt.addStretch()

        self.setLayout(self.v_asos_lyt)


    def kirish(self):
        mycursor = mydb.cursor()
        mycursor.execute(f"select * from users where number='{self.ledit.text()}' and password='{self.pedit.text()}'")
        myresalt = mycursor.fetchall()
        
        if myresalt:
            self.close()
            self.main = MyWindow(self.ledit.text())
            self.main.show()
        else:
            self.llbl.setText("Nomer yoki parol xato")
            self.llbl.setStyleSheet("color:red")
            self.ledit.clear()
            self.pedit.clear()    

  


if __name__ == "__main__":
    app = QApplication([])
    win = Tizm()
    win.show()
    app.exec_()
