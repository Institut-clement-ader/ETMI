# -*- coding: utf-8 -*-
import sys
import os
import datetime

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

# import threading
# import asyncio
sys.path.append("../Pmod_spi")
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
from components_ui import Led, Label, Text
from Pmod_spi.pmodJSTK2 import PmodJstk2
from drives import Drive, ManageDrives, config, DIR_POSITIF, DIR_NEGATIF

test = True
path_css = "./css/styles.css"


class JoyThread(QThread):
    #  """ Create Signal For initialize joy"""
    progress = Signal(bool)

    def __init__(self, joy):
        QThread.__init__(self)
        self.joy = joy
        self.is_running = False

    def run(self):
        self.joy.initialize()
        self.progress.emit(True)  # Send signal.


class ManualThread(QThread):
    #  """ Create Signal For initialize joy"""
    progress = Signal(bool)

    def __init__(self, joy):
        QThread.__init__(self)
        self.joy = joy
        # # self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            self.joy.read_data()
            self.progress.emit(True)  # Send signal.

    def stop(self):
        # # self.is_running = False
        self.quit()
        self.terminate()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_run.clicked.connect(self.run)
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
        self.init_joy()
        # drives
        self.manage_drives = ManageDrives()
        self.checked_drives()

    @Slot()
    def run(self):
        # self.ui.ShowText.appendPlainText(self.ui.lineEdit.text())
        # self.ui.ShowText.appendPlainText('coool')
        # asyncio.run(self.init_joy())
        self.init_joy()

    @Slot()
    def btn_led_clicked(self):
        self.led_joy_status.enabled = not self.led_joy_status.enabled
        # self.led_joy_status.update()

    @Slot()
    def manual(self):
        self.th_joy_manual.start()

    @Slot()
    def auto(self):
        self.th_joy_manual.stop()

    @Slot()
    def checked_drives(self):
        self.ui.btn_left_1.setEnabled(self.ui.chk_drive1.isChecked())
        self.ui.btn_left_2.setEnabled(self.ui.chk_drive2.isChecked())
        self.ui.btn_left_3.setEnabled(self.ui.chk_drive3.isChecked())
        self.ui.btn_left_4.setEnabled(self.ui.chk_drive4.isChecked())
        self.ui.btn_right_1.setEnabled(self.ui.chk_drive1.isChecked())
        self.ui.btn_right_2.setEnabled(self.ui.chk_drive2.isChecked())
        self.ui.btn_right_3.setEnabled(self.ui.chk_drive3.isChecked())
        self.ui.btn_right_4.setEnabled(self.ui.chk_drive4.isChecked())
        # if self.ui.chk_drive1.isChecked():
        #     self.manage_drives.drives[0].start()
        # else:
        #     self.manage_drives.drives[0].stop()
        # if self.ui.chk_drive2.isChecked():
        #     self.manage_drives.drives[1].start()
        # else:
        #     self.manage_drives.drives[1].stop()
        # if self.ui.chk_drive3.isChecked():
        #     self.manage_drives.drives[2].start()
        # else:
        #     self.manage_drives.drives[2].stop()
        # if self.ui.chk_drive4.isChecked():
        #     self.manage_drives.drives[3].start()
        # else:
        #     self.manage_drives.drives[3].stop()

    @Slot()
    def action_drives(self):
        if self.ui.btn_left_1.isDown():
            self.manage_drives.drives[0].start(DIR_POSITIF)
        elif self.ui.btn_right_1.isDown():
            self.manage_drives.drives[0].start(DIR_NEGATIF)
        else:
            self.manage_drives.drives[0].stop()

        if self.ui.btn_left_2.isDown():
            self.manage_drives.drives[1].start(DIR_POSITIF)
        elif self.ui.btn_right_2.isDown():
            self.manage_drives.drives[1].start(DIR_NEGATIF)
        else:
            self.manage_drives.drives[1].stop()

        if self.ui.btn_left_3.isDown():
            self.manage_drives.drives[2].start(DIR_POSITIF)
        elif self.ui.btn_right_3.isDown():
            self.manage_drives.drives[2].start(DIR_NEGATIF)
        else:
            self.manage_drives.drives[2].stop()

        if self.ui.btn_left_4.isDown():
            self.manage_drives.drives[3].start(DIR_POSITIF)
        elif self.ui.btn_right_4.isDown():
            self.manage_drives.drives[3].start(DIR_NEGATIF)
        else:
            self.manage_drives.drives[3].stop()

    def closeEvent(self, eventQCloseEvent):
        dlb = QuitDlg()
        reply = dlb.exec()
        if reply == QDialog.DialogCode.Accepted:
            self.joy.spi_close()
            self.th_joy_manual.stop()
            self.manage_drives.gpio_clean()
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

    def add_log(self, text):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.txt_logs.append(str(now) + ": " + text)


class QuitDlg(QDialog):
    def __init__(self, parent=None):
        super(QuitDlg, self).__init__(parent)
        self.ui = Ui_Dialog_Quit()
        self.ui.setupUi(self)


if __name__ == "__main__":
    config()
    app = QApplication(sys.argv)
    app.setStyleSheet(Path(path_css).read_text())
    window = MainWindow()

    window.show()

    sys.exit(app.exec())
