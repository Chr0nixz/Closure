from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtGui import QFont


class Tag(QLabel):
    def __init__(self, size):
        super().__init__()
        self.setProperty('class', 'tag')
        self.size = size
        font = QFont()
        font.setPointSize(self.size)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)

    def setText(self, text: str) -> None:
        super().setText(text)
        self.height = self.size + 10
        self.width = len(text) * self.size + 7
        #self.setFixedSize(self.width, self.height)
        #self.sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        #self.setSizePolicy(self.sizePolicy)
