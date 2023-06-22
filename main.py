from functools import partial
import datetime
import json
import time
import sys
import os

from cryptography.fernet import Fernet

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QTimer, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from ui_circleTimer import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        # Set UI
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buttons events
        self.ui.add_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.save_btn.clicked.connect(lambda: self.add_new_vault())

        # Round progress bar
        self.ui.progressCircle.rpb_setValue(0)
        self.ui.progressCircle.rpb_setGeometry(80, 0)
        self.ui.progressCircle.rpb_setLineWidth(10)
        self.ui.progressCircle.rpb_setPathWidth(15)
        self.ui.progressCircle.rpb_setLineCap('RoundCap')

        # Start the timer and connect to update function
        self.timer=QTimer()
        self.timer.timeout.connect(self.update)

        #Set attributes
        self.bar_value = 0
        self.seconds_to_end = 0

        self.key = b'3pWjI3fV1wPw3duy96RdFzEG67Z8Kh3qarO7FxE0bls='
        self.fernet = Fernet(self.key)

        self.compose_settings()

    def compose_settings(self):
        if 'vaults.json' not in os.listdir():
            with open('vaults.json', 'w') as file:
                file.write(json.dumps([]))
        else:
            with open('vaults.json', 'r') as file:
                self.vaults = json.load(file)
                self.compose_vaults()
                    
    def compose_vaults(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        for x, vault in enumerate(self.vaults):
            button = QPushButton(self.ui.scrollAreaWidgetContents)
            button.setObjectName(f'button{x}')
            button.setMinimumSize(QSize(0, 40))
            button.setText(vault['vault name'])
            button.setStyleSheet(u"color: rgb(255, 255, 255);")
            button.clicked.connect(partial(self.start_timer, vault))
            self.ui.verticalLayout_5.addWidget(button)

    def start_timer(self, vault):
        time_in_seconds = self.convert_time_to_seconds(int(vault['delay']), vault['format'])
        self.password = vault['password']
        self.seconds_to_end = int(time_in_seconds)
        self.step = 100 / int(self.seconds_to_end)
        self.timer.start(1000)
        self.ui.stackedWidget.setCurrentIndex(2)

    def update(self):
        if self.bar_value >= 100:
            pass_to_decrypt = bytes(self.password, 'utf-8')
            decrypted_password = self.fernet.decrypt(pass_to_decrypt).decode()
            self.ui.message.setText(decrypted_password)
            self.timer.stop()
        else:
            td = datetime.timedelta(seconds=self.seconds_to_end)
            formated_time_left = QtCore.QTime(td.seconds//3600, (td.seconds//60)%60, td.seconds%60 - 1 )
            self.ui.timeEdit.setTime(formated_time_left)
            self.seconds_to_end -= 1
            self.bar_value += self.step
            self.ui.progressCircle.rpb_setValue(self.bar_value)

    def add_new_vault(self):
        if self.ui.vault_message.toPlainText() == '' or self.ui.vault_title == '':
            self.start_time = time.time()
            self.ui.vault_title.setPlaceholderText("This placholder can't be empty")
            self.ui.vault_message.setPlaceholderText("This placholder can't be empty")
            
            self.timer = QTimer()
            self.timer.timeout.connect(lambda: self.ui.vault_title.setPlaceholderText("") 
                                       and self.ui.vault_message.setPlaceholderText("") 
                                       if (time.time() - self.start_time >= 1) else None)
            self.timer.start(1000)
        else:
            with open('vaults.json', 'r') as file:
                data = json.load(file)
            password = self.ui.vault_message.toPlainText()
            encMessage = self.fernet.encrypt(password.encode()).decode('utf-8')

            new_vault = {"vault name" : self.ui.vault_title.text(), 
                         "delay" : self.ui.delaySet.cleanText(),
                         "format" : self.ui.delay_format.currentText(),
                         "password" : str(encMessage)}

            data.append(new_vault)
            with open('vaults.json', 'w+') as file:
                json.dump(data, file)

            self.reset_scroll_area()
            self.ui.stackedWidget.setCurrentIndex(0)

    def convert_time_to_seconds(self, delay, format):
        if format == 'Minutes':
            return delay*60
        elif format == 'Hours':
            return delay*60*60
        elif format == 'Days':
            return delay*60*60*24
        else:
            return delay

    def reset_scroll_area(self):
        count = self.ui.verticalLayout_5.count()
        for x in range(count):
            item = self.ui.verticalLayout_5.itemAt(x)
            widget = item.widget()
            widget.deleteLater()

        self.compose_settings()
        self.ui.stackedWidget.setCurrentIndex(0)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())