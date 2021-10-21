from PyQt5.QtWidgets import QMainWindow, QTextEdit, QPushButton, QApplication
from random import choice
import sys


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.setGeometry(500, 300, 500, 60)
        self.setWindowTitle("Случайная строка")

        self.pushbutton_get = QPushButton(self)
        self.pushbutton_get.setGeometry(20, 20, 70, 30)
        self.pushbutton_get.setText("Получить")
        self.pushbutton_get.clicked.connect(self.get)

        self.out_line = QTextEdit(self)
        self.out_line.setGeometry(100, 20, 390, 30)
        self.out_line.setReadOnly(True)

    def get(self):

        self.out_line.clear()

        with open("input.txt", "r", encoding="utf-8") as out_file:

            string = choice(out_file.readlines()).strip()

        self.out_line.setText(string)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())
