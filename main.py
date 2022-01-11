import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QTimer, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_circleTimer import Ui_MainWindow
import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.startButton.clicked.connect(self.set_timer)

        self.duration = 12*60*60
        self.step = 1/self.duration
        self.start_time = str(datetime.timedelta(seconds=self.duration))
        self.ui.timeLabel.setText(self.start_time)
        
        self.init_value = 0

    def calc_times(self):
        now = datetime.datetime

    def set_timer(self):
        self.timer=QTimer()
        self.timer.timeout.connect(self.progressbar_step)
        self.timer.start(1000)

    def progressbar_step(self):
        self.update_progress_bar(1 - self.init_value-self.step)
        self.init_value += self.step
        self.time_label_update()

        if self.init_value >= 1:
            self.stop_and_show()
            
    def stop_and_show(self):
        self.timer.stop()
        self.ui.timeLabel.setText('<p align="center">DONE</p>')
        self.ui.email.setText('<p align="center">danielody@protonmail.com <br> maryzemorf@yandex.com </p>')
        self.ui.password.setText('<p align="center"> #### <br> ####</p>')
        self.ui.digits.setText('<p align="center">####</p>')


    def time_label_update(self):
            html_label_text = """<p align="center">{Value}</p>"""
            self.duration -= 1
            self.updated_time = str(datetime.timedelta(seconds=self.duration))
            new_html_label = html_label_text.replace("{Value}", self.updated_time)
            self.ui.timeLabel.setText(new_html_label)

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
