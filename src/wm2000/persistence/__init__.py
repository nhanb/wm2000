import re
import sqlite3
from importlib.resources import files
from pathlib import Path


class Database:
    def __init__(self, path: Path, *, init: bool):
        self.path: Path = path
        self.conn = sqlite3.connect(path, isolation_level=None)
        self.conn.create_function("REGEXP", 2, regexp)
        self.conn.row_factory = dict_factory
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.conn.execute("PRAGMA busy_timeout = 4000;")

        if init:
            self._init_schema()

    def __del__(self):
        self.conn.close()
        print(f"Closed db {self.path}")

    def _init_schema(self):
        sql = files("wm2000.persistence").joinpath("schema.sql").read_text()
        self.conn.cursor().executescript(sql)
        return self

    def save_as(self, path: Path):
        self.conn.execute("VACUUM INTO ?;", [str(path)])


def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
