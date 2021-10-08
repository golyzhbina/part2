from homework6 import MainWindow
from PyQt5.QtWidgets import QTextEdit, QApplication, QLineEdit
import sys


class ModifiedMainWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.mod_initMW()

    def mod_initMW(self):

        self.plain_edit.setGeometry(20, 140, 170, 100)

        self.count_cheeseburger = QLineEdit(self)
        self.count_cheeseburger.setGeometry(100, 27, 20, 15)
        self.count_cheeseburger.setEnabled(False)

        self.count_hamburger = QLineEdit(self)
        self.count_hamburger.setGeometry(100, 47, 20, 15)
        self.count_hamburger.setEnabled(False)

        self.count_cola = QLineEdit(self)
        self.count_cola.setGeometry(100, 67, 20, 15)
        self.count_cola.setEnabled(False)

        self.count_nuggets = QLineEdit(self)
        self.count_nuggets.setGeometry(100, 87, 20, 15)
        self.count_nuggets.setEnabled(False)

        self.dict_checkbox = {self.check_box_1.text(): self.count_cheeseburger,
                              self.check_box_2.text(): self.count_hamburger,
                              self.check_box_3.text(): self.count_cola,
                              self.check_box_4.text(): self.count_nuggets}

        self.price = {self.check_box_1.text(): 100,
                      self.check_box_2.text(): 120,
                      self.check_box_3.text(): 60,
                      self.check_box_4.text(): 10}

    def add_in_list(self):

        super(ModifiedMainWindow, self).add_in_list()
        self.dict_checkbox[self.sender().text()].setEnabled(True)

    def out(self):
        out = [self.order[0]]
        for pos in range(1, len(self.order)):
            count = self.dict_checkbox[self.order[pos]].text()
            out_i = self.order[pos].ljust(13, ".") + count + " шт."
            out_i = out_i.ljust(20, ".") + str(int(count) * self.price[self.order[pos]]) + " руб."
            out.append(out_i)

        self.plain_edit.setPlainText('\n'.join(out))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ModifiedMainWindow()
    ex.show()
    sys.exit(app.exec())
