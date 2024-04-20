import sys
from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from wm2000.gui.main_window import Ui_MainWindow
from wm2000.persistence import Database

EXTENSION = ".wm2k"
APP_NAME = "WebMaker2000"


class MainWindow(QMainWindow):
    signalFileChosen = Signal(Path)

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(APP_NAME)

        self.setup_shortcuts()

        # Actions
        self.ui.actionQuit.triggered.connect(self.action_quit)
        self.ui.actionNew.triggered.connect(self.action_new)
        self.ui.actionOpen.triggered.connect(self.action_open)

        # Custom signals
        self.signalFileChosen.connect(self.signal_file_chosen)

    def setup_shortcuts(self):
        # Since Qt6 Designer doesn't support using StandardKey sequences,
        # let's set them up here.
        self.ui.actionNew.setShortcut(QKeySequence.StandardKey.New)
        self.ui.actionOpen.setShortcut(QKeySequence.StandardKey.Open)
        self.ui.actionSave_As.setShortcut(QKeySequence.StandardKey.SaveAs)
        self.ui.actionQuit.setShortcut(QKeySequence.StandardKey.Quit)

    def action_quit(self):
        msgbox = QMessageBox(self)
        msgbox.setIcon(QMessageBox.Icon.Warning)
        msgbox.setWindowTitle("Quitting")
        msgbox.setText("Are you sure you want to quit?")
        msgbox.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        result = msgbox.exec()
        if result == QMessageBox.StandardButton.Ok:
            self.app.quit()
        self.ui.statusbar.showMessage("Quit cancelled.")

    def action_new(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            caption="New File",
            filter=f"WebMaker2000 files (*{EXTENSION})",
        )
        if not file_name:
            return

        if not file_name.endswith(EXTENSION):
            file_name += EXTENSION

        path = Path(file_name)
        if path.is_file():
            path.unlink()

        self.app.db = Database(path, init=True)
        self.signalFileChosen.emit(path)

    def action_open(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            caption="Open File",
            filter=f"WebMaker2000 files (*{EXTENSION})",
        )
        if not file_name:
            return

        path = Path(file_name)
        self.app.db = Database(path, init=False)
        self.signalFileChosen.emit(path)

    def signal_file_chosen(self, path: Path):
        self.setWindowTitle(f"{path} - {APP_NAME}")

        # Enable actions that require a chosen file:
        self.ui.menuExport.setEnabled(True)
        self.ui.menuPublish.setEnabled(True)
        self.ui.actionSave_As.setEnabled(True)

        self.ui.statusbar.showMessage(f"Chosen file: {path}")


def main():
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    exit(app.exec())
