import sqlite3
from typing import List, Tuple, Any
from sqlite3 import Connection, Cursor


class Database:
    """База данных для приложения."""

    def __init__(self) -> None:
        self.__create_database_with_table()

    @property
    def get_material_with_database(self) -> List[str]:
        """Получить материал с базы данных."""
        sql = """SELECT materials.material
                     FROM materials
                     GROUP BY materials.material
                     ORDER BY materials.material"""
        connect, cursor = self.__get_data_with_database(sql)
        list_materials = [material[0] for material in cursor.fetchall()]
        connect.close()
        return list_materials

    @property
    def get_type_part_with_database(self):
        """Получить класс детали с базы данных."""
        sql = """SELECT parts.type_part
                 FROM parts
                 GROUP BY parts.type_part
                 ORDER BY parts.type_part"""
        connect, cursor = self.__get_data_with_database(sql)
        list_type_parts = [type_part[0] for type_part in cursor.fetchall()]
        connect.close()
        return list_type_parts

    def get_brand_with_database(self, material: str) -> List[str]:
        """Получить марку материала с базы данных."""
        sql = """SELECT materials.brand
                 FROM materials
                 WHERE materials.material=?
                 GROUP BY materials.brand
                 ORDER BY materials.brand"""
        connect, cursor = self.__get_data_with_database(sql, (material,))
        list_brands = [brand[0] for brand in cursor.fetchall()]
        connect.close()
        return list_brands

    def get_parameters_with_database(self, type_part: str) -> List[str]:
        """Получить параметры с базы данных."""
        sql = """SELECT parameters.parameter
                 FROM parameters
                 JOIN parts on parts.id = parameters.id_part
                 WHERE parts.type_part = ?"""
        connect, cursor = self.__get_data_with_database(sql, (type_part,))
        list_parameters = [parameter[0] for parameter in cursor.fetchall()]
        connect.close()
        return list_parameters

    def add_data_in_material_pattern(self) -> None:
        """Добавление данных в таблицу material_pattern."""
        list_id = []
        for id_material in self.__get_id_materials():
            for id_pattern in self.__get_id_patterns():
                list_id.append((id_material, id_pattern))
        self.__add_data_in_material_pattern(list_id)

    def __get_id_materials(self):
        sql = """SELECT materials.id
                 FROM materials"""
        connect, cursor = self.__get_data_with_database(sql)
        list_materials_id = [
            id_material[0] for id_material in cursor.fetchall()
        ]
        connect.close()
        return list_materials_id

    def __get_id_patterns(self):
        sql = """SELECT patterns.id
                 FROM patterns"""
        connect, cursor = self.__get_data_with_database(sql)
        list_patterns_id = [id_pattern[0] for id_pattern in cursor.fetchall()]
        connect.close()
        return list_patterns_id

    def __add_data_in_material_pattern(self,
                                       id_list: Tuple[List[str]]) -> None:
        sql = """INSERT INTO material_pattern VALUES (?, ?)"""
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.executemany(sql, id_list)
        connect.commit()
        self.__delete_duplicate_in_material_pattern()

    def __delete_duplicate_in_material_pattern(self):
        """Удалить дубликаты в material part"""
        sql = """DELETE FROM material_pattern
                 WHERE ROWID NOT IN
                 (SELECT ROWID 
                  FROM material_pattern GROUP BY id_material, 
                                                 id_pattern);"""
        connect, cursor = self.__get_data_with_database(sql)
        connect.commit()
        connect.close()

    @staticmethod
    def __create_database_with_table() -> None:
        request = (
            """
            CREATE TABLE IF NOT EXISTS materials(id INTEGER,
                                                 brand TEXT,
                                                 material TEXT,
                                                 GOST TEXT,
                                                 PRIMARY KEY (id));
            CREATE TABLE IF NOT EXISTS parts(id INTEGER,
                                             type_part TEXT,
                                             PRIMARY KEY (id));
            CREATE TABLE IF NOT EXISTS parameters(id INTEGER,
                                                  id_part INTEGER,
                                                  parameter TEXT,
                                                  PRIMARY KEY (id),
                                                  FOREIGN KEY (id_part) REFERENCES parts (id));
            CREATE TABLE IF NOT EXISTS patterns(id INTEGER,
                                                id_part INTEGER,
                                                id_parameter INTEGER,
                                                pattern TEXT,
                                                connect_text TEXT,
                                                PRIMARY KEY (id),
                                                FOREIGN KEY (id_part) REFERENCES parts (id),
                                                FOREIGN KEY (id_parameter) REFERENCES parameters (id));
            CREATE TABLE IF NOT EXISTS material_pattern(id_material INTEGER,
                                                        id_pattern INTEGER,
                                                        FOREIGN KEY (id_material) REFERENCES materials (id),
                                                        FOREIGN KEY (id_pattern) REFERENCES patterns (id));
            """
        )
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.executescript(request)
        connect.close()

    @staticmethod
    def __get_data_with_database(
            sql: str,
            data: Any = None
    ) -> Tuple[Connection, Cursor]:
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        if data:
            return connect, cursor.execute(sql, data)
        return connect, cursor.execute(sql)


def delete_duplicate_data() -> None:
    with open('scripts/delete_duplicate.sql') as file:
        request = file.read()
    connect = sqlite3.connect("database.sqlite")
    cursor = connect.cursor()
    cursor.executescript(request)
    file.close()
    connect.close()


if __name__ == "__main__":
    print(Database().get_parameters_with_database('Вал'))
