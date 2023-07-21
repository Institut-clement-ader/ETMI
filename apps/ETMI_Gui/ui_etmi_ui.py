# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_etmi.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpenFile = QAction(MainWindow)
        self.actionOpenFile.setObjectName(u"actionOpenFile")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_quit = QPushButton(self.centralwidget)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setGeometry(QRect(710, 510, 75, 24))
        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setGeometry(QRect(710, 470, 75, 24))
        self.btn_run.setFocusPolicy(Qt.NoFocus)
        self.btn_manual = QPushButton(self.centralwidget)
        self.btn_manual.setObjectName(u"btn_manual")
        self.btn_manual.setGeometry(QRect(20, 100, 81, 24))
        self.btn_manual.setStyleSheet(u"background-color: rgb(23, 227, 0);\n"
"border:0;\n"
"")
        self.btn_auto = QPushButton(self.centralwidget)
        self.btn_auto.setObjectName(u"btn_auto")
        self.btn_auto.setGeometry(QRect(20, 130, 81, 24))
        self.btn_auto.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(255, 255, 255);")
        self.led_joy_status = QFrame(self.centralwidget)
        self.led_joy_status.setObjectName(u"led_joy_status")
        self.led_joy_status.setGeometry(QRect(300, 170, 16, 16))
        self.led_joy_status.setMinimumSize(QSize(14, 14))
        self.led_joy_status.setMaximumSize(QSize(16, 16))
        self.led_joy_status.setStyleSheet(u"background-color: rgb(85, 255, 0);\n"
"border-radius: 8px;\n"
"")
        self.led_joy_status.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.led_joy_status.setFrameShape(QFrame.StyledPanel)
        self.led_joy_status.setFrameShadow(QFrame.Raised)
        self.btn_parameters = QPushButton(self.centralwidget)
        self.btn_parameters.setObjectName(u"btn_parameters")
        self.btn_parameters.setGeometry(QRect(20, 160, 81, 24))
        self.btn_parameters.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(255, 255, 255);")
        self.btn_logs = QPushButton(self.centralwidget)
        self.btn_logs.setObjectName(u"btn_logs")
        self.btn_logs.setGeometry(QRect(20, 190, 81, 24))
        self.btn_logs.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(255, 255, 255);")
        self.btn_led = QPushButton(self.centralwidget)
        self.btn_led.setObjectName(u"btn_led")
        self.btn_led.setGeometry(QRect(110, 340, 75, 24))
        self.led_joy_trig_status = QFrame(self.centralwidget)
        self.led_joy_trig_status.setObjectName(u"led_joy_trig_status")
        self.led_joy_trig_status.setGeometry(QRect(300, 200, 16, 16))
        self.led_joy_trig_status.setMinimumSize(QSize(14, 14))
        self.led_joy_trig_status.setMaximumSize(QSize(16, 16))
        self.led_joy_trig_status.setStyleSheet(u"background-color: rgb(85, 255, 0);\n"
"border-radius: 8px;\n"
"")
        self.led_joy_trig_status.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.led_joy_trig_status.setFrameShape(QFrame.StyledPanel)
        self.led_joy_trig_status.setFrameShadow(QFrame.Raised)
        self.lbl_led_status = QLabel(self.centralwidget)
        self.lbl_led_status.setObjectName(u"lbl_led_status")
        self.lbl_led_status.setGeometry(QRect(240, 170, 51, 16))
        self.lbl_led_trig_status = QLabel(self.centralwidget)
        self.lbl_led_trig_status.setObjectName(u"lbl_led_trig_status")
        self.lbl_led_trig_status.setGeometry(QRect(240, 200, 61, 16))
        self.lbl_x = QLabel(self.centralwidget)
        self.lbl_x.setObjectName(u"lbl_x")
        self.lbl_x.setGeometry(QRect(240, 230, 51, 16))
        self.lbl_y = QLabel(self.centralwidget)
        self.lbl_y.setObjectName(u"lbl_y")
        self.lbl_y.setGeometry(QRect(240, 250, 51, 16))
        self.display_x = QLabel(self.centralwidget)
        self.display_x.setObjectName(u"display_x")
        self.display_x.setGeometry(QRect(300, 230, 49, 16))
        self.display_x.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.display_y = QLabel(self.centralwidget)
        self.display_y.setObjectName(u"display_y")
        self.display_y.setGeometry(QRect(300, 250, 49, 16))
        self.display_y.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuAide = QMenu(self.menubar)
        self.menuAide.setObjectName(u"menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())
        self.menuFichier.addAction(self.actionOpenFile)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuit)
        self.menuAide.addAction(self.actionAbout)
        self.menuAide.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.btn_quit.clicked.connect(MainWindow.close)
        self.btn_manual.clicked.connect(MainWindow.manual)
        self.btn_auto.clicked.connect(MainWindow.auto)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ETMI Pilotage", None))
        self.actionOpenFile.setText(QCoreApplication.translate("MainWindow", u"Ouvrir un fichier", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"A propos de...", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.btn_quit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Lancer", None))
        self.btn_manual.setText(QCoreApplication.translate("MainWindow", u"Manuel", None))
        self.btn_auto.setText(QCoreApplication.translate("MainWindow", u"Automatique", None))
        self.btn_parameters.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.btn_logs.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.btn_led.setText(QCoreApplication.translate("MainWindow", u"Voyant", None))
        self.lbl_led_status.setText(QCoreApplication.translate("MainWindow", u"Joystick", None))
        self.lbl_led_trig_status.setText(QCoreApplication.translate("MainWindow", u"Gachette", None))
        self.lbl_x.setText(QCoreApplication.translate("MainWindow", u"Coord. X", None))
        self.lbl_y.setText(QCoreApplication.translate("MainWindow", u"Coord. Y", None))
        self.display_x.setText("")
        self.display_y.setText("")
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

