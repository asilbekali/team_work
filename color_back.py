from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QListWidget
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import QLinearGradient, QBrush, QColor, QPalette, QPainter
from color_back import *

class GradientWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(1700, 900)
        self.original_color = QColor("brown")
        self.target_color = QColor("white")
        self.gradient = QLinearGradient(0, 0, 0, self.height())
        self.gradient.setColorAt(0.0, QColor("#6a0dad"))
        self.gradient.setColorAt(0.33, QColor("#1e90ff"))
        self.gradient.setColorAt(0.66, QColor("#87ceeb"))
        self.gradient.setColorAt(1.0, QColor("white"))

    def set_gradient(self, start_color, end_color):
        self.gradient.setColorAt(0, start_color)
        self.gradient.setColorAt(1, end_color)
        self.update()  

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(self.gradient))
        painter.drawRect(self.rect())

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 700)

    
        self.main_layout = QVBoxLayout(self)
        
   
        self.gradient_widget = GradientWidget(self)
        self.gradient_widget.setGeometry(0, 0, 400, 700)  
        self.gradient_widget.setStyleSheet("background: transparent;")

  
        self.slide = QWidget(self)
        self.slide.setGeometry(0, 0, 200, 700) 
        self.slide.setStyleSheet("background-color: lightgray;")
        self.slide.hide()  
        
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
