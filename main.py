from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from tizm_kirish import Tizm
from register import MyWindow
from color_back import GradientWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QSequentialAnimationGroup

class MyWindow1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1700, 900)
       
        self.stacked_widget = QStackedWidget()
        self.main_page_widget = QWidget()
        self.module1 = None  
        self.main()
        self.register()
        self.setup_ui()
        self.setup_animation()

    def main(self):
        self.gradient_widget = GradientWidget(self)
        self.gradient_widget.setGeometry(0, 0, 0, 0)
        self.gradient_widget.setStyleSheet("background: transparent;")
        v_main_layout = QVBoxLayout()
        h_main_text = QHBoxLayout()
        self.main_lbl = QLabel("Bosh sahifa")
        self.pic_label = QLabel(self)
        self.pic_label.setFixedSize(300, 300)
        self.pic_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("write_logo.png")
        self.pic_label.setPixmap(pixmap)
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pic_label.setPixmap(scaled_pixmap)
        self.pic_label.setStyleSheet("background: transparent;")
        self.main_lbl.setAlignment(Qt.AlignCenter)
        self.main_lbl.setStyleSheet("""
            font-family: 'Comic Sans MS';
            font-size: 50px;
            font-weight: bold;
            color: white;
        """)
        btn_login = QPushButton("Hisobga kirish", clicked=self.login)
        btn_login.setFixedSize(600, 100)

        btn_register = QPushButton("Ro'yxatdan o'tish", clicked=self.register_page_switch)
        btn_register.setFixedSize(600, 100)
        h_main_text.addWidget(self.main_lbl)
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
        self.main_page_widget.setLayout(v_main_layout)

    def register(self):
        self.module1 = MyWindow()
        self.stacked_widget.addWidget(self.module1) 

    def setup_ui(self):
        self.stacked_widget.addWidget(self.main_page_widget)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.stacked_widget)
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
            background-color: #0099ff;
            border: none;
            font-size: 40px;
            border-radius: 10px;
        """)

    def login(self):
        self.log = Tizm()
        self.log.show()

    def register_page_switch(self):
        self.register()
        self.stacked_widget.setCurrentWidget(self.module1)
    
    def setup_animation(self):
   
        self.animation = QPropertyAnimation(self.pic_label, b"geometry")
        self.animation2 = QPropertyAnimation(self.main_lbl, b"geometry")
        
        self.animation_group = QSequentialAnimationGroup()

        self.animation.setDuration(4000)  
        self.animation.setStartValue(QRect(350, 50, 300, 300))  
        self.animation.setEndValue(QRect(850, 50, 100, 100))  
        self.animation.setLoopCount(1) 

        self.animation2.setDuration(4000) 
        self.animation2.setStartValue(QRect(50, 170, 300, 100)) 
        self.animation2.setEndValue(QRect(500, 50, 300, 100))
        self.animation2.setLoopCount(1)  
        
        self.animation_group.addAnimation(self.animation)
        self.animation_group.addAnimation(self.animation2)

        self.animation_group.start()

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow1()
    win.show()
    app.exec_()
