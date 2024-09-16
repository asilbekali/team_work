from PyQt5.QtWidgets import *
import mysql.connector




mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rustamjon1",
    database="blog_orginal",
)


class Post(QWidget):
    def __init__(self,text):
        super().__init__()
        self.setFixedSize(300, 400)
        self.user=text
        self.v_b = QVBoxLayout()
        self.line_post = QLineEdit()
        self.line_post.setPlaceholderText("Enter")
        self.btn = QPushButton("Click")
        self.btn.clicked.connect(self.bosdi)
        self.v_b.addWidget(self.line_post)
        self.v_b.addStretch()
        self.v_b.addStretch()
        self.v_b.addWidget(self.btn)
        self.setLayout(self.v_b)
        self.line_post.setStyleSheet("border: 2px solid black; border-radius: 6px; font-size: 20px;")
        self.btn.setStyleSheet("font-size: 20px;")



    def bosdi(self):
        mycursor = mydb.cursor()

    # Foydalanuvchining id sini olish
        mycursor.execute("SELECT id FROM users WHERE number = %s", (self.user,))
        result = mycursor.fetchone()

        if result:
            user_id = result[0]
            text = self.line_post.text()

        # Postni qo'shish
            mycursor.execute("""
            INSERT INTO post (author_id, word) VALUES (%s, %s)
            """, (user_id, text))
            mydb.commit()

        # Yangi post ID-sini olish
            post_id = mycursor.lastrowid

        # Post ID-sini foydalanuvchining post_id ustuniga qo'shish
            mycursor.execute("""
            UPDATE users 
            SET post_id = COALESCE(CONCAT(post_id, ',', %s), %s) 
            WHERE id = %s
            """, (post_id, post_id, user_id))
            mydb.commit()

            self.line_post.clear()
        else:
                print("User topilmadi")

if __name__ == "__main__":
    app = QApplication([])
    win = Post('sasa')
    win.show()
    app.exec_()