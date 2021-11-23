import csv
import sys

from PyQt5.QtGui import QColor, QFont

from table_titanic_py import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.data = None
        self.title = None

        self.load_data("titanic.csv")

        self.textEdit.textChanged.connect(lambda: self.search() if len(self.textEdit.toPlainText()) > 2 else None)
        font = QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)

    def load_data(self, table_name):

        with open(table_name, encoding="utf8") as csv_file:
            reader = list(csv.reader(csv_file, delimiter=',', quotechar='"'))
            self.title = reader[0][1:]
            self.data = list(map(lambda x: x[1:], reader[1:]))

        self.load_table(self.data)

    def load_table(self, data):

        self.tableWidget.setColumnCount(len(self.title))
        self.tableWidget.setHorizontalHeaderLabels(self.title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))

                if row[4] == "0":
                    self.tableWidget.item(i, j).setBackground(QColor(255, 0, 0))
                else:
                    self.tableWidget.item(i, j).setBackground(QColor(0, 255, 0))
        self.tableWidget.resizeColumnsToContents()

    def search(self):

        text = self.textEdit.toPlainText()
        new_data = list(filter(lambda x: x is not None, map(lambda x: x if text.lower() in x[0].lower() else None, self.data)))

        self.load_table(new_data)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())