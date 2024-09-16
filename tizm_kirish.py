import json
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from main_window import MyWindow
from color_back import GradientWidget



import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rustamjon1",
    database = "blog_post"
)
print(mydb)




class Tizm(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1700,900)
        self.setStyleSheet("background:#fff;font-size:20px")

        self.gradient_widget = GradientWidget(self)
        self.gradient_widget.setGeometry(0, 0, 0, 0)
        self.gradient_widget.setStyleSheet("background: transparent;")

        self.h_lbl_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()
        self.v_asos_lyt = QVBoxLayout()
        self.rekursi()

    def rekursi(self):
        self.llbl = QLabel("Tizmga kirish")
        self.llbl.setStyleSheet("background-color: transparent;color:white;font-size:24px")
        self.ledit = QLineEdit()
        self.ledit.setFixedSize(400,40)
        self.ledit.setPlaceholderText("Telefon raqam")
        self.ledit.setStyleSheet("background:lightblue")

        self.pedit = QLineEdit()
        self.pedit.setFixedSize(400,40)
        self.pedit.setPlaceholderText("Parol")
        self.pedit.setStyleSheet("background:lightblue")

        self.cledit = QLineEdit()
        self.cledit.setPlaceholderText("Codni kiriting")
        self.cledit.setStyleSheet("background:lightgray")
        self.cledit.hide()

        self.lbtn = QPushButton("Log In",clicked=self.kirish)
        self.lbtn.setFixedSize(400,40)
        self.lbtn.setStyleSheet("""
            QPushButton {
                border-radius: 4px;
                background-color: #3498db; 
                color: white;
                border: 2px solid #2980b9;
            }
            QPushButton:hover {
                background-color: #216699;
                color: #ecf0f1;
            }
        """)

        self.exit_btn = QPushButton(self,clicked=self.qaytish)
        self.exit_btn.setFixedSize(40,30)
        self.exit_btn.move(20,20)
        self.exit_btn.setIcon(QIcon("images/back.png"))
        self.exit_btn.setIconSize(self.exit_btn.size())
        self.exit_btn.setStyleSheet("""
            QPushButton {
                border-radius: 4px;
                background-color: #3498db; 
                color: white;
                border: 2px solid #2980b9;
            }
            QPushButton:hover {
                background-color: #216699;
                color: #ecf0f1;
            }
        """)

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
            self.llbl.setStyleSheet("background-color: transparent;color:red;font-size:24px")
            self.ledit.clear()
            self.pedit.clear() 

    def qaytish(self):
        from main import MyWindow1
        self.regis = MyWindow1()
        self.regis.show()
        self.hide()

        
         

  


if __name__ == "__main__":
    app = QApplication([])
    win = Tizm()
    win.show()
    app.exec_()
