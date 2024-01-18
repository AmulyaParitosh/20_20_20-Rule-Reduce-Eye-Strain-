import sys
from typing import (
    Generator,
    NoReturn,
)

import chime
from PyQt5.QtCore import (
    Qt,
    QTimer,
)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Rule(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.seconds = 20
        self.setWindowTitle("20-20-20")
        self.setGeometry(750, 450, 500, 100)
        self.create_ui()
        self.rule_seq = self._sequence()
        self.show()

    def create_ui(self) -> None:

        self.start = False
        self.count = 0

        self.widget_layout = QVBoxLayout()

        self.text = QLabel(self)
        self.text.setText("FOLLOW 20-20-20 RULE")
        self.text.setFont(QFont("Times", 24))
        self.text.setAlignment(Qt.AlignCenter)

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(QFont("Times", 22))

        self.button_text = "Start"
        self.button = QPushButton(self.button_text, self)
        self.button.setFont(QFont("Times", 15))
        self.button.clicked.connect(self.sequence)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.widget_layout.addWidget(self.text)
        self.widget_layout.addWidget(self.time_label)
        self.widget_layout.addWidget(self.button)

        self.setLayout(self.widget_layout)

    def show_time(self) -> None:
        if not self.start:
            return

        if self.count < 3:
            chime.info()

        if self.count > 0:
            text = str(self.count) + "s"
            self.time_label.setText(text)

        else:
            self.start = False
            self.time_label.setText("click next")
            self.button.setText(self.button_text)
            self.button.setDisabled(False)

        self.count -= 1

    def _sequence(self) -> Generator[None, None, None]:
        self.close_eyes()
        yield None
        self.look_away()
        yield None

    def sequence(self) -> None:
        try:
            return next(self.rule_seq)
        except StopIteration:
            self.close()

    def reset(self) -> None:
        self.count = self.seconds
        self.start = True

    def close_eyes(self) -> None:
        self.button.setDisabled(True)
        self.text.setText("Close your eyes for 20 secs")
        self.button_text = "Next"
        self.reset()

    def look_away(self) -> None:
        self.button.setDisabled(True)
        self.text.setText("Look away at 20 feets for 20 secs")
        self.button_text = "Close"
        self.reset()


def follow() -> NoReturn:
    app = QApplication(sys.argv)
    Rule()
    sys.exit(app.exec_())


if __name__ == "__main__":
    follow()
