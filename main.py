import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QTimer, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_circleTimer import Ui_MainWindow
import datetime
import json
import time
import os

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if 'vaults.json' not in os.listdir():
            with open('vaults.json', 'w') as file:
                file.write(json.dumps({}))
        else:
            with open('vaults.json', 'r') as file:
                self.vaults = json.load(file)
                if self.vaults == {}:
                    print('No vaults')
                else:
                    self.compose_vaults()

        self.ui.add_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.back_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.save_btn.clicked.connect(lambda: self.add_new_vault())


    def compose_vaults(self):
        for x, vault in enumerate(self.vaults):
            self.delay = self.vaults[vault]
            btn_name = f'button{x}'

            print(self.delay)
            print(btn_name)

            self.button = QPushButton(self.ui.scrollAreaWidgetContents)
            self.button.setObjectName(btn_name)
            self.button.setMinimumSize(QSize(0, 40))
            self.button.setText(f'Vault {x+1}')
            self.button.setStyleSheet(u"color: rgb(255, 255, 255);")
            self.button.clicked.connect(lambda: self.start_timer(self.delay))
            self.ui.verticalLayout_5.addWidget(self.button)


    def start_timer(self, delay):
        #self.ui.stackedWidget.setCurrentIndex(2)
        print(delay)

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