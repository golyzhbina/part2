from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QPlainTextEdit
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initMW()

    def initMW(self):

        self.setGeometry(500, 200, 200, 300)
        self.setWindowTitle("Заказа в Мкдональдсе")

        self.check_box_1 = QCheckBox(self)
        self.check_box_1.sizeHint()
        self.check_box_1.move(20, 20)
        self.check_box_1.setText("Чизбургер")
        self.check_box_1.stateChanged.connect(self.add_in_list)

        self.check_box_2 = QCheckBox(self)
        self.check_box_2.sizeHint()
        self.check_box_2.move(20, 40)
        self.check_box_2.setText("Гамбургер")
        self.check_box_2.stateChanged.connect(self.add_in_list)

        self.check_box_3 = QCheckBox(self)
        self.check_box_3.sizeHint()
        self.check_box_3.move(20, 60)
        self.check_box_3.setText("Кока-кола")
        self.check_box_3.stateChanged.connect(self.add_in_list)

        self.check_box_4 = QCheckBox(self)
        self.check_box_4.sizeHint()
        self.check_box_4.move(20, 80)
        self.check_box_4.setText("Наггетсы")
        self.check_box_4.stateChanged.connect(self.add_in_list)

        self.plain_edit = QPlainTextEdit(self)
        self.plain_edit.setGeometry(20, 140, 100, 100)
        self.plain_edit.setEnabled(False)

        self.order_food = QPushButton(self)
        self.order_food.setGeometry(60, 110, 60, 25)
        self.order_food.setText("Заказать")
        self.order_food.clicked.connect(self.out)

        self.flag = False
        self.order = ["Ваш заказ:" + '\n']

    def add_in_list(self):

        sender = self.sender().text()
        if sender not in self.order:
            self.order.append(sender)
        else:
            del self.order[self.order.index(sender)]

    def out(self):

        self.plain_edit.setPlainText('\n'.join(self.order))




app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())