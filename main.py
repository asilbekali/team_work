from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation, QSequentialAnimationGroup
from PyQt5.QtGui import *
from tizm_kirish import Tizm
from color_back import GradientWidget
import mysql.connector

class MyWindow1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1700, 900)
        self.stacked_widget = QStackedWidget()
        self.main_page_widget = QWidget()
        self.register_page = QWidget()
        self.stacked_widget.addWidget(self.main_page_widget)
        self.stacked_widget.addWidget(self.register_page)
        self.setup_main_page()
        self.setup_register_page()
        self.setup_animation()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.stacked_widget.addWidget(self.register_page)
        
        self.setLayout(main_layout)
       
    def setup_main_page(self):
        self.gradient_widget = GradientWidget(self)
        self.gradient_widget.setGeometry(0, 0, 0, 0)
        self.gradient_widget.setStyleSheet("background: transparent;")

        v_main_layout = QVBoxLayout()
        h_main_text = QHBoxLayout()
        
        self.main_lbl = QLabel("Bosh sahifa")
        self.main_lbl.setStyleSheet("color:black")
        self.pic_label = QLabel(self)
        self.pic_label.setFixedSize(300, 300)
        self.pic_label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap("write_logo.png")
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pic_label.setPixmap(scaled_pixmap)
        self.pic_label.setStyleSheet("background: transparent;")
        
        self.main_lbl.setAlignment(Qt.AlignCenter)
        self.main_lbl.setStyleSheet("""
            font-family: 'Comic Sans MS';
            font-size: 50px;
            font-weight: bold;
            color: black;
        """)

        btn_login = QPushButton("Hisobga kirish", clicked=self.login)
        btn_login.setFixedSize(600, 100)

        btn_register = QPushButton("Ro'yxatdan o'tish", clicked=self.main_page_switch)
        btn_register.setFixedSize(600, 100)
        self.button_style(btn_login)
        self.button_style(btn_register)

        h_main_text.addWidget(self.main_lbl)
        h_main_text.addWidget(self.pic_label)
        h_main_text.addStretch()

        v_main_layout.addStretch()
        v_main_layout.addLayout(h_main_text)
        v_main_layout.addStretch()
        v_main_layout.addWidget(btn_login, alignment=Qt.AlignCenter)
        v_main_layout.addWidget(btn_register, alignment=Qt.AlignCenter)
        v_main_layout.addStretch()
        self.main_page_widget.setLayout(v_main_layout)

    def resizeEvent(self, event):
        """Resize the pixmap to fit the label size."""
        pixmap = self.pic_label.pixmap()
        if pixmap:
            scaled_pixmap = pixmap.scaled(self.pic_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.pic_label.setPixmap(scaled_pixmap)
        super().resizeEvent(event)

    def button_style(self, btn):
        btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn.setStyleSheet(
            """
            QPushButton {
                background-color: white;
                font-size: 40px;
                border-radius: 30px;
                color:#d4af37
            }
            QPushButton:hover {
                background-color: #d4af37;
                font-size: 60px;
                border-radius: 30px;
                color:black
            }
        """
        
            
            
            
       
        )

    def login(self):
        """Show login window."""
        self.log = Tizm()
        self.log.show()

    def setup_animation(self):
        self.animation = QPropertyAnimation(self.pic_label, b"geometry")
        self.animation2 = QPropertyAnimation(self.main_lbl, b"geometry")
        
        self.animation_group = QSequentialAnimationGroup()

        self.animation.setDuration(1000)
        self.animation.setStartValue(QRect(350, 50, 300, 300))
        self.animation.setEndValue(QRect(850, 50, 100, 100))
        self.animation.setLoopCount(1)

        self.animation2.setDuration(1000)
        self.animation2.setStartValue(QRect(50, 170, 300, 100))
        self.animation2.setEndValue(QRect(500, 150, 300, 100))
        self.animation2.setLoopCount(1)
        
        self.animation_group.addAnimation(self.animation)
        self.animation_group.addAnimation(self.animation2)

        self.animation_group.start()

    def setup_register_page(self):
        register_page = QWidget()
        register_layout = QVBoxLayout(register_page)
        
        h_btn = QHBoxLayout()
        main_lbl = QLabel("WORDPAD UCHUN RO'YXATDAN O'TISH")
        main_lbl.setStyleSheet("font-size:50px;font-family: 'Comic Sans MS';color:white")
        main_lbl.setAlignment(Qt.AlignCenter)

        self.scs_lbl = QLabel("")
        self.scs_lbl.setStyleSheet("font-size:30px;font-family: 'Comic Sans MS';color:black")

        self.space_lbl = QLabel()
        self.space_lbl.setFixedHeight(30)

        self.space_lbl2 = QLabel()
        self.space_lbl2.setFixedHeight(15)

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
        self.ext_btn = QPushButton("Exit", clicked=self.exit)
        self.button_style2(self.ok_btn)
        self.button_style2(self.ext_btn)

        self.ok_btn.setFixedSize(200, 50)
        self.ext_btn.setFixedSize(200, 50)

        register_layout.addStretch()
        register_layout.addWidget(main_lbl)
        register_layout.addStretch()

        line_edit_layout = QVBoxLayout()
        line_edit_layout.addWidget(self.ln_user_name)
        line_edit_layout.addWidget(self.space_lbl2)
        line_edit_layout.addWidget(self.ln_ism_edit)
        line_edit_layout.addWidget(self.space_lbl2)

        line_edit_layout.addWidget(self.ln_phone_edit)
        line_edit_layout.addWidget(self.space_lbl2)
        line_edit_layout.addWidget(self.ln_password_edit)
        line_edit_layout.setAlignment(Qt.AlignCenter)

        register_layout.addLayout(line_edit_layout)
        register_layout.addWidget(self.scs_lbl)

        h_btn.addWidget(self.ok_btn)
        h_btn.addWidget(self.ext_btn)
        register_layout.addStretch()
        register_layout.addLayout(h_btn)
        register_layout.addWidget(self.space_lbl)

        self.stacked_widget.addWidget(register_page)
    
    def connetor(self):
        """Ma'lumotlarni ma'lumotlar bazasiga qo'shish."""
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rustamjon1",
            database="blog_orginal"
        )
        user_name = self.ln_user_name.text().strip()
        ism = self.ln_ism_edit.text().strip()
        telefon = self.ln_phone_edit.text().strip()
        parol = self.ln_password_edit.text().strip()

        telefon_operator = [90, 91, 88, 99, 93, 94,95,33,97,98,77]

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
        print(myresult)

        if myresult:
            for i in myresult:
                if telefon == i[2]:
                    self.scs_lbl.setText("Bu telefon raqam bilan ro'yxatdan o'tilgan")
                elif user_name == i[1]:
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
                return operator_code
            except ValueError:
                return None
        return None

    def is_valid_phone_number(self, telefon):

        return telefon.startswith('+998') and len(telefon) == 13 and telefon[1:].isdigit()

    def clear_inputs(self):

        self.ln_user_name.clear()
        self.ln_ism_edit.clear()
        self.ln_phone_edit.clear()
        self.ln_password_edit.clear()

    def line_style(self, ln):
        ln.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ln.setStyleSheet("""
            font-family: 'Comic Sans MS';
            color: white;
            background-color: transparent; 
            border: none;
            font-size: 30px;
            border-radius: 20px;
        """)
    def button_style2(self, btn):
        btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                font-size: 40px;
                border-radius: 30px;
                color:#d4af37
            }
            QPushButton:hover {
                background-color: transparent;
                font-size: 60px;
                border-radius: 30px;
                color:black
            }
        """)
    def main_page_switch(self):
        self.stacked_widget.setCurrentIndex(1)

    def exit(self):
        self.clear_inputs()
        self.scs_lbl.clear()
        self.stacked_widget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow1()
    win.show()
    app.exec_()
