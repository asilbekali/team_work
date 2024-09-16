from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='953901313',
    database='blog_post'
)

class MyPost(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(550, 600)
        self.v_main_lay = QVBoxLayout()

        self.main_lbl = QLabel("Mening postlarim")
        self.main_lbl.setFont(QFont("Arial", 20))
        self.main_lbl.setAlignment(Qt.AlignCenter)
        self.v_main_lay.addWidget(self.main_lbl)

        self.qlis = QListWidget()
        self.v_main_lay.addWidget(self.qlis)
        self.qlis.setFixedHeight(500)

        self.load_posts()

        self.setLayout(self.v_main_lay)

    def load_posts(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT word from post inner join users on post.id = users.post_id")  
        posts = cursor.fetchall()

        for post in posts:
            self.qlis.addItem(post[0])
            

if __name__ == '__main__':
    app = QApplication([])
    w = MyPost()
    w.setWindowTitle("Mening Postlarim") 
    w.show()
    app.exec_()
