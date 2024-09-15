from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QPixmap

class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qirg'i")
        self.setFixedSize(1920, 1000)

      
        self.background_pixmap = QPixmap("1.png")

        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setGeometry(600, 900, 700, 20)
        
      
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #bbb;
                border-radius: 10px;
                background: #eee;
                text-align: center;
            }
            QProgressBar::chunk {
                background: #F4C542; 
                width: 20px;
                margin: 1.5px;
            }
        """)

       
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(5900)

    def update_progress(self):
        self.hide()

    def paintEvent(self, event):
        painter = QPainter(self)
        scaled_pixmap = self.background_pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        painter.drawPixmap(self.rect(), scaled_pixmap)

app = QApplication([])

window = MyWin()
window.show()

app.exec_()
