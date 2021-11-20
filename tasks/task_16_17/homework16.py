import sys
import csv

from py_file import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.data = None
        self.school_list = None
        self.classes_list = None

        self.load_table('rez.csv')
        self.buttton_result.clicked.connect(self.sort_data)

        self.box_school.addItem("Все")

        for text in sorted(self.school_list, key=lambda n: int(n) if n[0] != 0 else int(n[1:])):
            self.box_school.addItem(text)

        self.box_class.addItem("Все")

        for text in sorted(self.classes_list, key=lambda n: int(n) if n[0] != 0 else int(n[1:])):
            self.box_class.addItem(text)

    def load_table(self, table_name):

        with open(table_name, encoding="utf8") as csvfile:
            reader = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
            title = [reader[0][1], reader[0][7]]
            self.data = reader[1:]
            self.school_list, self.classes_list, data = set(map(lambda x: x[2][12:14], self.data)), \
                                              set(map(lambda x: x[2][15:17], self.data)), \
                                              list(map(lambda x: [x[1][8:-2], x[7]], self.data))

            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(["Фамилия", "Результат"])
            self.table.setRowCount(0)
            for i, row in enumerate(data):
                self.table.setRowCount(
                    self.table.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(elem))
        self.table.resizeColumnsToContents()

    def sort_data(self):
        cur_school = [self.box_school.currentText()] if self.box_school.currentText() != "Все" else self.school_list
        cur_class = [self.box_class.currentText()] if self.box_class.currentText() != "Все" else self.classes_list
        data = list(filter(lambda x: x is not None,
                           map(lambda x: [x[1][8:-2], x[7]] if x[2][12:14] in cur_school and
                                                               x[2][15:17] in cur_class else None, self.data)))
        self.table.setRowCount(0)
        for i, row in enumerate(data):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(elem))
        self.table.resizeColumnsToContents()

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
