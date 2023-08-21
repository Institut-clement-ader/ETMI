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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QToolBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 600)
        MainWindow.setToolTipDuration(5)
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
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 80, 101, 176))
        self.layout_menu_left = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_menu_left.setObjectName(u"layout_menu_left")
        self.layout_menu_left.setContentsMargins(0, 0, 0, 0)
        self.btn_auto = QPushButton(self.verticalLayoutWidget)
        self.btn_auto.setObjectName(u"btn_auto")
        self.btn_auto.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(255, 255, 255);")

        self.layout_menu_left.addWidget(self.btn_auto)

        self.btn_parameters = QPushButton(self.verticalLayoutWidget)
        self.btn_parameters.setObjectName(u"btn_parameters")
        self.btn_parameters.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(255, 255, 255);")

        self.layout_menu_left.addWidget(self.btn_parameters)

        self.btn_manual = QPushButton(self.verticalLayoutWidget)
        self.btn_manual.setObjectName(u"btn_manual")
        self.btn_manual.setStyleSheet(u"background-color: rgb(23, 227, 0);\n"
"")

        self.layout_menu_left.addWidget(self.btn_manual)

        self.btn_logs = QPushButton(self.verticalLayoutWidget)
        self.btn_logs.setObjectName(u"btn_logs")
        self.btn_logs.setStyleSheet(u"background-color: rgb(69, 69, 69);\n"
"color: rgb(255, 255, 255);")

        self.layout_menu_left.addWidget(self.btn_logs)

        self.btn_run = QPushButton(self.verticalLayoutWidget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setFocusPolicy(Qt.NoFocus)

        self.layout_menu_left.addWidget(self.btn_run)

        self.btn_quit = QPushButton(self.verticalLayoutWidget)
        self.btn_quit.setObjectName(u"btn_quit")

        self.layout_menu_left.addWidget(self.btn_quit)

        self.frm_manual = QFrame(self.centralwidget)
        self.frm_manual.setObjectName(u"frm_manual")
        self.frm_manual.setGeometry(QRect(100, 20, 701, 351))
        self.frm_manual.setFrameShape(QFrame.StyledPanel)
        self.frm_manual.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frm_manual)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(550, 60, 91, 84))
        self.formLayout = QFormLayout(self.gridLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_led_status = QLabel(self.gridLayoutWidget)
        self.lbl_led_status.setObjectName(u"lbl_led_status")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_led_status)

        self.lbl_led_trig_status = QLabel(self.gridLayoutWidget)
        self.lbl_led_trig_status.setObjectName(u"lbl_led_trig_status")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_led_trig_status)

        self.lbl_x = QLabel(self.gridLayoutWidget)
        self.lbl_x.setObjectName(u"lbl_x")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_x)

        self.display_x = QLabel(self.gridLayoutWidget)
        self.display_x.setObjectName(u"display_x")
        self.display_x.setBaseSize(QSize(0, 0))
        self.display_x.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.display_x)

        self.lbl_y = QLabel(self.gridLayoutWidget)
        self.lbl_y.setObjectName(u"lbl_y")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_y)

        self.display_y = QLabel(self.gridLayoutWidget)
        self.display_y.setObjectName(u"display_y")
        self.display_y.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.display_y)

        self.led_joy_status = QFrame(self.gridLayoutWidget)
        self.led_joy_status.setObjectName(u"led_joy_status")
        self.led_joy_status.setMinimumSize(QSize(14, 14))
        self.led_joy_status.setMaximumSize(QSize(15, 15))
        self.led_joy_status.setStyleSheet(u"background-color: rgb(85, 255, 0);\n"
"border-radius: 7px;\n"
"")
        self.led_joy_status.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.led_joy_status.setFrameShape(QFrame.StyledPanel)
        self.led_joy_status.setFrameShadow(QFrame.Plain)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.led_joy_status)

        self.led_joy_trig_status = QFrame(self.gridLayoutWidget)
        self.led_joy_trig_status.setObjectName(u"led_joy_trig_status")
        self.led_joy_trig_status.setMaximumSize(QSize(15, 15))
        self.led_joy_trig_status.setStyleSheet(u"background-color: rgb(85, 255, 0);\n"
"border-radius: 8px;\n"
"")
        self.led_joy_trig_status.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.led_joy_trig_status.setFrameShape(QFrame.StyledPanel)
        self.led_joy_trig_status.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.led_joy_trig_status)

        self.gridLayoutWidget_2 = QWidget(self.frm_manual)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(240, 170, 101, 151))
        self.grid_layout_btn_dir = QGridLayout(self.gridLayoutWidget_2)
        self.grid_layout_btn_dir.setObjectName(u"grid_layout_btn_dir")
        self.grid_layout_btn_dir.setContentsMargins(0, 0, 0, 0)
        self.btn_left_2 = QToolButton(self.gridLayoutWidget_2)
        self.btn_left_2.setObjectName(u"btn_left_2")
        self.btn_left_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"images/svg/chevron-circle-left-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left_2.setIcon(icon)
        self.btn_left_2.setIconSize(QSize(25, 25))
        self.btn_left_2.setCheckable(False)

        self.grid_layout_btn_dir.addWidget(self.btn_left_2, 1, 0, 1, 1)

        self.btn_right_2 = QToolButton(self.gridLayoutWidget_2)
        self.btn_right_2.setObjectName(u"btn_right_2")
        self.btn_right_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"images/svg/chevron-circle-right-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_right_2.setIcon(icon1)
        self.btn_right_2.setIconSize(QSize(25, 25))
        self.btn_right_2.setCheckable(False)

        self.grid_layout_btn_dir.addWidget(self.btn_right_2, 1, 1, 1, 1)

        self.btn_left_3 = QToolButton(self.gridLayoutWidget_2)
        self.btn_left_3.setObjectName(u"btn_left_3")
        self.btn_left_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_left_3.setIcon(icon)
        self.btn_left_3.setIconSize(QSize(25, 25))
        self.btn_left_3.setCheckable(False)

        self.grid_layout_btn_dir.addWidget(self.btn_left_3, 2, 0, 1, 1)

        self.btn_right_1 = QToolButton(self.gridLayoutWidget_2)
        self.btn_right_1.setObjectName(u"btn_right_1")
        self.btn_right_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_right_1.setIcon(icon1)
        self.btn_right_1.setIconSize(QSize(25, 25))
        self.btn_right_1.setCheckable(False)

        self.grid_layout_btn_dir.addWidget(self.btn_right_1, 0, 1, 1, 1)

        self.btn_right_3 = QToolButton(self.gridLayoutWidget_2)
        self.btn_right_3.setObjectName(u"btn_right_3")
        self.btn_right_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_right_3.setIcon(icon1)
        self.btn_right_3.setIconSize(QSize(25, 25))
        self.btn_right_3.setCheckable(False)

        self.grid_layout_btn_dir.addWidget(self.btn_right_3, 2, 1, 1, 1)

        self.btn_left_1 = QToolButton(self.gridLayoutWidget_2)
        self.btn_left_1.setObjectName(u"btn_left_1")
        self.btn_left_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_left_1.setIcon(icon)
        self.btn_left_1.setIconSize(QSize(25, 25))
        self.btn_left_1.setCheckable(False)

        self.grid_layout_btn_dir.addWidget(self.btn_left_1, 0, 0, 1, 1)

        self.btn_left_4 = QToolButton(self.gridLayoutWidget_2)
        self.btn_left_4.setObjectName(u"btn_left_4")
        self.btn_left_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_left_4.setIcon(icon)
        self.btn_left_4.setIconSize(QSize(25, 25))
        self.btn_left_4.setCheckable(False)

        self.grid_layout_btn_dir.addWidget(self.btn_left_4, 3, 0, 1, 1)

        self.btn_right_4 = QToolButton(self.gridLayoutWidget_2)
        self.btn_right_4.setObjectName(u"btn_right_4")
        self.btn_right_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_right_4.setIcon(icon1)
        self.btn_right_4.setIconSize(QSize(25, 25))
        self.btn_right_4.setCheckable(False)

        self.grid_layout_btn_dir.addWidget(self.btn_right_4, 3, 1, 1, 1)

        self.verticalLayoutWidget_2 = QWidget(self.frm_manual)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(550, 170, 71, 100))
        self.layout_choice_drive = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_choice_drive.setObjectName(u"layout_choice_drive")
        self.layout_choice_drive.setContentsMargins(0, 0, 0, 0)
        self.chk_drive1 = QCheckBox(self.verticalLayoutWidget_2)
        self.chk_drive1.setObjectName(u"chk_drive1")

        self.layout_choice_drive.addWidget(self.chk_drive1)

        self.chk_drive2 = QCheckBox(self.verticalLayoutWidget_2)
        self.chk_drive2.setObjectName(u"chk_drive2")

        self.layout_choice_drive.addWidget(self.chk_drive2)

        self.chk_drive3 = QCheckBox(self.verticalLayoutWidget_2)
        self.chk_drive3.setObjectName(u"chk_drive3")

        self.layout_choice_drive.addWidget(self.chk_drive3)

        self.chk_drive4 = QCheckBox(self.verticalLayoutWidget_2)
        self.chk_drive4.setObjectName(u"chk_drive4")

        self.layout_choice_drive.addWidget(self.chk_drive4)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(100, 0, 701, 34))
        self.layout_display_up = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_display_up.setObjectName(u"layout_display_up")
        self.layout_display_up.setContentsMargins(0, 0, 0, 0)
        self.lbl_drive1 = QLabel(self.horizontalLayoutWidget)
        self.lbl_drive1.setObjectName(u"lbl_drive1")

        self.layout_display_up.addWidget(self.lbl_drive1)

        self.txt_drive1 = QLabel(self.horizontalLayoutWidget)
        self.txt_drive1.setObjectName(u"txt_drive1")
        self.txt_drive1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.layout_display_up.addWidget(self.txt_drive1)

        self.lbl_drive2 = QLabel(self.horizontalLayoutWidget)
        self.lbl_drive2.setObjectName(u"lbl_drive2")

        self.layout_display_up.addWidget(self.lbl_drive2)

        self.txt_drive2 = QLabel(self.horizontalLayoutWidget)
        self.txt_drive2.setObjectName(u"txt_drive2")
        self.txt_drive2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.layout_display_up.addWidget(self.txt_drive2)

        self.lbl_drive3 = QLabel(self.horizontalLayoutWidget)
        self.lbl_drive3.setObjectName(u"lbl_drive3")

        self.layout_display_up.addWidget(self.lbl_drive3)

        self.txt_drive3 = QLabel(self.horizontalLayoutWidget)
        self.txt_drive3.setObjectName(u"txt_drive3")
        self.txt_drive3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.layout_display_up.addWidget(self.txt_drive3)

        self.lbl_drive4 = QLabel(self.horizontalLayoutWidget)
        self.lbl_drive4.setObjectName(u"lbl_drive4")

        self.layout_display_up.addWidget(self.lbl_drive4)

        self.txt_drive4 = QLabel(self.horizontalLayoutWidget)
        self.txt_drive4.setObjectName(u"txt_drive4")
        self.txt_drive4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.layout_display_up.addWidget(self.txt_drive4)

        self.txt_logs = QTextEdit(self.centralwidget)
        self.txt_logs.setObjectName(u"txt_logs")
        self.txt_logs.setGeometry(QRect(100, 460, 701, 71))
        self.txt_logs.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 845, 22))
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
        QWidget.setTabOrder(self.btn_quit, self.btn_logs)
        QWidget.setTabOrder(self.btn_logs, self.btn_manual)
        QWidget.setTabOrder(self.btn_manual, self.btn_parameters)
        QWidget.setTabOrder(self.btn_parameters, self.btn_auto)
        QWidget.setTabOrder(self.btn_auto, self.chk_drive1)
        QWidget.setTabOrder(self.chk_drive1, self.chk_drive2)
        QWidget.setTabOrder(self.chk_drive2, self.chk_drive3)
        QWidget.setTabOrder(self.chk_drive3, self.chk_drive4)
        QWidget.setTabOrder(self.chk_drive4, self.btn_left_1)
        QWidget.setTabOrder(self.btn_left_1, self.btn_right_1)
        QWidget.setTabOrder(self.btn_right_1, self.btn_left_2)
        QWidget.setTabOrder(self.btn_left_2, self.btn_right_2)
        QWidget.setTabOrder(self.btn_right_2, self.btn_left_3)
        QWidget.setTabOrder(self.btn_left_3, self.btn_right_3)
        QWidget.setTabOrder(self.btn_right_3, self.btn_left_4)
        QWidget.setTabOrder(self.btn_left_4, self.btn_right_4)

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
        self.chk_drive4.stateChanged.connect(MainWindow.checked_drives)
        self.chk_drive2.stateChanged.connect(MainWindow.checked_drives)
        self.chk_drive1.stateChanged.connect(MainWindow.checked_drives)
        self.chk_drive3.stateChanged.connect(MainWindow.checked_drives)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ETMI Pilotage", None))
        self.actionOpenFile.setText(QCoreApplication.translate("MainWindow", u"Ouvrir un fichier", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"A propos de...", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.btn_auto.setText(QCoreApplication.translate("MainWindow", u"Automatique", None))
        self.btn_parameters.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.btn_manual.setText(QCoreApplication.translate("MainWindow", u"Manuel", None))
        self.btn_logs.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Lancer", None))
        self.btn_quit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.lbl_led_status.setText(QCoreApplication.translate("MainWindow", u"Joystick", None))
        self.lbl_led_trig_status.setText(QCoreApplication.translate("MainWindow", u"Gachette", None))
        self.lbl_x.setText(QCoreApplication.translate("MainWindow", u"Coord. X", None))
        self.display_x.setText("")
        self.lbl_y.setText(QCoreApplication.translate("MainWindow", u"Coord. Y", None))
        self.display_y.setText("")
        self.btn_left_2.setText("")
        self.btn_right_2.setText("")
        self.btn_left_3.setText("")
        self.btn_right_1.setText("")
        self.btn_right_3.setText("")
        self.btn_left_1.setText("")
        self.btn_left_4.setText("")
        self.btn_right_4.setText("")
        self.chk_drive1.setText(QCoreApplication.translate("MainWindow", u"Drive 1", None))
        self.chk_drive2.setText(QCoreApplication.translate("MainWindow", u"Drive 2", None))
        self.chk_drive3.setText(QCoreApplication.translate("MainWindow", u"Drive 3", None))
        self.chk_drive4.setText(QCoreApplication.translate("MainWindow", u"Drive 4", None))
        self.lbl_drive1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:700;\">Drive 1</span></p></body></html>", None))
        self.txt_drive1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lbl_drive2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:700;\">Drive 2</span></p></body></html>", None))
        self.txt_drive2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lbl_drive3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:700;\">Drive 3</span></p></body></html>", None))
        self.txt_drive3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lbl_drive4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:700;\">Drive 4</span></p></body></html>", None))
        self.txt_drive4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

