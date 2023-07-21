# -*- coding: utf-8 -*-
import sys

sys.path.append("../Pmod_spi")
# import threading
# import asyncio
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
from PySide6.QtCore import QFile, Slot, Signal, QThread
from ui_etmi_ui import Ui_MainWindow
from quit_ui import Ui_Dialog_Quit
from color import *
from components import Led, Label, Text
from pmodJSTK2 import PmodJstk2


class JoyThread(QThread):
    #  """ Create Signal For initialize joy"""
    progress = Signal(bool)

    def __init__(self, joy):
        QThread.__init__(self)
        self.joy = joy

    def run(self):
        self.joy.initialize()
        self.progress.emit(True)  # Send signal.


class ManualThread(QThread):
    #  """ Create Signal For initialize joy"""
    progress = Signal(bool)

    def __init__(self, joy):
        QThread.__init__(self)
        self.joy = joy
        self.isRunning = False

    def run(self):
        self.isRunning = True
        while self.isRunning:
            self.joy.read_data()
            self.progress.emit(True)  # Send signal.

    def stop(self):
        self.isRunning = False
        self.quit()
        self.terminate()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_run.clicked.connect(self.run)
        self.ui.btn_led.clicked.connect(self.btn_led_clicked)
        # self.ui.btnQuit.clicked.connect(self.quit)
        # self.ui.actionQuit.triggered.connect(self.quit)
        self.led_joy_status = Led(self.ui.led_joy_status)
        self.led_joy_trig_status = Led(self.ui.led_joy_trig_status)
        self.text_x = Text(self.ui.display_x)
        self.text_y = Text(self.ui.display_y)
        self.joy = PmodJstk2()
        # thread
        self.th_joy = JoyThread(self.joy)
        self.th_joy.progress.connect(self.update_led_joy_status)
        self.th_joy_manual = ManualThread(self.joy)
        self.th_joy_manual.progress.connect(self.display_joy)

    @Slot()
    def run(self):
        # self.ui.ShowText.appendPlainText(self.ui.lineEdit.text())
        # self.ui.ShowText.appendPlainText('coool')
        # asyncio.run(self.init_joy())
        self.init_joy()

    @Slot()
    def btn_led_clicked(self):
        self.led_joy_status.enabled = not self.led_joy_status.enabled
        self.led_joy_status.update()

    @Slot()
    def manual(self):
        self.th_joy_manual.start()

    @Slot()
    def auto(self):
        self.th_joy_manual.stop()

    def closeEvent(self, eventQCloseEvent):
        dlb = QuitDlg()
        reply = dlb.exec()
        if reply == QDialog.DialogCode.Accepted:
            self.joy.spi_close()
            self.th_joy_manual.stop()
            eventQCloseEvent.accept()
        else:
            eventQCloseEvent.ignore()

    def init_joy(self):
        self.joy.spi_open()
        # thread = threading.Thread(target=self.joy.initialize(), args=())
        # thread.start()
        # thread.join()
        self.th_joy.start()

    def update_led_joy_status(self):
        self.led_joy_status.enabled = True
        self.led_joy_status.update()

    def display_joy(self):
        self.ui.display_x.setText(str(self.joy.x))
        self.ui.display_y.setText(str(self.joy.y))
        self.led_joy_trig_status.enabled = self.joy.trigger_select
        self.led_joy_trig_status.update()


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
