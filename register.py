from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import mysql.connector

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1700, 900)
        v_main_layout = QVBoxLayout()
        h_btn = QHBoxLayout()
        main_lbl = QLabel("WORDPAD UCHUN RO'YXATDAN O'TISH")
        main_lbl.setStyleSheet("font-size:50px;font-family: 'Comic Sans MS';color:white")
        main_lbl.setAlignment(Qt.AlignCenter)
  
        self.ln_user_name = QLineEdit()
        self.ln_user_name.setFixedSize(600,100)
        self.ln_user_name.setPlaceholderText("User name tanlang")
        self.ln_ism_edit = QLineEdit()
        self.ln_ism_edit.setFixedSize(600,100)
        self.ln_ism_edit.setPlaceholderText("Ismingizni kiriting")
        self.ln_phone_edit = QLineEdit()
        self.ln_phone_edit.setFixedSize(600,100)
        self.ln_phone_edit.setPlaceholderText("Telefon raqamingizni kiriting")
        self.ln_password_edit = QLineEdit()
        self.ln_password_edit.setFixedSize(600,100)
        self.ln_password_edit.setPlaceholderText("Parolingizni kiriting")

        self.line_style(self.ln_user_name)
        self.line_style(self.ln_ism_edit)
        self.line_style(self.ln_phone_edit)
        self.line_style(self.ln_password_edit)
     
        self.ok_btn = QPushButton("OK", clicked=self.connetor)
        self.ext_btn = QPushButton("Exit")
        self.line_style(self.ok_btn)
        self.line_style(self.ext_btn)

        self.ok_btn.setFixedSize(200,50)
        self.ext_btn.setFixedSize(200,50)
        v_main_layout.addStretch()
        v_main_layout.addWidget(main_lbl)
        v_main_layout.addStretch()
 
        line_edit_layout = QVBoxLayout()
        line_edit_layout.addWidget(self.ln_user_name)
        line_edit_layout.addWidget(self.ln_ism_edit)
        line_edit_layout.addWidget(self.ln_phone_edit)
        line_edit_layout.addWidget(self.ln_password_edit)
        line_edit_layout.setAlignment(Qt.AlignCenter)  
        
    
        v_main_layout.addLayout(line_edit_layout)
        h_btn.addWidget(self.ok_btn)
        h_btn.addWidget(self.ext_btn)
        v_main_layout.addStretch()
        v_main_layout.addLayout(h_btn)
        
        self.button_to_module1 = QPushButton("Loginga qaytish")
        v_main_layout.addWidget(self.button_to_module1)
        self.setLayout(v_main_layout)
        
        
        self.button_to_module1.clicked.connect(self.close)  
        print(11)

    def connetor(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rustamjon1",
            database="blog_orginal"
        )
        user_name = self.ln_user_name.text()
        ism = self.ln_ism_edit.text()
        telefon = self.ln_phone_edit.text()
        parol = self.ln_password_edit.text()
        cursor = mydb.cursor()
        cursor.execute(f"""
            INSERT INTO users(user_name, number, password, name)
            VALUES(%s, %s, %s, %s)
        """, (user_name, telefon, parol, ism))
        mydb.commit()
        cursor.close()
        mydb.close()

    def line_style(self, ln):
        ln.setStyleSheet("""
            font-family: 'Comic Sans MS';
            color: white;
            background-color: #0099ff; 
            border: none;
            font-size: 40px;
            border-radius: 20px;
        """)
    