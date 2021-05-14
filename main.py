import sys
import os
from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from circular_progress import circular_progress


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.resize(500, 500)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.container = QtWidgets.QFrame()
        self.container.setStyleSheet("background-color: transparent;")
        self.layout = QtWidgets.QVBoxLayout()

        self.progress = circular_progress.CircularProgress()
        self.progress.value = 0
        self.progress.setMinimumSize(self.progress.width, self.progress.height)
        self.progress.add_shadow(True)
        self.slider = QtWidgets.QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self.change_value)
        self.slider.setRange(0, 100)

        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)
        self.layout.addWidget(self.slider, Qt.AlignCenter, Qt.AlignCenter)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.update()
        self.show()

    def change_value(self, value):
        self.progress.set_value(value)
        self.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
