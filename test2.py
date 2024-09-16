from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

app = QApplication([])

# Asosiy oynani yaratamiz
window = QWidget()
window.setWindowTitle("Video Player")

# Video oynasi uchun widget yaratamiz
video_widget = QVideoWidget()

# Media player yaratamiz
media_player = QMediaPlayer()
media_player.setVideoOutput(video_widget)

# Play tugmasi yaratamiz
play_button = QPushButton("Play")

# Tugmani bosganda video ijro etiladi
def play_video():
    video_url = QUrl.fromLocalFile("1.mp4")  # Video faylingizning to'g'ri yo'lini kiriting
    media_player.setMedia(QMediaContent(video_url))
    media_player.play()

play_button.clicked.connect(play_video)

# Layout yaratib, elementlarni joylashtiramiz
layout = QVBoxLayout()
layout.addWidget(video_widget)
layout.addWidget(play_button)

window.setLayout(layout)
window.show()

app.exec_()