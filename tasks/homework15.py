import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from math import sin, pi, cos, acos, asin


class Widget2(QWidget):

    def __init__(self):

        super(Widget2, self).__init__()

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Квадрат-объектив 3")

        self.label_coef = QLabel(self)
        self.label_coef.move(20, 20)
        self.label_coef.setText("Coef:")
        self.label_coef.sizeHint()

        self.line_coef = QTextEdit(self)
        self.line_coef.setGeometry(50, 16, 50, 20)

        self.label_n = QLabel(self)
        self.label_n.move(120, 20)
        self.label_n.setText("N:")
        self.label_n.sizeHint()

        self.line_n = QTextEdit(self)
        self.line_n.setGeometry(135, 16, 50, 20)

        self.label_m = QLabel(self)
        self.label_m.move(210, 20)
        self.label_m.setText("M:")
        self.label_m.sizeHint()

        self.line_m = QTextEdit(self)
        self.line_m.setGeometry(225, 16, 50, 20)

        self.button_show = QPushButton(self)
        self.button_show.move(290, 16)
        self.button_show.setText("Показать")
        self.button_show.clicked.connect(self.update)

        self.coord_x = lambda x: 250 + x
        self.coord_y = lambda y: 250 - y

        self.side = 100
        self.a = None

    def paintEvent(self, event):

        if self.line_coef.toPlainText() == "" \
                or self.line_n.toPlainText() == "" \
                or self.line_m.toPlainText() == "":
            return

        qt_paint = QPainter()

        qt_paint.begin(self)
        self.draw_square(qt_paint)
        qt_paint.end()

    def draw_square(self, qp):

        m = int(self.line_m.toPlainText())
        n = int(self.line_n.toPlainText())
        coef = float(self.line_coef.toPlainText())

        x = ((coef * self.side) ** 2 + self.side ** 2 * (1 - coef) ** 2 -
             2 * coef * self.side ** 2 * (1 - coef) * cos(pi * (m - 2) / m)) ** 0.5
        self.a = pi / 10
        if m == 6:
            self.a = pi / 13
        elif m == 8:
            self.a = pi / 7
        elif m == 10:
            self.a = pi / 10
        elif m == 12:
            self.a = pi / 12

        lst_side = list(map(lambda i: coef ** i * self.side * (1.5 ** 0.5), range(n)))
        lst_r_vec = list(map(lambda s: s * coef ** lst_side.index(s), lst_side))

        for j in range(n):
            nodes = [(lst_side[j] * cos(i * 2 * pi / m) * cos(self.a * j)
                      - sin(self.a * j) * lst_side[j] * sin(i * 2 * pi / m),
                      lst_side[j] * cos(i * 2 * pi / m) * sin(self.a * j)
                      + lst_side[j] * sin(i * 2 * pi / m) * cos(self.a * j)) for i in range(m)]
            nodes2 = [(self.coord_x(node[0]), self.coord_y(node[1])) for node in nodes]

            pen = QPen(QColor(81, 192, 15), 3)
            qp.setPen(pen)
            for i in range(-1, len(nodes2) - 1):
                qp.drawLine(*nodes2[i], *nodes2[i + 1])

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)
window = Widget2()
window.show()
sys.exit(app.exec())