import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from math import sin, pi, cos, acos


class Widget2(QWidget):

    def __init__(self):

        super(Widget2, self).__init__()

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Квадрат-объектив 2")

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

        self.button_show = QPushButton(self)
        self.button_show.move(190, 16)
        self.button_show.setText("Показать")
        self.button_show.clicked.connect(self.update)

        self.coord_x = lambda x: 250 + x
        self.coord_y = lambda y: 250 - y

        self.side = 200
        self.a = None

    def paintEvent(self, event):

        if self.line_coef.toPlainText() == "" \
                or self.line_n.toPlainText() == "":
            return

        qt_paint = QPainter()

        qt_paint.begin(self)
        self.draw_square(qt_paint)
        qt_paint.end()

    def draw_square(self, qp):

        n = int(self.line_n.toPlainText())
        coef = float(self.line_coef.toPlainText())

        self.a = - acos((3 - coef ** 2) / 2 ** 1.5) + pi / 4
        lst_side = list(map(lambda i: coef ** i * self.side, range(n)))
        lst_r_vec = list(map(lambda s: s / 2 ** 0.5, lst_side))
        angels = [lambda i: pi / 4 - self.a * i, lambda i: - pi / 4 - self.a * i,
                  lambda i: 3 * pi / 4 - self.a * i, lambda i: 5 * pi / 4 - self.a * i]
        coords = []

        for k in range(n):
            coord = [[lst_r_vec[k] * cos(angels[0](k)), lst_r_vec[k] * sin(angels[0](k))],
                     [lst_r_vec[k] * cos(angels[1](k)), lst_r_vec[k] * sin(angels[1](k))],
                     [lst_r_vec[k] * cos(angels[2](k)), lst_r_vec[k] * sin(angels[2](k))],
                     [lst_r_vec[k] * cos(angels[3](k)), lst_r_vec[k] * sin(angels[3](k))]]

            coord = list(map(lambda c: [self.coord_x(c[0]), self.coord_y(c[1])], coord))

            coords.append(coord)

        lines = [(0, 1), (0, 2), (2, 3), (3, 1)]
        r, g, b = 151, 81, 132
        for m in range(n):
            d = m - 20 * (m // 20)
            pen = QPen(QColor(r + d * 6 if r + d * 6 < 255 else 254, g,
                              b + d * 3 if b + d * 3 < 255 else 254), 3)
            qp.setPen(pen)
            for j in range(4):
                coord = coords[d][lines[j][0]] + coords[d][lines[j][1]]
                qp.drawLine(*coord)

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)
window = Widget2()
window.show()
sys.exit(app.exec())
