from PyQt5.QtWidgets import *
from mypost import MyPost
import mysql.connector
from team_project import *


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rustamjon1",
    database = "blog_post"
)

class MyWindow(QWidget):
    def __init__(self,text):
        super().__init__()
        self.user_nomer=text
        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        
        self.write_post_btn = QPushButton("Post yozish", clicked=self.createpost)
        self.mypost_btn = QPushButton("Postlarim", clicked=self.mypost)
        self.qlist = QListWidget()

        self.h_btn_lay.addWidget(self.write_post_btn)
        self.h_btn_lay.addWidget(self.mypost_btn)

        self.v_main_lay.addLayout(self.h_btn_lay)
        self.v_main_lay.addWidget(self.qlist)
        self.print_post()

        self.setLayout(self.v_main_lay)

    def print_post(self):
            cursor = mydb.cursor()
            cursor.execute("SELECT word from post inner join users on post.id = users.post_id")
            posts = cursor.fetchall()
            for post in posts:
                self.qlist.addItem(post[0])


    def createpost(self):
        self.obj=Post(self.user_nomer)
        self.obj.show()

    def mypost(self):
            self.post = MyPost()
            self.post.show()

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()

