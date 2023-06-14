import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QTimer, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QGraphicsBlurEffect

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
        self.show()

        # FUNCTIONS CONNECT
        self.ui.start_button.clicked.connect(self.check_user_input)
        self.ui.timeEdit.timeChanged.connect(lambda: self.calculate_time())

        self.init_value = 0
        self.duration = 0
        self.stepper = 0

        self.blur = QGraphicsBlurEffect()
        self.blur.setBlurRadius(15)

        self.unblur = QGraphicsBlurEffect()
        self.unblur.setBlurRadius(0)
  
    def calculate_time(self):
        self.duration = (self.ui.timeEdit.time().hour()*60 + self.ui.timeEdit.time().minute())*60
        self.step = 1/self.duration
        self.start_time = str(datetime.timedelta(seconds=self.duration))


    def check_user_input(self):
        if self.ui.plainTextEdit.toPlainText() == '' or self.duration == 0:
            self.ui.plainTextEdit.setPlaceholderText('Please enter information and set the timer')
        else:
            self.ui.timeEdit.stepUp()
            self.ui.floating_frame.setGraphicsEffect(self.blur)
            self.set_timer()


    def set_timer(self):
        self.timer=QTimer()
        self.timer.timeout.connect(self.progressbar_step)
        self.timer.start(1000)

    def progressbar_step(self):

        #self.ui.timeEdit.stepDown()
        self.stepper += 1
        if self.stepper%60 == 1:
            self.ui.timeEdit.stepDown()

        self.update_progress_bar(1 - self.init_value - self.step)
        self.init_value += self.step

        if self.init_value >= 1:
            self.stop_and_show()
            
    def stop_and_show(self):
        self.timer.stop()
        self.ui.floating_frame.setGraphicsEffect(self.unblur)
        

            
    def update_progress_bar(self, value):
        stop_1 = str(value)
        stop_2 = str(value+0.001)
        styleSheet = """
                        border-radius: 150px;
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
                        stop:{stop1} rgba(200, 33, 142, 0), 
                        stop:{stop2} rgba(85, 170, 255, 255));"""


        updateStyleSheet = styleSheet.replace("{stop1}", stop_1).replace("{stop2}", stop_2)
        self.ui.circuralProgress.setStyleSheet(updateStyleSheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
