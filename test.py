from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from tizm_kirish import Tizm
from register import MyWindow
from color_back import *
from PyQt5.QtGui import *

class MyWindow1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1700, 900)
        self.stacked_widget = QStackedWidget()
        self.main_page_widget = QWidget()
        self.register_page = MyWindow()
        self.init_ui()

    def init_ui(self):
        # Bosh sahifa dizayni
        self.gradient_widget = GradientWidget(self)
        self.gradient_widget.setGeometry(0, 0, 1700, 900)
        self.gradient_widget.setStyleSheet("background: transparent;")

        v_main_layout = QVBoxLayout()
        h_main_text = QHBoxLayout()
        main_lbl = QLabel("Bosh sahifa")
        self.pic_label = QLabel(self)
        self.pic_label.setFixedSize(300, 300)
        self.pic_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("write_logo.png")
        self.pic_label.setPixmap(pixmap)
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pic_label.setPixmap(scaled_pixmap)
        self.pic_label.setStyleSheet("background: transparent;")
        main_lbl.setAlignment(Qt.AlignCenter)
        main_lbl.setStyleSheet("""
            font-family: 'Comic Sans MS';
            font-size: 50px;
            font-weight: bold;
            color: white;
        """)
        btn_login = QPushButton("Hisobga kirish", clicked=self.login)
        btn_login.setFixedSize(600, 100)
        btn_register = QPushButton("Ro'yxatdan o'tish", clicked=self.register)
        btn_register.setFixedSize(600, 100)
        h_main_text.addWidget(main_lbl)
        self.button_style(btn_login)
        self.button_style(btn_register)

        h_main_text.addWidget(self.pic_label)
        h_main_text.addStretch()

        v_main_layout.addStretch()
        v_main_layout.addLayout(h_main_text)
        v_main_layout.addStretch()
        v_main_layout.addWidget(btn_login, alignment=Qt.AlignCenter)
        v_main_layout.addWidget(btn_register, alignment=Qt.AlignCenter)
        v_main_layout.addStretch()

        h_main_layout = QHBoxLayout()
        h_main_layout.addStretch()
        h_main_layout.addLayout(v_main_layout)
        h_main_layout.addStretch()

        self.stacked_widget.addWidget(self.main_page_widget)
        self.stacked_widget.addWidget(self.register_page)

        self.setLayout(h_main_layout)
        self.stacked_widget.setCurrentWidget(self.main_page_widget)

    def resizeEvent(self, event):
        pixmap = self.pic_label.pixmap()
        if pixmap:
            scaled_pixmap = pixmap.scaled(self.pic_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.pic_label.setPixmap(scaled_pixmap)
        super().resizeEvent(event)

    def button_style(self, btn):
        btn.setStyleSheet("""
            font-family: 'Comic Sans MS';
            color: white;
            background-color: #0099ff; /* Asosiy rang */
            border: none;
            font-size: 40px;
            border-radius: 10px;
        """)

    def login(self):
        self.log = Tizm()
        self.log.show()

    def register(self):
        self.stacked_widget.setCurrentWidget(self.register_page)
if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow1()
    win.show()
    app.exec_()
