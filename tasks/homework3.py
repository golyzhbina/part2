from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QMainWindow, QLabel
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.MWinit()

    def MWinit(self):

        self.setGeometry(500, 300, 370, 70)
        self.setWindowTitle("Арифмометр")

        self.line_left = QTextEdit(self)
        self.line_left.setGeometry(10, 10, 60, 50)

        self.line_right = QTextEdit(self)
        self.line_right.setGeometry(228, 10, 60, 50)

        self.equal_sign = QLabel(self)
        self.equal_sign.setText("=")
        self.equal_sign.setGeometry(290, 30, 10, 10)

        self.result = QTextEdit(self)
        self.result.setGeometry(300, 10, 60, 50)
        self.result.setReadOnly(True)

        self.multiplicate = QPushButton(self)
        self.multiplicate.setGeometry(72, 10, 50, 50)
        self.multiplicate.setText("*")
        self.multiplicate.clicked.connect(self.operation)

        self.add = QPushButton(self)
        self.add.setGeometry(124, 10, 50, 50)
        self.add.setText("+")
        self.add.clicked.connect(self.operation)

        self.difference = QPushButton(self)
        self.difference.setGeometry(176, 10, 50, 50)
        self.difference.setText("-")
        self.difference.clicked.connect(self.operation)

        self.chars = {"+": lambda n1, n2: n1 + n2,
                  "-": lambda n1, n2: n1 - n2,
                  "*": lambda n1, n2: n1 * n2,
                  ":": lambda n1, n2: n1 / n2}

    def operation(self):
        sender = self.sender().text()
        a, b = self.line_left.toPlainText(), self.line_right.toPlainText()
        if len(a) == 0:
            a = 0
        if len(b) == 0:
            b = 0
        a, b = int(a), int(b)
        result = self.operations[sender](a, b)
        self.result.setText(str(result))

app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())
