from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
import sys

from wm2000.gui.main_window import Ui_MainWindow


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_shortcuts()

    def setup_shortcuts(self):
        # Since Qt6 Designer doesn't support using StandardKey sequences,
        # let's set them up here.
        self.ui.actionNew.setShortcut(qtg.QKeySequence.StandardKey.New)
        self.ui.actionOpen.setShortcut(qtg.QKeySequence.StandardKey.Open)
        self.ui.actionSave_As.setShortcut(qtg.QKeySequence.StandardKey.SaveAs)
        self.ui.actionQuit.setShortcut(qtg.QKeySequence.StandardKey.Quit)


def main():
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    exit(app.exec())
