import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QPushButton
from PySide6.QtCore import QFile, Slot
from ui_etmi_ui import Ui_MainWindow
from quit_ui import Ui_Dialog_Quit


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnRun.clicked.connect(self.lancer)
        # self.ui.btnQuit.clicked.connect(self.quit)
        # self.ui.actionQuit.triggered.connect(self.quit)

    @Slot()
    def lancer(self):
        # self.ui.ShowText.appendPlainText(self.ui.lineEdit.text())
        # self.ui.ShowText.appendPlainText('coool')
        print('')

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

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
