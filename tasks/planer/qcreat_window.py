import pickle
from PyQt5.QtWidgets import QWidget
from py_creat_task import Ui_form_task_creat


class CreateWindow(QWidget, Ui_form_task_creat):

    def __init__(self, list_tasks, date):
        super().__init__()
        self.setupUi(self)
        self.data = list_tasks
        self.dateTimeEdit.setDate(date)
        self.pushbutton_creat.clicked.connect(self.create_task)
        self.pushbutton_cancel.clicked.connect(lambda: self.hide())

    def create_task(self):
        description = self.task.text()
        date = self.dateTimeEdit.date().toPyDate()

        if date not in self.data:
            self.data[date] = list()

        self.data[date].append(f"{self.dateTimeEdit.time().toString()[:-3]}:  {description}")

        with open("data.txt", "wb") as out_file:
            pickle.dump(self.data, out_file)
        self.hide()