# -*- coding: utf-8 -*-
import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QDialog,
    QPushButton,
    QLabel,
    QFrame,
)
from PySide6.QtCore import QFile, Slot
from ui_etmi_ui import Ui_MainWindow
from quit_ui import Ui_Dialog_Quit
from color import *
from components import Led


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnRun.clicked.connect(self.lancer)
        self.ui.btn_led.clicked.connect(self.btn_led_clicked)
        # self.ui.btnQuit.clicked.connect(self.quit)
        # self.ui.actionQuit.triggered.connect(self.quit)
        self.led_joy_status = Led(self.ui.led_joy_status)

    @Slot()
    def lancer(self):
        # self.ui.ShowText.appendPlainText(self.ui.lineEdit.text())
        # self.ui.ShowText.appendPlainText('coool')
        print("")

    @Slot()
    def btn_led_clicked(self):
        self.led_joy_status.enabled = not self.led_joy_status.enabled
        self.led_joy_status.update()

    def closeEvent(self, eventQCloseEvent):
        dlb = QuitDlg()
        reply = dlb.exec()
        if reply == QDialog.DialogCode.Accepted:
            eventQCloseEvent.accept()
        else:
            eventQCloseEvent.ignore()


class QuitDlg(QDialog):
    def __init__(self, parent=None):
        super(QuitDlg, self).__init__(parent)
        self.ui = Ui_Dialog_Quit()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(Path("./styles.css").read_text())
    window = MainWindow()

    window.show()

    sys.exit(app.exec())
