import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen


class Widget(QWidget):

    def __init__(self):

        super(Widget, self).__init__()

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Квадрат-объектив 1")

        self.label_sizeSide = QLabel(self)
        self.label_sizeSide.move(30, 20)
        self.label_sizeSide.setText("Side:")
        self.label_sizeSide.sizeHint()

        self.line_size_side = QTextEdit(self)
        self.line_size_side.setGeometry(60, 16, 50, 20)

        self.label_coef = QLabel(self)
        self.label_coef.move(130, 20)
        self.label_coef.setText("Coef:")
        self.label_coef.sizeHint()

        self.line_coef = QTextEdit(self)
        self.line_coef.setGeometry(160, 16, 50, 20)

        self.label_n = QLabel(self)
        self.label_n.move(230, 20)
        self.label_n.setText("N:")
        self.label_n.sizeHint()

        self.line_n = QTextEdit(self)
        self.line_n.setGeometry(245, 16, 50, 20)

        self.button_show = QPushButton(self)
        self.button_show.move(310, 16)
        self.button_show.setText("Показать")
        self.button_show.clicked.connect(self.update)

        self.coord_x = lambda x: 250 + x
        self.coord_y = lambda y: 250 - y
        self.coords = lambda side: [[self.coord_x(-side), self.coord_y(side), self.coord_x(side), self.coord_y(side)],
                       [self.coord_x(side), self.coord_y(side), self.coord_x(side), self.coord_y(-side)],
                       [self.coord_x(side), self.coord_y(-side), self.coord_x(-side), self.coord_y(-side)],
                       [self.coord_x(-side), self.coord_y(-side), self.coord_x(-side), self.coord_y(side)]]

    def paintEvent(self, event):

        if self.line_size_side.toPlainText() == "" \
                or self.line_coef.toPlainText() == "" \
                or self.line_n.toPlainText() == "":
            return

        qt_paint = QPainter()

        qt_paint.begin(self)
        self.draw_square(qt_paint)
        qt_paint.end()

    def draw_square(self, qp):

        n = int(self.line_n.toPlainText())
        side = int(self.line_size_side.toPlainText())
        coef = float(self.line_coef.toPlainText())

        pen = QPen(QColor(151, 81, 132), 3)
        qp.setPen(pen)
        lst_side = list(map(lambda i: coef ** i * side, range(n)))
        for s in lst_side:
            for coord in self.coords(s):
                qp.drawLine(*coord)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)
window = Widget()
window.show()
sys.exit(app.exec())



