import sys

from PyQt6 import uic
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = True

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x1, y1 = randint(0, 700), randint(0, 700)
        step = randint(10, 300)
        rectangle = QRectF(x1, y1, step, step)
        qp.drawEllipse(rectangle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())