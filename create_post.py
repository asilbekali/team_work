from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import mysql.connector
from datetime import datetime
from PyQt5.QtCore import QTimer
class Create_post(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:white;")
        self.setFixedSize(500, 600)
        self.space_lbl=QLabel()
        self.space_lbl.setFixedHeight(30)
        self.scs_lbl=QLabel(self)
        self.scs_lbl.setStyleSheet("""
            font-family: 'Comic Sans MS';
            color: black;
            font-size: 20px;
          
        """)
        self.pic_label = QLabel(self)
        self.pic_label.setFixedSize(300, 300)
        self.pic_label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap("notepad.png")
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pic_label.setPixmap(scaled_pixmap)

        v_main_lay = QVBoxLayout()
        h_btn_lay = QHBoxLayout()  
        self.ok_btn = QPushButton("OK",clicked=self.connetor)
        self.exit_btn = QPushButton("EXIT",clicked=self.exit)
        self.button_style2(self.ok_btn)
        self.button_style2(self.exit_btn)
        self.ok_btn.setFixedSize(60,60)
        self.exit_btn.setFixedSize(60,60)
        self.post_text_edit = QTextEdit()
        self.post_text_edit.setGeometry(100, 100, 300, 50)  
        self.post_text_edit.setPlaceholderText("O'z sahifangizni shu yerda yarating ")
        self.post_text_edit.setStyleSheet("""
            font-family: 'Comic Sans MS';
            color: black;
            background-color: #FAFAD2; 
            border: 1px solid black;
            font-size: 20px;
            border-radius: 10px;
        """)
        h_btn_lay.addWidget(self.ok_btn)
        h_btn_lay.addWidget(self.exit_btn)
        v_main_lay.addWidget(self.pic_label)
        v_main_lay.addWidget(self.post_text_edit)
        v_main_lay.addWidget(self.scs_lbl)
        v_main_lay.addLayout(h_btn_lay)
        v_main_lay.addWidget(self.space_lbl)
        
        self.setLayout(v_main_lay)
    def button_style2(self, btn):
        btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                font-size: 20px;
                border-radius: 30px;
                color:#d4af37
            }
            QPushButton:hover {
                background-color: #FAFAD2;
                font-size: 28px;
                border-radius: 30px;
                color:black
            }
        """)


    def connetor(self):
        telefon = "+998905133030"
        post = self.post_text_edit.toPlainText() 
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rustamjon1",
            database="note_pad"
        )
        cursor = mydb.cursor()
        
        cursor.execute("SELECT id FROM users WHERE number = %s", (telefon,))
        myresult = cursor.fetchone()
        

        self.id = myresult[0]
        
           
        insert_query = """
        INSERT INTO post (author_id, word, post_time)
        VALUES (%s, %s, %s)
        """
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(insert_query, (self.id, post, current_time))
        mydb.commit()
        cursor.close()
        mydb.close()
        self.scs_lbl.setText("Post muvaffaqiyatli qo'shildi")
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(2000) 
    def update_progress(self):
        self.post_text_edit.clear()
        self.scs_lbl.setText("") 
        self.timer.stop() 
    def exit(self):
        self.hide()

if __name__ == "__main__":
    app = QApplication([])
    win = Create_post()
    win.show()
    app.exec_()
