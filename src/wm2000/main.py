from PySide6 import QtWidgets as qtw
import sys

from wm2000 import gui


def main():
    app = qtw.QApplication(sys.argv)

    window = gui.load("main_window.ui", None)
    window.show()

    exit(app.exec())
