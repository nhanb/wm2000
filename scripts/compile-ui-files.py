#!/usr/bin/env python
import os
import subprocess
from pathlib import Path
from time import perf_counter


def run(*cmd):
    return subprocess.run(cmd, check=True, capture_output=True).stdout


os.chdir("src/wm2000/gui/")

for ui_file_path in Path(".").glob("*.ui"):
    start = perf_counter()

    py_code = run("/usr/lib/qt6/uic", "-g", "python", ui_file_path)
    py_file_path = ui_file_path.stem + ".py"
    Path(py_file_path).write_bytes(py_code)

    miliseconds = int((perf_counter() - start) * 1000)
    print(f"Wrote {py_file_path} (took {miliseconds}ms)")
