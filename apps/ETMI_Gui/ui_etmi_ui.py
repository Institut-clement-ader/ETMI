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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QWidget)

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
        self.btnQuit = QPushButton(self.centralwidget)
        self.btnQuit.setObjectName(u"btnQuit")
        self.btnQuit.setGeometry(QRect(710, 520, 75, 24))
        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(710, 480, 75, 24))
        self.btnRun.setFocusPolicy(Qt.NoFocus)
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
        self.btnQuit.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ETMI Pilotage", None))
        self.actionOpenFile.setText(QCoreApplication.translate("MainWindow", u"Ouvrir un fichier", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"A propos de...", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"Lancer", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

