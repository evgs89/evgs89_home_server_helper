import sqlite3

class DB:
    def __init__(self):
        self._db = sqlite3.connect('db.sql')

    def