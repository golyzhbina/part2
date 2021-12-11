import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from math import sin, pi, cos
from PyQt5.QtWidgets import QColorDialog


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

        self.flag = False
        self.button_show = QPushButton(self)
        self.button_show.move(290, 16)
        self.button_show.setText("Показать")
        self.button_show.clicked.connect(self.color)

        self.coord_x = lambda x: 250 + x
        self.coord_y = lambda y: 250 - y

        self.side = 150

    def color(self):
        self.color = QColorDialog.getColor()
        self.flag = True


    def paintEvent(self, event):

        if self.line_coef.toPlainText() == "" or self.line_n.toPlainText() == "" or self.line_m.toPlainText() == "" or not self.flag:
            return

        else:
            self.k = float(self.line_coef.toPlainText())
            self.n = int(self.line_n.toPlainText())
            self.m = int(self.line_m.toPlainText())

        qt_paint = QPainter()
        qt_paint.begin(self)
        self.coord_figure(qt_paint)
        qt_paint.end()

    def figure(self):

        self.a = 2 * pi / self.m
        a0 = 0
        r = []
        for i in range(int(self.line_m.toPlainText())):
            ri = (int(round(self.side * cos(a0), 0)), round(self.side * sin(a0), 0))
            a0 += self.a
            r.append(ri)

        return r

    def new_coord(self, ri):
        return [round(ri[0] + self.k * (ri[2] - ri[0]), 0), round(ri[1] + self.k * (ri[3] - ri[1]), 0)]

    def coord_figure(self, qp):
        r = self.figure()
        pen = QPen(self.color)
        qp.setPen(pen)

        for j in range(self.n):
            for i in range(len(r) - 1):
                coords = [self.coord_x(r[i][0]), self.coord_y(r[i][1]),
                          self.coord_x(r[i + 1][0]), self.coord_y(r[i+1][1])]
                qp.drawLine(*coords)

            coords = [self.coord_x(r[0][0]), self.coord_y(r[0][1]), self.coord_x(r[-1][0]), self.coord_y(r[-1][1])]
            qp.drawLine(*coords)

            new_r = []
            for i in range(-1, len(r) - 1):
                r1 = r[i]
                r2 = r[i + 1]
                ri = r1 + r2
                new_r.append(self.new_coord(ri))

            r = new_r

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)
window = Widget2()
window.show()
sys.exit(app.exec())