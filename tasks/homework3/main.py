import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QTextEdit, QMainWindow
from calc_py import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def initMW(self):
        self.number_1.setText("0")
        self.number_2.setText("0")
        self.result.setReadOnly(True)

        self.add.clicked.connect(self.operation)
        self.differnt.clicked.connect(self.operation)
        self.multiplicate.clicked.connect(self.operation)
        self.division.clicked.connect(self.operation)

        self.chars = {"+": lambda n1, n2: n1 + n2,
                        "-": lambda n1, n2: n1 - n2,
                        "*": lambda n1, n2: n1 * n2,
                        ":": lambda n1, n2: n1 / n2}

    def operation(self):
        sender = self.sender().text()
        result = self.chars[sender](int(self.number_1.text()), int(self.number_1.text()))
        self.result.setText(str(result))


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = MainWindow()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
