from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect


class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x4988D1
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x498BD1
        self.enable_shadow = True

        self.resize(self.width, self.height)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = int(self.progress_width / 2)
        value = (self.value * 360) / self.max_value

        paint = QtGui.QPainter()
        paint.begin(self)
        paint.setRenderHint(QtGui.QPainter.Antialiasing)
        paint.setFont(QtGui.QFont(self.font_family, self.font_size))

        rect = QtCore.QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, int(-value * 16))

        pen.setColor(QtGui.QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        paint.end()

    def set_value(self, value: int):
        self.value = value

    def add_shadow(self, enable):
        if enable:
            self.shadow.setBlurRadius(5)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)
