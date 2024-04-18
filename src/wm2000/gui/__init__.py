from pathlib import Path
import sys

from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore as qtc


def load(filename: str, parent):
    full_path = Path(__file__).parent / filename
    ui_file = qtc.QFile(full_path)
    if not ui_file.open(qtc.QIODevice.ReadOnly):
        print(f"Cannot open {full_path}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    result = loader.load(ui_file, parent)
    ui_file.close()
    return result
