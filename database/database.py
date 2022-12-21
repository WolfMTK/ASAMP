import os
import sqlite3
from sqlite3 import Connection, Cursor
from typing import Tuple, Any

from dotenv import load_dotenv, find_dotenv


class Database:
    """База данных."""

    def __init__(self):
        self.sql: str = None

    @property
    def connect(self) -> Tuple[Connection, Cursor]:
        """Подключение базы данных."""
        load_dotenv(find_dotenv())
        try:
            connect = sqlite3.connect(os.getenv('DATABASE'))
            cursor = connect.cursor()
            return connect, cursor
        except sqlite3.OperationalError:
            raise ConnectionError('Подключение к базе данных отстутствует!')


    @property
    def open_sql(self) -> str:
        if self.sql:
            with open(self.sql) as fs:
                return fs.read()

    def close(self) -> None:
        """Закрытие базы данных."""
        connect, cursor = self.connect
        return cursor.close(), connect.close()

    def update(self, sql: str, data: Any) -> None:
        """Обновление базы данных."""
        connect, cursor = self.connect
        if type(data) == tuple:
            for index in range(len(data[0])):
                count = list()
                for value in range(len(data)):
                    count.append(data[value][index])
                cursor.execute(sql, tuple(count))
        else:
            for value in data:
                cursor.execute(sql, (value,))
        connect.commit()
        return self.close()

    def clean_repeat(self, sql: str) -> None:
        """Очистка повторных записей в базе данных."""
        connect, cursor = self.connect
        cursor.execute(sql)
        connect.commit()
        return self.close()

    def delete(self, sql: str, data: str) -> None:
        """Удаление записи с базы данных"""
        connect, cursor = self.connect
        cursor.execute(sql, (data,))
        connect.commit()
        return self.close()
