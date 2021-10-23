import sys
from pickle import load, dump
from os import listdir
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QTextEdit


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(500, 200, 400, 350)

        self.label_filename = QLabel(self)
        self.label_filename.setGeometry(20, 20, 60, 30)
        self.label_filename.setText("Имя файла:")

        self.line_filename = QLineEdit(self)
        self.line_filename.setGeometry(90, 20, 300, 25)

        self.pushbutton_create = QPushButton(self)
        self.pushbutton_create.setGeometry(20, 55, 100, 25)
        self.pushbutton_create.setText("Создать файл")
        self.pushbutton_create.clicked.connect(self.create_file)

        self.pushbutton_save = QPushButton(self)
        self.pushbutton_save.setGeometry(20, 90, 100, 25)
        self.pushbutton_save.setText("Сохранить файл")
        self.pushbutton_save.clicked.connect(self.save_file)

        self.pushbutton_open = QPushButton(self)
        self.pushbutton_open.setGeometry(20, 125, 100, 25)
        self.pushbutton_open.setText("Открыть файл")
        self.pushbutton_open.clicked.connect(self.open_file)

        self.list = QTextEdit(self)
        self.list.setGeometry(130, 55, 260, 235)

        self.label_satisfy_file = QLabel(self)
        self.label_satisfy_file.move(20, 300)

        self.files_names = listdir(r"C:\Users\Lenovo\PycharmProject\part2\tasks\task_12")

    def create_file(self):

        self.list.clear()
        filename = self.line_filename.text()

        if filename in self.files_names:

            self.label_satisfy_file.resize(150, 30)
            self.label_satisfy_file.setText("Такое имя уже существует")

        else:
            with open(filename, "wb") as input_file:
                dump(self.list.toPlainText(), input_file)
                self.files_names.append(filename)

            self.label_satisfy_file.resize(150, 30)
            self.label_satisfy_file.setText("Файл успешно создан")

    def save_file(self):

        filename = self.line_filename.text()

        with open(filename, "wb") as input_file:
            dump(self.list.toPlainText(), input_file)

        self.label_satisfy_file.resize(150, 30)
        self.label_satisfy_file.setText("Файл успешно сохранен")

    def open_file(self):

        filename = self.line_filename.text()

        if filename in self.files_names:
            try:
                with open(filename, "rb") as out_file:
                    text = load(out_file)
            except EOFError:
                pass
            else:
                self.list.setText(text)

        else:
            self.label_satisfy_file.resize(150, 30)
            self.label_satisfy_file.setText("Файл не найден")


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())