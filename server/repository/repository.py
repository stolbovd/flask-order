import sqlite3


class Repository:
    def get_connect(self):
        return sqlite3.connect("../db/order.sqlite")