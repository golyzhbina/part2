from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
import sys
from os import listdir


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.setGeometry(400, 200, 300, 300)
        self.setWindowTitle("Файловая статистика")

        self.label_filename = QLabel(self)
        self.label_filename.setText("Имя файла:")
        self.label_filename.setGeometry(10, 10, 65, 30)

        self.label_maxvalue = QLabel(self)
        self.label_maxvalue.setText("Максимальное значение:")
        self.label_maxvalue.setGeometry(10, 50, 150, 30)

        self.label_maxvalue = QLabel(self)
        self.label_maxvalue.setText("Минимальное значение:")
        self.label_maxvalue.setGeometry(10, 90, 150, 30)

        self.label_maxvalue = QLabel(self)
        self.label_maxvalue.setText("Среднее значение:")
        self.label_maxvalue.setGeometry(10, 130, 150, 30)

        self.line_filename = QLineEdit(self)
        self.line_filename.setGeometry(75, 10, 130, 30)

        self.line_maxvalue = QLineEdit(self)
        self.line_maxvalue.setGeometry(160, 50, 125, 30)

        self.line_minvalue = QLineEdit(self)
        self.line_minvalue.setGeometry(160, 90, 125, 30)

        self.line_mean = QLineEdit(self)
        self.line_mean.setGeometry(160, 130, 125, 30)

        self.pushbutton_calc = QPushButton(self)
        self.pushbutton_calc.setGeometry(215, 10, 70, 30)
        self.pushbutton_calc.setText("Рассчитать")
        self.pushbutton_calc.clicked.connect(self.calc)

        self.label_satisfy_file = QLabel(self)
        self.label_satisfy_file.move(10, 260)

        self.lst_name = listdir(r"C:\Users\Lenovo\PycharmProject\part2\tasks\task_10")
        self.lst_name.sort()

    def calc(self):

        file_name = self.line_filename.text()

        if file_name in self.lst_name:

            with open(file_name, "r", encoding="utf-8") as out_file:
                numbers = list(map(lambda x: x.replace('\t', " ").replace('\n', " ").split(" "), out_file.readlines()))
                numbers = [list(filter(lambda x: x != "", numbers[i])) for i in range(len(numbers))]

            try:
                numbers = [list(map(int, numbers[i])) for i in range(len(numbers))]
            except ValueError:
                self.label_satisfy_file.setText(f"Неверный формат данных")
                self.label_satisfy_file.resize(100, 30)
            else:

                self.line_maxvalue.setText(str(max(map(max, numbers))))
                self.line_minvalue.setText(str(min(map(min, numbers))))
                self.line_mean.setText(str(sum(map(sum, numbers)) / len(numbers)))

        else:
            self.label_satisfy_file.setText(f"Файл не найден {file_name}")
            self.label_satisfy_file.sizeHint()

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())
