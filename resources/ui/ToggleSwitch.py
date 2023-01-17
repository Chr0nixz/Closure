from PyQt5.QtCore import Qt, QRectF, QRect, QTimer, pyqtSignal
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QFont
from PyQt5.QtWidgets import QWidget


class SliderButton(QWidget):
    # 信号
    checkedChanged = pyqtSignal(bool)

    def __init__(self, parent=None, checked=False, text=False, size=(40, 20)):
        super(QWidget, self).__init__(parent)

        self.checked = checked
        self.bgColorOff = QColor(255, 255, 255)
        self.bgColorOn = QColor(255, 193, 7)

        self.sliderColorOff = QColor(100, 100, 100)
        self.sliderColorOn = QColor(255, 255, 255)

        self.textColorOff = QColor(143, 143, 143)
        self.textColorOn = QColor(255, 255, 255)

        self.text = text
        self.textOff = "OFF"
        self.textOn = "ON"

        self.space = 2
        self.rectRadius = 5

        self.setMaximumSize(size[0], size[1])
        self.step = self.width() / 40
        if checked:
            self.startX = self.width() - self.height()
            self.endX = self.width() - self.height()
        else:
            self.startX = 0
            self.endX = 0

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.updateValue)  # 计时结束调用operate()方法

        self.setFont(QFont("Microsoft Yahei", 10))

    def updateValue(self):
        if self.checked:
            if self.startX < self.endX:
                self.startX = self.startX + self.step
            else:
                self.startX = self.endX
                self.timer.stop()
        else:
            if self.startX > self.endX:
                self.startX = self.startX - self.step
            else:
                self.startX = self.endX
                self.timer.stop()

        self.update()

    def mousePressEvent(self, event):
        self.checked = not self.checked
        # 发射信号
        self.checkedChanged.emit(self.checked)

        # 每次移动的步长为宽度的40分之一
        self.step = self.width() / 40
        # 状态切换改变后自动计算终点坐标
        if self.checked:
            self.endX = self.width() - self.height()
        else:
            self.endX = 0
        self.timer.start(5)

    def paintEvent(self, evt):
        # 绘制准备工作, 启用反锯齿
        painter = QPainter()

        painter.begin(self)

        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制背景
        self.drawBg(evt, painter)
        # 绘制滑块
        self.drawSlider(evt, painter)
        if self.text:
            # 绘制文字
            self.drawText(evt, painter)

        painter.end()

    def drawText(self, event, painter):
        painter.save()

        if self.checked:
            painter.setPen(self.textColorOn)
            painter.drawText(0, 0, int(self.width() / 2 + self.space * 2), int(self.height()), Qt.AlignCenter,
                             self.textOn)
        else:
            painter.setPen(self.textColorOff)
            painter.drawText(int(self.width() / 2), 0, int(self.width() / 2 - self.space), int(self.height()),
                             Qt.AlignCenter, self.textOff)

        painter.restore()

    def drawBg(self, event, painter):
        painter.save()
        painter.setPen(Qt.NoPen)

        if self.checked:
            painter.setBrush(self.bgColorOn)
        else:
            painter.setBrush(self.bgColorOff)

        rect = QRect(0, 0, self.width(), self.height())
        # 半径为高度的一半
        radius = rect.height() / 2
        # 圆的宽度为高度
        circleWidth = rect.height()

        path = QPainterPath()
        path.moveTo(radius, rect.left())
        path.arcTo(QRectF(rect.left(), rect.top(), circleWidth, circleWidth), 90, 180)
        path.lineTo(rect.width() - radius, rect.height())
        path.arcTo(QRectF(rect.width() - rect.height(), rect.top(), circleWidth, circleWidth), 270, 180)
        path.lineTo(radius, rect.top())

        painter.drawPath(path)
        painter.restore()

    def drawSlider(self, event, painter):
        painter.save()

        if self.checked:
            painter.setBrush(self.sliderColorOn)
        else:
            painter.setBrush(self.sliderColorOff)

        rect = QRect(0, 0, self.width(), self.height())
        sliderWidth = rect.height() - self.space * 2
        sliderRect = QRect(int(self.startX + self.space), int(self.space), int(sliderWidth), int(sliderWidth))
        painter.drawEllipse(sliderRect)

        painter.restore()
