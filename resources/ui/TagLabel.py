from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class Tag(QLabel):
    def __init__(self, size):
        super().__init__()
        self.setProperty('class', 'tag')
        self.size = size
        font = QFont()
        font.setPointSize(self.size)
        self.setFont(font)

    def setText(self, text: str) -> None:
        super().setText(text)
        self.height = self.size + 10
        self.width = len(text) * self.size + 7
        self.setFixedSize(self.width, self.height)
