from PyQt5.QtGui import QPainter, QPainterPath, QPixmap, QPen, QColor
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class CircleImage(QLabel):
    def __init__(self, parent, x, y, width, height):
        super().__init__(parent)
        self.resize(width, height)
        self.circleImage = None
        self.x = x
        self.y = y

    def setImage(self, image):
        self.circleImage = QPixmap(image)
        pixmap = QPixmap(self.width(), self.height())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.begin(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform, True)
        path = QPainterPath()
        path.addEllipse(self.x, self.y, self.x + self.width(), self.y + self.height())
        painter.setClipPath(path)
        painter.drawPixmap(self.x, self.y, self.x + self.width(), self.y + self.height(), self.circleImage)
        painter.setPen(QPen(QColor('#ffc107'), 4))
        painter.drawEllipse(self.x, self.y, self.x + self.width(), self.y + self.height())
        painter.end()
        self.setPixmap(pixmap)


