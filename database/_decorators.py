import sqlite3


def open_database(function):
    def _inner(self, *args, **kwargs):
        connect = sqlite3.connect("db.sqlite3")
        cursor = connect.cursor()
        returned_function = function(self, connect, cursor, *args, **kwargs)
        cursor.close()
        connect.close()
        return returned_function

    return _inner
