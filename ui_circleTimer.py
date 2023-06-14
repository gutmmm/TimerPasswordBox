# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circleTimerQMPTel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
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
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 780)
        MainWindow.setMinimumSize(QSize(500, 765))
        MainWindow.setMaximumSize(QSize(500, 1000))
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 1000))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 266))
        self.frame.setMaximumSize(QSize(16777215, 359))
        self.frame.setCursor(QCursor(Qt.SizeVerCursor))
        self.frame.setMouseTracking(True)
        self.frame.setTabletTracking(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.circuralProgresBarBase = QFrame(self.frame)
        self.circuralProgresBarBase.setObjectName(u"circuralProgresBarBase")
        self.circuralProgresBarBase.setGeometry(QRect(80, 30, 320, 320))
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
        self.container.setStyleSheet(u"background-color: rgba(77, 77, 127);\n"
"border-radius: 140px;\n"
"")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.timeEdit = QTimeEdit(self.container)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(-20, 0, 331, 281))
        font = QFont()
        font.setPointSize(33)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.timeEdit.setFrame(False)
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.container)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(93, 170, 91, 20))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setFocusPolicy(Qt.WheelFocus)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.container)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(107, 90, 61, 20))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setFocusPolicy(Qt.WheelFocus)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.circurallBg.raise_()
        self.circuralProgress.raise_()
        self.container.raise_()

        self.verticalLayout_3.addWidget(self.frame)

        self.button_frame = QFrame(self.centralwidget)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setMinimumSize(QSize(0, 30))
        self.button_frame.setMaximumSize(QSize(16777215, 50))
        self.button_frame.setFrameShape(QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.start_button = QPushButton(self.button_frame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(0, 0, 471, 40))
        self.start_button.setMinimumSize(QSize(180, 40))
        self.start_button.setMaximumSize(QSize(500, 16777215))
        self.start_button.setFont(font2)
        self.start_button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.button_frame)

        self.floating_frame = QFrame(self.centralwidget)
        self.floating_frame.setObjectName(u"floating_frame")
        self.floating_frame.setMinimumSize(QSize(0, 320))
        self.floating_frame.setFrameShape(QFrame.StyledPanel)
        self.floating_frame.setFrameShadow(QFrame.Sunken)
        self.info_frame = QFrame(self.floating_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(0, 10, 470, 0))
        self.info_frame.setMinimumSize(QSize(0, 0))
        self.info_frame.setMaximumSize(QSize(16777215, 0))
        self.info_frame.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"border-radius: 10px;")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.textBrowser = QTextBrowser(self.info_frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 10, 441, 251))
        self.settings_frame = QFrame(self.floating_frame)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setGeometry(QRect(0, 0, 469, 310))
        self.settings_frame.setMinimumSize(QSize(469, 310))
        self.settings_frame.setMaximumSize(QSize(470, 0))
        self.settings_frame.setStyleSheet(u"background-color: rgb(51, 51, 51);\n"
"border-radius: 10px;")
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.settings_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.settings_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.settings_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(31, 31, 31, 50);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setLineWidth(10)
        self.frame_2.setMidLineWidth(10)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit.setFrameShape(QFrame.StyledPanel)
        self.plainTextEdit.setFrameShadow(QFrame.Sunken)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.plainTextEdit)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.floating_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"(HH:mm)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SCROLL", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START TIMER", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Lorem Ipsum</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Information to store", None))
    # retranslateUi

