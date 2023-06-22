# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circleTimerCeNYtV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 550)
        MainWindow.setMinimumSize(QSize(500, 550))
        MainWindow.setMaximumSize(QSize(500, 550))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(31, 31, 31, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(190, 190, 190, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(490, 540))
        self.centralwidget.setMaximumSize(QSize(490, 540))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.floating_frame = QFrame(self.centralwidget)
        self.floating_frame.setObjectName(u"floating_frame")
        self.floating_frame.setMinimumSize(QSize(490, 540))
        self.floating_frame.setMaximumSize(QSize(490, 540))
        self.floating_frame.setFrameShape(QFrame.StyledPanel)
        self.floating_frame.setFrameShadow(QFrame.Sunken)
        self.stackedWidget = QStackedWidget(self.floating_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 481, 550))
        self.stackedWidget.setMinimumSize(QSize(481, 550))
        self.stackedWidget.setMaximumSize(QSize(500, 550))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 441, 396))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.add_btn = QPushButton(self.frame_7)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.add_btn)


        self.verticalLayout.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMinimumSize(QSize(500, 0))
        self.page_2.setMaximumSize(QSize(500, 16777215))
        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 480, 541))
        self.frame_5.setMinimumSize(QSize(480, 0))
        self.frame_5.setMaximumSize(QSize(480, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 80))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.delaySet = QSpinBox(self.frame_11)
        self.delaySet.setObjectName(u"delaySet")
        self.delaySet.setGeometry(QRect(0, 10, 201, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.delaySet.setFont(font1)
        self.delaySet.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(55, 55, 55);")
        self.delaySet.setAlignment(Qt.AlignCenter)
        self.delaySet.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.delaySet.setMinimum(1)
        self.delaySet.setValue(5)

        self.horizontalLayout_2.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.delay_format = QComboBox(self.frame_10)
        self.delay_format.addItem("")
        self.delay_format.addItem("")
        self.delay_format.addItem("")
        self.delay_format.setObjectName(u"delay_format")
        self.delay_format.setGeometry(QRect(0, 10, 191, 51))
        self.delay_format.setFont(font1)
        self.delay_format.setLayoutDirection(Qt.LeftToRight)
        self.delay_format.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-color: rgb(119, 118, 123);")

        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.vaultTitleLabel = QLabel(self.frame_6)
        self.vaultTitleLabel.setObjectName(u"vaultTitleLabel")
        self.vaultTitleLabel.setFont(font1)
        self.vaultTitleLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vaultTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.vaultTitleLabel)

        self.vault_title = QLineEdit(self.frame_6)
        self.vault_title.setObjectName(u"vault_title")
        self.vault_title.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.vault_title.setFont(font2)
        self.vault_title.setStyleSheet(u"background-color: rgb(55, 55, 55);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.vault_title)

        self.vaultMessageLabel = QLabel(self.frame_6)
        self.vaultMessageLabel.setObjectName(u"vaultMessageLabel")
        self.vaultMessageLabel.setFont(font1)
        self.vaultMessageLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vaultMessageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.vaultMessageLabel)

        self.vault_message = QTextEdit(self.frame_6)
        self.vault_message.setObjectName(u"vault_message")
        self.vault_message.setFont(font2)
        self.vault_message.setStyleSheet(u"background-color: rgb(55, 55, 55);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.vault_message)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.save_btn = QPushButton(self.frame_2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 50))
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.save_btn)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.progressCircle = roundProgressBar(self.page_3)
        self.progressCircle.setObjectName(u"progressCircle")
        self.progressCircle.setMinimumSize(QSize(0, 300))
        self.progressCircle.setMaximumSize(QSize(16777215, 300))
        self.timeEdit = QTimeEdit(self.progressCircle)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setEnabled(False)
        self.timeEdit.setGeometry(QRect(140, 190, 181, 51))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.timeEdit.setFont(font3)
        self.timeEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.label_2 = QLabel(self.progressCircle)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(171, 230, 121, 20))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.progressCircle)

        self.frame_8 = QFrame(self.page_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 200))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.message = QLabel(self.frame_8)
        self.message.setObjectName(u"message")
        self.message.setFont(font3)
        self.message.setStyleSheet(u"background-color: rgb(55, 55, 55);\n"
"color: rgb(255, 255, 255);")
        self.message.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.message)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_3.addWidget(self.floating_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Avialable Vaults", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add New Vault", None))
        self.delay_format.setItemText(0, QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.delay_format.setItemText(1, QCoreApplication.translate("MainWindow", u"Hours", None))
        self.delay_format.setItemText(2, QCoreApplication.translate("MainWindow", u"Days", None))

        self.vaultTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Vault Title", None))
        self.vaultMessageLabel.setText(QCoreApplication.translate("MainWindow", u"Enter details", None))
        self.vault_message.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:400;\"><br /></p></body></html>", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DD:HH:mm", None))
        self.message.setText("")
    # retranslateUi

