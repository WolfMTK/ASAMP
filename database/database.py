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
        list_materials = self.__get_list_materials(cursor.fetchall())
        connect.close()
        return list_materials

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
        list_type_parts = self.__get_list_type_parts(cursor.fetchall())
        connect.close()
        return list_type_parts

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
        list_brands = self.__get_list_brands(cursor.fetchall())
        connect.close()
        return list_brands

    def get_parameters_with_database(self, type_part: str) -> List[str]:
        """Получить параметры с базы данных."""
        request = """SELECT parameters.parameter
                     FROM parameters
                     JOIN parts on parts.id = parameters.id_part
                     WHERE parts.type_part = ?"""
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.execute(request, (type_part, ))
        list_parameters = self.__get_list_parameters(cursor.fetchall())
        connect.close()
        return list_parameters

    @staticmethod
    def __get_list_parameters(data: List[Tuple[str]]) -> List[str]:
        return [parameter[0] for parameter in data]

    @staticmethod
    def __get_list_brands(data: List[Tuple[str]]) -> List[str]:
        return [brand[0] for brand in data]

    @staticmethod
    def __get_list_materials(data: List[Tuple[str]]) -> List[str]:
        return [material[0] for material in data]

    @staticmethod
    def __get_list_type_parts(data: List[Tuple[str]]) -> List[str]:
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
                                                      PRIMARY KEY(id));
                     CREATE TABLE IF NOT EXISTS parameters(
                     id INTEGER,
                     id_part INTEGER,
                     parameter TEXT,
                     PRIMARY KEY(id),
                     FOREIGN KEY(id_part) REFERENCES parts(id)
                     );"""
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.executescript(request)
        connect.close()


if __name__ == "__main__":
    print(Database().get_parameters_with_database('Вал'))
