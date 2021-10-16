import pickle
from PyQt5.QtWidgets import QWidget
from py_change_task import Ui_form_change_task


class ChangeWindow(QWidget, Ui_form_change_task):

    def __init__(self, date, description, data):
        super().__init__()
        self.setupUi(self)

        self.data = data
        self.old_date = date.toPyDate()
        self.old_description = description

        self.dateTimeEdit.setDate(date)
        self.task.setText(description[8:])
        self.pushButton_change.clicked.connect(self.click_change)
        self.pushButton_cancel.clicked.connect(lambda: self.hide())

    def click_change(self):
        new_description = self.task.text()
        new_date = self.dateTimeEdit.date().toPyDate()

        if new_date not in self.data:
            self.data[new_date] = list()
            i = 0
        else:
            i = self.data[new_date].index(self.old_description)

        self.data[new_date][i] = f"{self.dateTimeEdit.time().toString()[:-3]}:  {new_description}"

        with open("data.txt", "wb") as out_file:
            pickle.dump(self.data, out_file)
        self.hide()