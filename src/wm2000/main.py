from PySide6 import QtWidgets as qtw
import sys

from wm2000.gui.main_window import Ui_MainWindow


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
