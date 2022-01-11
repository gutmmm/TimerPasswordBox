# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circleTimerJRNwur.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 750)
        MainWindow.setMinimumSize(QSize(500, 750))
        MainWindow.setMaximumSize(QSize(500, 750))
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.counter = QFrame(self.centralwidget)
        self.counter.setObjectName(u"counter")
        self.counter.setMinimumSize(QSize(0, 0))
        self.counter.setMaximumSize(QSize(500, 500))
        self.counter.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"border-radius: 10px;")
        self.counter.setFrameShape(QFrame.StyledPanel)
        self.counter.setFrameShadow(QFrame.Raised)
        self.circuralProgresBarBase = QFrame(self.counter)
        self.circuralProgresBarBase.setObjectName(u"circuralProgresBarBase")
        self.circuralProgresBarBase.setGeometry(QRect(83, 6, 320, 320))
        self.circuralProgresBarBase.setMaximumSize(QSize(320, 320))
        self.circuralProgresBarBase.setFrameShape(QFrame.NoFrame)
        self.circuralProgresBarBase.setFrameShadow(QFrame.Raised)
        self.circuralProgress = QFrame(self.circuralProgresBarBase)
        self.circuralProgress.setObjectName(u"circuralProgress")
        self.circuralProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circuralProgress.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.0 rgba(200, 33, 142, 0), stop:0.001 rgba(85, 170, 255, 255));\n"
"}")
        self.circuralProgress.setFrameShape(QFrame.NoFrame)
        self.circuralProgress.setFrameShadow(QFrame.Raised)
        self.circurallBg = QFrame(self.circuralProgresBarBase)
        self.circurallBg.setObjectName(u"circurallBg")
        self.circurallBg.setGeometry(QRect(10, 10, 300, 300))
        self.circurallBg.setStyleSheet(u" border-radius: 150px;\n"
"background-color:rgba(77,77,127, 120);")
        self.circurallBg.setFrameShape(QFrame.StyledPanel)
        self.circurallBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circuralProgresBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(20, 20, 280, 280))
        self.container.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(77, 77, 127);\n"
"	border-radius: 140px;\n"
"}")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.timeLabel = QLabel(self.container)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(30, 70, 221, 131))
        font = QFont()
        font.setFamily(u"Roboto Thin")
        font.setPointSize(40)
        self.timeLabel.setFont(font)
        self.timeLabel.setTextFormat(Qt.AutoText)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.circurallBg.raise_()
        self.circuralProgress.raise_()
        self.container.raise_()

        self.verticalLayout_3.addWidget(self.counter)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")

        self.verticalLayout_3.addWidget(self.startButton)

        self.infoFrame = QFrame(self.centralwidget)
        self.infoFrame.setObjectName(u"infoFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoFrame.sizePolicy().hasHeightForWidth())
        self.infoFrame.setSizePolicy(sizePolicy)
        self.infoFrame.setMaximumSize(QSize(500, 300))
        self.infoFrame.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"border-radius: 10px;")
        self.infoFrame.setFrameShape(QFrame.NoFrame)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.infoFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 451, 301))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.row1 = QFrame(self.layoutWidget)
        self.row1.setObjectName(u"row1")
        self.row1.setFrameShape(QFrame.StyledPanel)
        self.row1.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.row1)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 431, 81))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.emailFrame = QFrame(self.layoutWidget1)
        self.emailFrame.setObjectName(u"emailFrame")
        self.emailFrame.setFrameShape(QFrame.StyledPanel)
        self.emailFrame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.emailFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 131, 61))
        font1 = QFont()
        font1.setFamily(u"Roboto Mono Thin [pyrs]")
        font1.setPointSize(24)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.emailFrame)

        self.emailInfo = QFrame(self.layoutWidget1)
        self.emailInfo.setObjectName(u"emailInfo")
        self.emailInfo.setStyleSheet(u"background-color: rgb(31,31,31);")
        self.emailInfo.setFrameShape(QFrame.StyledPanel)
        self.emailInfo.setFrameShadow(QFrame.Raised)
        self.email = QLabel(self.emailInfo)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(10, 20, 250, 40))

        self.horizontalLayout.addWidget(self.emailInfo)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addWidget(self.row1)

        self.row2 = QFrame(self.layoutWidget)
        self.row2.setObjectName(u"row2")
        self.row2.setMaximumSize(QSize(16777215, 90))
        self.row2.setFrameShape(QFrame.StyledPanel)
        self.row2.setFrameShadow(QFrame.Raised)
        self.layoutWidget2 = QWidget(self.row2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 0, 431, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.passFrame = QFrame(self.layoutWidget2)
        self.passFrame.setObjectName(u"passFrame")
        self.passFrame.setFrameShape(QFrame.StyledPanel)
        self.passFrame.setFrameShadow(QFrame.Raised)
        self.passInfo = QLabel(self.passFrame)
        self.passInfo.setObjectName(u"passInfo")
        self.passInfo.setGeometry(QRect(0, 10, 131, 51))
        self.passInfo.setFont(font1)

        self.horizontalLayout_2.addWidget(self.passFrame)

        self.frame_9 = QFrame(self.layoutWidget2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.password = QLabel(self.frame_9)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(10, 20, 250, 40))

        self.horizontalLayout_2.addWidget(self.frame_9)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.row2)

        self.row3 = QFrame(self.layoutWidget)
        self.row3.setObjectName(u"row3")
        self.row3.setFrameShape(QFrame.StyledPanel)
        self.row3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.row3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 0, 431, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.digitPass = QFrame(self.layoutWidget_2)
        self.digitPass.setObjectName(u"digitPass")
        self.digitPass.setFrameShape(QFrame.StyledPanel)
        self.digitPass.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.digitPass)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 131, 31))
        font2 = QFont()
        font2.setFamily(u"Roboto Mono Thin [pyrs]")
        font2.setPointSize(13)
        self.label_4.setFont(font2)

        self.horizontalLayout_3.addWidget(self.digitPass)

        self.digitInfo = QFrame(self.layoutWidget_2)
        self.digitInfo.setObjectName(u"digitInfo")
        self.digitInfo.setStyleSheet(u"background-color: rgb(31,31,31);")
        self.digitInfo.setFrameShape(QFrame.StyledPanel)
        self.digitInfo.setFrameShadow(QFrame.Raised)
        self.digits = QLabel(self.digitInfo)
        self.digits.setObjectName(u"digits")
        self.digits.setGeometry(QRect(10, 20, 250, 40))

        self.horizontalLayout_3.addWidget(self.digitInfo)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout.addWidget(self.row3)


        self.verticalLayout_3.addWidget(self.infoFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\">90%</p>", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START TIMER", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.email.setText("")
        self.passInfo.setText(QCoreApplication.translate("MainWindow", u"PASS", None))
        self.password.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DIGIT PASS", None))
        self.digits.setText("")
    # retranslateUi

