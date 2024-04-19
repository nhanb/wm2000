from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
import sys

from wm2000.gui.main_window import Ui_MainWindow


class MainWindow(qtw.QMainWindow):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_shortcuts()

        # Actions
        self.ui.actionQuit.triggered.connect(self.action_quit)

    def setup_shortcuts(self):
        # Since Qt6 Designer doesn't support using StandardKey sequences,
        # let's set them up here.
        self.ui.actionNew.setShortcut(qtg.QKeySequence.StandardKey.New)
        self.ui.actionOpen.setShortcut(qtg.QKeySequence.StandardKey.Open)
        self.ui.actionSave_As.setShortcut(qtg.QKeySequence.StandardKey.SaveAs)
        self.ui.actionQuit.setShortcut(qtg.QKeySequence.StandardKey.Quit)

    def action_quit(self):
        msgbox = qtw.QMessageBox(self)
        msgbox.setIcon(qtw.QMessageBox.Icon.Warning)
        msgbox.setWindowTitle("Quitting")
        msgbox.setText("Are you sure you want to quit?")
        msgbox.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        result = msgbox.exec()
        if result == qtw.QMessageBox.Ok:
            self.app.quit()
        self.ui.statusbar.showMessage("Quit cancelled.")


def main():
    app = qtw.QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    exit(app.exec())
