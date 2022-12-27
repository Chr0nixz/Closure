from PyQt5.QtGui import QPainter, QPainterPath, QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QRect


class CircleImage(QLabel):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.resize(width, height)
        self.circleImage = None

    def setImage(self, image):
        self.circleImage = QPixmap(image)
        pixmap = QPixmap(self.width(), self.height())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.begin(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform, True)
        path = QPainterPath()
        path.addEllipse(0, 0, self.width(), self.height())
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, self.width(), self.height(), self.circleImage)
        painter.end()
        self.setPixmap(pixmap)


