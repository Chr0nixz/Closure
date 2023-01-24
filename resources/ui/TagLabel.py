from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtGui import QFont


class Tag(QLabel):
    def __init__(self, size, parent):
        super().__init__()
        self.sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setSizePolicy(self.sizePolicy)
        parent.addWidget(self)
        self.setProperty('class', 'tag')
        font = QFont()
        font.setPointSize(size)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        print(self.height(), self.width())

    def setText(self, text: str) -> None:
        super().setText(text)
        self.height = self.fontMetrics().height() + 8
        self.width = self.fontMetrics().width(text)
        self.setFixedSize(self.width, self.height)
