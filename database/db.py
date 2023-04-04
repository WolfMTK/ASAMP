from typing import List, Tuple, Any
from sqlite3 import Connection, Cursor

from ._decorators import open_database


class Database:
    def __init__(self, sql: str | None = None) -> None:
        self.__sql_path = sql

    @open_database
    def create_table(self, connect: Connection, cursor: Cursor) -> None:
        if self.__sql_path:
            sql = self.__open_file()
            cursor.executescript(sql)
            connect.commit()

    @open_database
    def get_data(
        self, connect: Connection, cursor: Cursor, **kwargs
    ) -> List[str]:
        if self.__sql_path:
            sql = self.__open_file()
            cursor.execute(sql, kwargs)
            return cursor.fetchall()

    @open_database
    def requests_with_database(
        self,
        connect: Connection,
        cursor: Cursor,
        data: Tuple[Any] = None,
        **kwargs
    ) -> None:
        if self.__sql_path and kwargs or data:
            sql = self.__open_file()
            cursor.executemany(sql, kwargs or data)
        elif self.__sql_path:
            sql = self.__open_file()
            cursor.execute(sql)
        connect.commit()

    def __open_file(self) -> str:
        with open(self.__sql_path, "r") as sql:
            request_sql = sql.read()
            sql.close()
        return request_sql
