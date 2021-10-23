from PyQt5.QtWidgets import QPushButton, QRadioButton, QApplication, QMainWindow, QLabel
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initMW()

    def initMW(self):

        self.setGeometry(500, 100, 300, 370)
        self.setWindowTitle("Крестики-нолики")

        self.winner = QLabel(self)
        self.winner.setGeometry(140, 20, 50, 20)
        self.winner.setText("GO!")

        self.button_new_game = QPushButton(self)
        self.button_new_game.setGeometry(100, 50, 70, 30)
        self.button_new_game.setText("Новая игра")
        self.button_new_game.clicked.connect(self.new_game)

        self.radio_button_x = QRadioButton(self)
        self.radio_button_x.setGeometry(20, 50, 30, 30)
        self.radio_button_x.setText("x")
        self.radio_button_x.setChecked(True)

        self.radio_button_o = QRadioButton(self)
        self.radio_button_o.setGeometry(60, 50, 30, 30)
        self.radio_button_o.setText("o")

        self.button_00 = QPushButton(self)
        self.button_00.setGeometry(20, 100, 70, 70)
        self.button_00.clicked.connect(self.player_turn)

        self.button_10 = QPushButton(self)
        self.button_10.setGeometry(20, 180, 70, 70)
        self.button_10.clicked.connect(self.player_turn)

        self.button_20 = QPushButton(self)
        self.button_20.setGeometry(20, 260, 70, 70)
        self.button_20.clicked.connect(self.player_turn)

        self.button_01 = QPushButton(self)
        self.button_01.setGeometry(100, 100, 70, 70)
        self.button_01.clicked.connect(self.player_turn)

        self.button_11 = QPushButton(self)
        self.button_11.setGeometry(100, 180, 70, 70)
        self.button_11.clicked.connect(self.player_turn)

        self.button_21 = QPushButton(self)
        self.button_21.setGeometry(100, 260, 70, 70)
        self.button_21.clicked.connect(self.player_turn)

        self.button_02 = QPushButton(self)
        self.button_02.setGeometry(180, 100, 70, 70)
        self.button_02.clicked.connect(self.player_turn)

        self.button_12 = QPushButton(self)
        self.button_12.setGeometry(180, 180, 70, 70)
        self.button_12.clicked.connect(self.player_turn)

        self.button_22 = QPushButton(self)
        self.button_22.setGeometry(180, 260, 70, 70)
        self.button_22.clicked.connect(self.player_turn)

        self.buttons = [[self.button_00, self.button_01, self.button_02],
                        [self.button_10, self.button_11, self.button_12],
                        [self.button_20, self.button_21, self.button_22]]

        self.playing_field = [["0"] * 3 for _ in range(3)]
        self.count = 0
        self.end = False
        self.flag = self.radio_button_x.isChecked()

    def player_turn(self):

        sender = self.sender()
        if bool(len(sender.text())):
            return

        indexes = None
        self.flag = self.radio_button_x.isChecked()

        for lst in self.buttons:
            if sender in lst:
                indexes = [self.buttons.index(lst), lst.index(sender)]

        if self.count == 0 and self.flag or self.count % 2 == 0 and self.flag\
                or self.count % 2 == 1 and not self.flag:
            sender.setText("x")
            self.playing_field[indexes[0]][indexes[1]] = "x"

        elif self.count == 0 and not self.flag or self.count % 2 == 0 and not self.flag \
                or self.count % 2 == 1 and self.flag:
            sender.setText("o")
            self.playing_field[indexes[0]][indexes[1]] = "o"

        self.count += 1
        self.check()

    def check(self):

        playing_field_rev = [[self.playing_field[j][i] for j in range(3)] for i in range(3)]

        for char in ["x", "o"]:
            for i in range(3):
                if len(list(filter(lambda x: x == char, self.playing_field[i]))) == 3 \
                        or len(list(filter(lambda x: x == char, playing_field_rev[i]))) == 3:
                    self.winner.setText(f"Winner: {char}!")
                    self.game_over()
                    return

        for char in ["x", "o"]:
            if self.buttons[1][1].text() == char and self.buttons[0][0].text() == char \
                    and self.buttons[2][2].text() == char \
            or self.buttons[1][1].text() == char and self.buttons[0][2].text() == char\
                    and self.buttons[2][0].text() == char:
                self.winner.setText(f"Winner: {char}!")
                self.game_over()
                return

    def game_over(self):

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setEnabled(False)

    def new_game(self):

        self.playing_field = [["0"] * 3 for i in range(3)]
        self.count = 0
        self.winner.setText("GO!")

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText(None)
                self.buttons[i][j].setEnabled(True)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())
