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
        main_lbl.setStyleSheet("font-size:50px;font-family: 'Comic Sans MS';")
        main_lbl.setAlignment(Qt.AlignCenter)
        self.scs_lbl = QLabel("")
        self.scs_lbl.setStyleSheet("font-size:30px;font-family: 'Comic Sans MS';color:black")
        self.space_lbl = QLabel()
        self.space_lbl.setFixedHeight(30)
        self.ln_user_name = QLineEdit()
        self.ln_user_name.setFixedSize(600, 100)
        self.ln_user_name.setPlaceholderText("User name tanlang")
        self.ln_ism_edit = QLineEdit()
        self.ln_ism_edit.setFixedSize(600, 100)
        self.ln_ism_edit.setPlaceholderText("Ismingizni kiriting")
        self.ln_phone_edit = QLineEdit()
        self.ln_phone_edit.setFixedSize(600, 100)
        self.ln_phone_edit.setPlaceholderText("Telefon raqamingizni kiriting (+998 ...)")
        self.ln_password_edit = QLineEdit()
        self.ln_password_edit.setFixedSize(600, 100)
        self.ln_password_edit.setPlaceholderText("Parolingizni kiriting")

        self.line_style(self.ln_user_name)
        self.line_style(self.ln_ism_edit)
        self.line_style(self.ln_phone_edit)
        self.line_style(self.ln_password_edit)

        self.ok_btn = QPushButton("OK", clicked=self.connetor)
        self.ext_btn = QPushButton("Exit")
        self.line_style(self.ok_btn)
        self.line_style(self.ext_btn)

        self.ok_btn.setFixedSize(200, 50)
        self.ext_btn.setFixedSize(200, 50)
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
        v_main_layout.addWidget(self.scs_lbl)
        h_btn.addWidget(self.ok_btn)
        h_btn.addWidget(self.ext_btn)
        v_main_layout.addStretch()
        v_main_layout.addLayout(h_btn)
        v_main_layout.addWidget(self.space_lbl)
        self.setLayout(v_main_layout)

    def connetor(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2024072311",
            database="blog_post"
        )
        user_name = self.ln_user_name.text().strip()
        ism = self.ln_ism_edit.text().strip()
        telefon = self.ln_phone_edit.text().strip()
        parol = self.ln_password_edit.text().strip()


        telefon_operator = [90, 91, 88, 99, 93, 94]

        if not user_name or not ism or not telefon or not parol:
            self.scs_lbl.setText("Iltimos, barcha maydonlarni to'ldiring!")
            self.scs_lbl.adjustSize()
            return

        if not self.is_valid_phone_number(telefon):
            self.scs_lbl.setText("Telefon raqami noto'g'ri formatda!")
            self.scs_lbl.adjustSize()
            return

        operator_code = self.get_operator_code(telefon)

        if operator_code is None:
            self.scs_lbl.setText("Telefon raqami noto'g'ri formatda!")
            self.scs_lbl.adjustSize()
            return
        cursor = mydb.cursor()

 
        cursor.execute("SELECT * FROM users WHERE number = %s OR user_name = %s", (telefon, user_name))
        myresult = cursor.fetchall()

        if myresult:
            for i in myresult:
                if telefon == i[1]:
                    self.scs_lbl.setText("Bu telefon raqam bilan ro'yxatdan o'tilgan")
                    self.scs_lbl.adjustSize()
                elif user_name == i[0]:
                    self.scs_lbl.setText("Bu username olingan")
                    self.scs_lbl.adjustSize()
            self.clear_inputs()
        else:
            if operator_code in telefon_operator:
                cursor.execute("""
                    INSERT INTO users(user_name, number, password, name)
                    VALUES(%s, %s, %s, %s)
                """, (user_name, telefon, parol, ism))
                mydb.commit()
                self.scs_lbl.setText("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")
                self.scs_lbl.adjustSize()
            else:
                self.scs_lbl.setText("Telefon raqamining operator kodi noto'g'ri!")
                self.scs_lbl.adjustSize()

            self.clear_inputs()

        cursor.close()
        mydb.close()

    def get_operator_code(self, telefon):
       
        if telefon.startswith('+998') and len(telefon) == 13: 
            try:
                operator_code = int(telefon[4:6]) 
                print(operator_code) 
                return operator_code
            except ValueError:
                return None
        return None

    def is_valid_phone_number(self, telefon):
        if telefon.startswith('+998') and len(telefon) == 13 and telefon[1:].isdigit():
            return True
        else:
            self.ln_phone_edit.clear()
            return False

    def clear_inputs(self):
        self.ln_user_name.clear()
        self.ln_ism_edit.clear()
        self.ln_phone_edit.clear()
        self.ln_password_edit.clear()

    def line_style(self, ln):
        ln.setStyleSheet("""
            font-family: 'Comic Sans MS';
            color: white;
            background-color: #0099ff; 
            border: none;
            font-size: 30px;
            border-radius: 20px;
        """)