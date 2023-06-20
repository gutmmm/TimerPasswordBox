import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QTimer, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar

from ui_circleTimer import Ui_MainWindow
from functools import partial
import datetime
import json
import time
import os

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buttons events
        self.ui.add_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.back_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.save_btn.clicked.connect(lambda: self.add_new_vault())

        # Round progress bar
        self.ui.progressCircle.rpb_setValue(0)
        self.ui.progressCircle.rpb_setGeometry(80, 0)
        self.ui.progressCircle.rpb_setLineWidth(10)
        self.ui.progressCircle.rpb_setPathWidth(15)
        self.ui.progressCircle.rpb_setLineCap('RoundCap')

        self.settings_file()

        self.timer=QTimer()
        self.timer.timeout.connect(self.update)
        self.bar_value = 0
        self.delay = 0
        

    def settings_file(self):
        if 'vaults.json' not in os.listdir():
            with open('vaults.json', 'w') as file:
                file.write(json.dumps({}))
        else:
            with open('vaults.json', 'r') as file:
                self.vaults = json.load(file)
                if self.vaults == {}:
                    print('No vaults')
                else:
                    print(self.vaults)
                    self.compose_vaults()

    def compose_vaults(self):
        for x, vault in enumerate(self.vaults):
            btn_name = f'button{x}'
            button = QPushButton(self.ui.scrollAreaWidgetContents)
            button.setObjectName(btn_name)
            button.setMinimumSize(QSize(0, 40))
            button.setText(f'Vault {x+1}')
            button.setStyleSheet(u"color: rgb(255, 255, 255);")
            button.clicked.connect(partial(self.start_timer, self.vaults[vault]))
            self.ui.verticalLayout_5.addWidget(button)

    def start_timer(self, time):
        self.delay = int(time)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.step = 100 / int(self.delay)
        self.timer.start(1000)

    def update(self):
        if self.bar_value == 100:
            self.timer.stop()
            self.ui.time_left_label.setText(str(self.delay - 1))
        else:
            self.bar_value += self.step
            self.ui.progressCircle.rpb_setValue(self.bar_value)
            self.ui.time_left_label.setText(str(self.delay - 1))
            self.delay -= 1

    def add_new_vault(self):
        if self.ui.text_input.toPlainText() == '':
            self.start_time = time.time()
            self.ui.text_input.setPlaceholderText("This placholder can't be empty")
            self.timer = QTimer()
            self.timer.timeout.connect(
                lambda: self.ui.text_input.setPlaceholderText("")
                if (time.time() - self.start_time >= 1)
                else None
                )
            self.timer.start(1000)
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())