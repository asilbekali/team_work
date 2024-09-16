from PyQt5.QtWidgets import *
from team_project import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import mysql.connector
from mypost import MyPost
from color_back import GradientWidget



mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "953901313",
    database = "blog_post"
)

class MyWindow(QWidget):
    def __init__(self,text):
        super().__init__()
        self.setFixedSize(1700, 900)
        self.gradient_widget = GradientWidget(self)
        self.gradient_widget.setGeometry(0, 0, 0, 0)
        self.gradient_widget.setStyleSheet("background: transparent;")

        self.user_nomer=text
        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.h_btn1_lay = QHBoxLayout()
        self.h_qlist_lay = QHBoxLayout()

        self.label = QLabel("My posts")
        self.label.setStyleSheet("""
            font-family: 'Comic Sans MS';
            font-size: 50px;
            font-weight: bold;
            color: white;
        """)
        
        self.write_post_btn = QPushButton("", clicked=self.createpost)
        self.write_post_btn.setIcon(QIcon("pen.png"))
        self.write_post_btn.setIconSize(QSize(50,50))
        self.write_post_btn.setStyleSheet("border-radius:10px")

        self.mypost_btn = QPushButton("", clicked=self.mypost)
        self.mypost_btn.setIcon(QIcon("man.png"))
        self.mypost_btn.setIconSize(QSize(50,50))
        self.mypost_btn.setStyleSheet("border-radius:10px")

        self.qlist = QListWidget()
        self.qlist.setFixedSize(1000,700)
        
        self.h_qlist_lay.addWidget(self.qlist)

        self.h_btn_lay.addStretch()
        self.h_btn_lay.addWidget(self.label)
        self.h_btn_lay.addStretch()
        self.h_btn_lay.addWidget(self.mypost_btn)

        self.h_btn1_lay.addStretch()
        self.h_btn1_lay.addWidget(self.write_post_btn)

        self.v_main_lay.addLayout(self.h_btn_lay)
        self.v_main_lay.addLayout(self.h_qlist_lay)
        self.v_main_lay.addLayout(self.h_btn1_lay)
        self.print_post()

        self.setLayout(self.v_main_lay)

    def print_post(self):
            cursor = mydb.cursor()
            cursor.execute("SELECT word , data from post inner join users on post.id = users.post_id")
            posts = cursor.fetchall()
            for post in posts:
                print(post)
                self.qlist.addItem(post[0])
                self.qlist.addItem(str(post[1]))


    def createpost(self):
        self.obj=Post(self.user_nomer)
        self.obj.show()

    def mypost(self):
            self.post = MyPost()
            self.post.show()

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow("salom")
    win.show()
    app.exec_()

