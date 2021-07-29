import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QTimer


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setGeometry(50, 50, 400, 300)
    widget.setStyleSheet("background:blue")
    widget.setWindowTitle("Color Visualizer")
    widget.show()

    colors = ["blue", "red", "green"]

    def update_background():
        widget.setStyleSheet(f"background:{random.choice(colors)}")

    timer = QTimer()
    timer.timeout.connect(update_background)
    timer.start(2*100)

    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
