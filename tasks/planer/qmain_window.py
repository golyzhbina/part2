import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore
from py_main_window import Ui_MainWindow
from qcreat_window import CreateWindow
from qchange_window import ChangeWindow


class TaskSystem(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        try:
            with open("data.txt", "rb") as out_file:
                self.data = pickle.load(out_file)
        except EOFError:
            self.data = dict()

        self.calendar.clicked.connect(self.click_calendar)
        self.pushbutton_create.clicked.connect(self.click_create_task)
        self.pushbutton_change.clicked.connect(self.click_change_task)

        self.dateEdit.setDate(self.calendar.selectedDate())
        self.dateEdit.dateChanged.connect(lambda: self.calendar.setSelectedDate(self.dateEdit.date()))

        self.pushbutton_delete.clicked.connect(self.click_delete)
        self.action_create.triggered.connect(self.click_create_task)
        self.action_change.triggered.connect(self.click_change_task)
        self.action_delete.triggered.connect(self.click_delete)
        self.action_exit.triggered.connect(lambda: self.close())

    def click_calendar(self, date):
        date = date.toPyDate()
        data_list_task = self.data.get(date, ['Пока ничего не запланировано'])
        self.list_tasks.clear()
        self.list_tasks.addItems(data_list_task)
        self.dateEdit.setDate(self.calendar.selectedDate())

    def click_create_task(self):

        self.create_window = CreateWindow(self.data, self.dateEdit.date())
        self.create_window.show()

    def click_change_task(self):

        self.change_window = ChangeWindow(self.dateEdit.date(), self.list_tasks.currentItem().text(), self.data)
        self.change_window.show()

    def click_delete(self):

        item = self.list_tasks.takeItem(self.list_tasks.selectedIndexes()[0].row())
        del self.data[self.dateEdit.date().toPyDate()][self.data[self.dateEdit.date().toPyDate()].index(item.text())]

        if len(self.data[self.dateEdit.date().toPyDate()]) == 0:
            del self.data[self.dateEdit.date().toPyDate()]

        with open("data.txt", "wb") as out_file:
            pickle.dump(self.data, out_file)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)
window = TaskSystem()
window.show()
sys.exit(app.exec())

