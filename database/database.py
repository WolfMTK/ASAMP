import sqlite3
from typing import List, Tuple


class Database:
    """База данных для приложения."""

    def __init__(self) -> None:
        self.__create_database_with_table()

    @property
    def get_material_with_database(self) -> List[str]:
        """Получить материал с базы данных."""
        request = """SELECT materials.material
                     FROM materials
                     GROUP BY materials.material
                     ORDER BY materials.material"""
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.execute(request)
        list_material = self.__get_list_material(cursor.fetchall())
        connect.close()
        return list_material

    @property
    def get_type_part_with_database(self):
        """Получить класс детали с базы данных."""
        request = """SELECT parts.type_part
                     FROM parts
                     GROUP BY parts.type_part
                     ORDER BY parts.type_part"""
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.execute(request)
        list_type_part = self.__get_list_type_part(cursor.fetchall())
        connect.close()
        return list_type_part

    def get_brand_with_database(self, material: str) -> List[str]:
        """Получить марку материала с базы данных."""
        request = """SELECT materials.brand
                     FROM materials
                     WHERE materials.material=?
                     GROUP BY materials.brand
                     ORDER BY materials.brand"""
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.execute(request, (material, ))
        list_brand = self.__get_list_brand(cursor.fetchall())
        connect.close()
        return list_brand

    @staticmethod
    def __get_list_brand(data: List[Tuple[str]]) -> List[str]:
        return [brand[0] for brand in data]

    @staticmethod
    def __get_list_material(data: List[Tuple[str]]) -> List[str]:
        return [material[0] for material in data]

    @staticmethod
    def __get_list_type_part(data: List[Tuple[str]]) -> List[str]:
        return [type_part[0] for type_part in data]

    @staticmethod
    def __create_database_with_table() -> None:
        request = """CREATE TABLE IF NOT EXISTS materials(id INTEGER,
                                                          brand TEXT,
                                                          material TEXT,
                                                          GOST TEXT,
                                                          PRIMARY KEY(id));
                     CREATE TABLE IF NOT EXISTS parts(id INTEGER,
                                                      type_part TEXT,
                                                      PRIMARY KEY(id))"""
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.executescript(request)
        connect.close()


if __name__ == "__main__":
    print(Database().get_type_part_with_database)
