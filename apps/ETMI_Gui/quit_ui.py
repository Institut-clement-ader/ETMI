# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quit.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)

class Ui_Dialog_Quit(object):
    def setupUi(self, Dialog_Quit):
        if not Dialog_Quit.objectName():
            Dialog_Quit.setObjectName(u"Dialog_Quit")
        Dialog_Quit.setWindowModality(Qt.NonModal)
        Dialog_Quit.resize(181, 89)
        Dialog_Quit.setLocale(QLocale(QLocale.French, QLocale.France))
        self.btn_quit = QDialogButtonBox(Dialog_Quit)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setGeometry(QRect(-20, 50, 221, 32))
        self.btn_quit.setCursor(QCursor(Qt.WaitCursor))
        self.btn_quit.setToolTipDuration(-3)
        self.btn_quit.setLocale(QLocale(QLocale.French, QLocale.France))
        self.btn_quit.setOrientation(Qt.Horizontal)
        self.btn_quit.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)
        self.btn_quit.setCenterButtons(True)
        self.lbl_quit = QLabel(Dialog_Quit)
        self.lbl_quit.setObjectName(u"lbl_quit")
        self.lbl_quit.setGeometry(QRect(30, 20, 131, 16))

        self.retranslateUi(Dialog_Quit)
        self.btn_quit.accepted.connect(Dialog_Quit.accept)
        self.btn_quit.rejected.connect(Dialog_Quit.reject)

        QMetaObject.connectSlotsByName(Dialog_Quit)
    # setupUi

    def retranslateUi(self, Dialog_Quit):
        Dialog_Quit.setWindowTitle(QCoreApplication.translate("Dialog_Quit", u"Fermeture", None))
        self.lbl_quit.setText(QCoreApplication.translate("Dialog_Quit", u"Voulez-vous quitter ?", None))
    # retranslateUi

