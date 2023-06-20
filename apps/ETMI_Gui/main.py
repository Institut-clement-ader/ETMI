import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, Slot
from ui_etmi_ui import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Lancer.clicked.connect(self.lancer)
        

    @Slot()
    def lancer(self):
        # self.ui.ShowText.appendPlainText(self.ui.lineEdit.text())
        # self.ui.ShowText.appendPlainText('coool')
        print('')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())