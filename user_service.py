from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from color_back import GradientWidget


class User_service(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200, 900)
        self.move(1200, 100)
        self.color = GradientWidget(self)
        self.color.setGeometry(0, 0, 0, 0)
        self.color.setStyleSheet("background: transperent;")

        self.main_vb = QVBoxLayout()
        self.hb_box_btns = QHBoxLayout()

        self.update_btn = QPushButton("Update User", clicked=self.update_user)
        self.update_btn.setFixedSize(450, 80)
        self.update_btn.setStyleSheet("""
                                            QPushButton {
                                                background-color: #4CAF50; /* Green */
                                                border: none;
                                                color: white;
                                                padding: 10px 25px;
                                                text-align: center;
                                                text-decoration: none;
                                                font-size: 25px;
                                                margin: 4px 2px;
                                                border-radius: 25px;
                                            }
                                            QPushButton:hover {
                                                background-color: #45a049; font-size: 28px;
                                            }
                                        """)

        self.delete_user = QPushButton("Delete User", clicked=self.delete_user_action)
        self.delete_user.setFixedSize(450, 80)
        self.delete_user.setStyleSheet("""
                                            QPushButton {
                                                background-color: #4CAF50; /* Green */
                                                border: none;
                                                color: white;
                                                padding: 10px 25px;
                                                text-align: center;
                                                text-decoration: none;
                                                font-size: 25px;
                                                margin: 4px 2px;
                                                border-radius: 25px;
                                            }
                                            QPushButton:hover {
                                                background-color: #45a049; font-size: 28px;
                                            }
                                        """)

        self.hb_box_btns.addWidget(self.update_btn)
        self.hb_box_btns.addWidget(self.delete_user)

        self.lebl = QLabel("User Service")
        self.lebl.setStyleSheet("font-size: 40px;")

        self.main_vb.addStretch()
        self.main_vb.addWidget(self.lebl, alignment=Qt.AlignCenter)
        self.main_vb.addStretch()
        self.main_vb.addLayout(self.hb_box_btns)

        self.setLayout(self.main_vb)

    def update_user(self):
        self.upd = Update_account()
        self.upd.show()
        self.hide()

    def delete_user_action(self):
        QMessageBox.information(self, "Delete User", "User has been deleted!")

class Update_account(QWidget):
    def __init__(self):
        super().__init__()
        self.color = GradientWidget(self)
        self.color.setGeometry(0, 0, 0, 0)
        self.color.setStyleSheet("background: transperent;")
        self.setFixedSize(1200, 900)
        self.move(1200, 100)
        self.vb_box_main = QVBoxLayout()
        self.hb_box = QHBoxLayout()
        self.back = QHBoxLayout()

        self.line_name_old = QLineEdit()
        self.line_name_old.setPlaceholderText("User name")
        self.line_name_old.setStyleSheet("font-size: 25px; border-radius: 10px;")
        self.line_name = QLineEdit()
        self.line_name.setPlaceholderText("New user name")
        self.line_password = QLineEdit()
        self.line_password.setPlaceholderText("Password")
        self.line_password.setEchoMode(QLineEdit.Password)

        font = QFont("Arial", 25)
        self.line_name.setFont(font)
        self.line_password.setFont(font)

        self.line_password.setFixedSize(555, 60)
        self.line_name.setFixedSize(555, 60)
        self.line_name_old.setFixedSize(555, 60)

        self.btn_ok = QPushButton("Submit")
        self.btn_back = QPushButton("Back", clicked=self.qaytish)
        self.line_name.setStyleSheet("font-size: 25px; border-radius: 10px;")
        self.line_password.setStyleSheet("font-size: 25px; border-radius: 10px;")
        self.btn_ok.setStyleSheet("""
                                            QPushButton {
                                                background-color: #4CAF50; /* Green */
                                                border: none;
                                                color: white;
                                                padding: 10px 25px;
                                                text-align: center;
                                                text-decoration: none;
                                                font-size: 25px;
                                                margin: 4px 2px;
                                                border-radius: 25px;
                                            }
                                            QPushButton:hover {
                                                background-color: #45a049; font-size: 28px;
                                            }
                                        """)

        self.btn_back.setStyleSheet("""
                                                   QPushButton {
                                                       background-color: #4CAF50; /* Green */
                                                       border: none;
                                                       color: white;
                                                       padding: 10px 25px;
                                                       text-align: center;
                                                       text-decoration: none;
                                                       font-size: 25px;
                                                       margin: 4px 2px;
                                                       border-radius: 25px;
                                                   }
                                                   QPushButton:hover {
                                                       background-color: #45a049; font-size: 28px;
                                                   }
                                               """)

        self.btn_ok.setFixedSize(450, 80)
        self.btn_back.setFixedSize(450, 80)
        self.back.addWidget(self.btn_ok)
        self.back.addWidget(self.btn_back)
        self.vb_box_main.addWidget(self.line_name_old, alignment=Qt.AlignCenter)
        self.vb_box_main.addWidget(self.line_name, alignment=Qt.AlignCenter)
        self.vb_box_main.addWidget(self.line_password, alignment=Qt.AlignCenter)
        self.vb_box_main.addLayout(self.hb_box)
        self.vb_box_main.addStretch()
        self.vb_box_main.addStretch()
        self.vb_box_main.addLayout(self.back)
        self.setLayout(self.vb_box_main)

    def qaytish(self):
        self.main = User_service()
        self.main.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication([])
    win = User_service()
    win.show()
    app.exec_()
