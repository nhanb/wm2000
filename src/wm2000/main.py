import sys
from pathlib import Path
from typing import Union

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
    Signal,
)
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from wm2000.gui.main_window import Ui_MainWindow
from wm2000.persistence import Database

EXTENSION = ".wm2k"
APP_NAME = "WebMaker2000"


class MainWindow(QMainWindow):
    signalFileChosen = Signal(Path, str)

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
        self.ui.actionSave_As.triggered.connect(self.action_save_as)

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
        self.signalFileChosen.emit(path, "Created")

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
        self.signalFileChosen.emit(path, "Opened")

    def action_save_as(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            caption="Save As",
            filter=f"WebMaker2000 files (*{EXTENSION})",
        )
        if not file_name:
            return

        if not file_name.endswith(EXTENSION):
            file_name += EXTENSION

        path = Path(file_name)
        if path.is_file():
            path.unlink()

        self.app.db.save_as(path)
        del self.app.db
        self.app.db = Database(path, init=False)
        self.signalFileChosen.emit(path, "Saved as")

    def signal_file_chosen(self, path: Path, message: str):
        self.setWindowTitle(f"{path.name} - {APP_NAME}")

        # Enable actions that require a chosen file:
        self.ui.menuExport.setEnabled(True)
        self.ui.menuPublish.setEnabled(True)
        self.ui.actionSave_As.setEnabled(True)

        # Setup index view with proper model
        self.ui.stackedWidget.setCurrentWidget(self.ui.indexView)
        self.ui.pagesTable.setModel(PagesTableModel(self.app.db))

        self.ui.statusbar.showMessage(f"{message} {path}")


class PagesTableModel(QAbstractTableModel):
    db_columns = (
        "id",
        "slug",
        "title",
        "created_at",
        "updated_at",
        "is_draft",
        "show_in_feed",
    )

    def __init__(self, db: Database):
        super().__init__()
        self._db = db
        self._data = []
        self.refresh_data()

    def refresh_data(self):
        pages = self._db.run_sql(
            f"SELECT {', '.join(self.db_columns)}"
            " FROM post"
            " ORDER BY created_at DESC;",
            [],
        )
        print(">> pages:", pages)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(
        self,
        parent: Union[QModelIndex, QPersistentModelIndex] = QModelIndex(),
    ) -> int:
        # The length of the outer list.
        return len(self._data)

    def columnCount(
        self,
        parent: Union[QModelIndex, QPersistentModelIndex] = QModelIndex(),
    ) -> int:
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if rowCount == 0:
            return 0
        return len(self._data[0])


def main():
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    exit(app.exec())
