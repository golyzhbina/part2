import sqlite3
import sys
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox
from main_py import Ui_MainWindow
from add_py import Ui_Form


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_delete.clicked.connect(self.delete)
        self.connection = sqlite3.connect("films.sqlite")
        self.update_table()
        self.lineEdit.textChanged.connect(self.update_table)

    def update_table(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Id", "Название", "Год", "Жанр", "Продолжительность"])
        cursor = self.connection.cursor()
        search = self.lineEdit.text()
        query = f"SELECT * FROM films" + " " + search
        self.genres = cursor.execute("SELECT * FROM genres").fetchall()
        try:
            data = cursor.execute(query).fetchall()
        except sqlite3.OperationalError:
            return
        self.tableWidget.setRowCount(len(data))
        for i, line in enumerate(data):
            self.tableWidget: QTableWidget
            for j, elem in enumerate(line):
                if j == 3:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(next(filter(lambda x: x[0] == elem, self.genres))[1])))
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def add(self):
        self.add_windows = AddWindow(self.genres, self.tableWidget)
        self.add_windows.show()

    def delete(self):
        self.tableWidget: QTableWidget
        selected_items = self.tableWidget.selectedIndexes()
        rows = sorted(set(map(lambda t: t.row(), selected_items)), reverse=True)
        ids = list(map(lambda row: self.tableWidget.item(row, 0).text(), rows))
        cursor = self.connection.cursor()
        for id, row in zip(ids, rows):
            self.tableWidget.removeRow(row)
            cursor.execute(f"DELETE FROM films WHERE id={id}")
        self.connection.commit()


class AddWindow(QWidget, Ui_Form):
    def __init__(self, genres, table):
        super().__init__()
        self.genres = genres
        self.setupUi(self)

        self.tableWidget: QTableWidget = table
        self.connection = sqlite3.connect("films.sqlite")
        self.pushButton_ok.clicked.connect(self.ok)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.comboBox_genre : QComboBox
        self.comboBox_genre.addItems(map(lambda t: t[1], genres))

    def ok(self):

        if len(self.lineEdit_title.text()) and len(self.lineEdit_year.text())\
                and set(self.lineEdit_title.text()) != {" "} and set(self.lineEdit_year.text()) != {" "}:
            cursor = self.connection.cursor()

            id = self.lineEdit_id.text() if len(self.lineEdit_id.text()) \
                                            and set(self.lineEdit_title.text()) != {" "} else False

            if id:
                if int(self.lineEdit_id.text()) in cursor.execute("SELECT id FROM films").fetchall():
                    return

            title = self.lineEdit_title.text()
            year = self.lineEdit_year.text()
            genre = next(filter(lambda x: x[1] == self.comboBox_genre.currentText(), self.genres))[0]
            duration = self.lineEdit_duration.text() if len(self.lineEdit_duration.text()) \
                                                        and set(self.lineEdit_duration.text()) != {" "} else False

            name_of_field = ['id', 'genre', 'duration']
            value_of_field = [id, genre, duration]
            cursor.execute(f"INSERT INTO films(title, year) VALUES('{title}', {year})")
            if not bool(id):
                id = cursor.execute(f"SELECT id FROM films WHERE title='{title}' and year={year}").fetchall()[-1][-1]
                print(id)

            for field in value_of_field:
                if bool(field):
                    cursor.execute(f"""UPDATE films SET {name_of_field[value_of_field.index(field)]}={field} WHERE id=?""", [id])
            self.connection.commit()
            self.close()
            self.update_table()

    def update_table(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Id", "Название", "Год", "Жанр", "Продолжительность"])
        base_query = "SELECT * FROM films"
        cursor = self.connection.cursor()
        data = cursor.execute(base_query).fetchall()

        self.genres = cursor.execute("SELECT * FROM genres").fetchall()
        for i, line in enumerate(data):
            self.tableWidget: QTableWidget
            count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(count)
            for j, elem in enumerate(line):
                if j == 3:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(next(filter(lambda x: x[0] == elem, self.genres))[1])))
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


    def cancel(self):
        self.close()


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


sys.excepthook = excepthook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())