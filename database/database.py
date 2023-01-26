import sqlite3
from typing import List, Tuple, Any
from sqlite3 import Connection, Cursor


class Database:
    """База данных для приложения."""

    def __init__(self) -> None:
        self.__create_database_with_table()

    @property
    def materials_with_database(self) -> List[str]:
        """Материал с базы данных."""
        sql = """SELECT materials.material
                 FROM materials
                 GROUP BY materials.material
                 ORDER BY materials.material"""
        connect, cursor = self.__get_data_with_database(sql)
        list_materials = [material[0] for material in cursor.fetchall()]
        connect.close()
        return list_materials

    @property
    def type_parts_with_database(self):
        """Классы деталей с базы данных."""
        sql = """SELECT parts.type_part
                 FROM parts
                 GROUP BY parts.type_part
                 ORDER BY parts.type_part"""
        connect, cursor = self.__get_data_with_database(sql)
        list_type_parts = [type_part[0] for type_part in cursor.fetchall()]
        connect.close()
        return list_type_parts

    @property
    def materials_for_database(self) -> List[Tuple[Any]]:
        """Материалы для базы данных."""
        sql = """SELECT * FROM materials"""
        connect, cursor = self.__get_data_with_database(sql)
        list_data = cursor.fetchall()
        connect.close()
        return list_data

    @property
    def parameters_for_database(self) -> List[Tuple[Any]]:
        """Параметры для базы данных."""
        sql = """SELECT * FROM parameters"""
        connect, cursor = self.__get_data_with_database(sql)
        list_data = cursor.fetchall()
        connect.close()
        return list_data

    @property
    def patterns_for_database(self) -> List[Tuple[Any]]:
        """Шаблоны для базы данных."""
        sql = """SELECT * FROM patterns"""
        connect, cursor = self.__get_data_with_database(sql)
        list_data = cursor.fetchall()
        connect.close()
        return list_data

    @property
    def type_parts_for_database(self) -> List[Tuple[Any]]:
        """Классы деталей для базы данных."""
        sql = """SELECT * FROM parts"""
        connect, cursor = self.__get_data_with_database(sql)
        list_data = cursor.fetchall()
        connect.close()
        return list_data

    def get_brand_with_database(self, material: str) -> List[str]:
        """Получить марку материала с базы данных."""
        sql = """SELECT materials.brand
                 FROM materials
                 WHERE materials.material = ?
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
                 JOIN parts ON parts.id = parameters.id_part
                 WHERE parts.type_part = ?"""
        connect, cursor = self.__get_data_with_database(sql, (type_part,))
        list_parameters = [parameter[0] for parameter in cursor.fetchall()]
        connect.close()
        return list_parameters

    def get_material_with_database(self, material: str, brand: str) -> str:
        """Получить материал с базы данных."""
        sql = """SELECT materials.material,
                        materials.brand,
                        materials.GOST
                 FROM materials
                 WHERE materials.material = ? 
                 AND materials.brand = ? """
        connect, cursor = self.__get_data_with_database(sql, (material, brand))
        material = " ".join(cursor.fetchall()[0])
        connect.close()
        return material

    def get_patterns_with_database(
        self, material: str, type_part: str, brand: str
    ) -> List[str]:
        """Получить шаблоны с базы данных."""
        sql = """SELECT patterns.pattern,
                      patterns.connect_text,
                      patterns.id_parameter
               FROM patterns
               JOIN material_pattern mp ON patterns.id = mp.id_pattern
               JOIN materials ON mp.id_material = materials.id
               JOIN parts ON parts.id = patterns.id_part
               JOIN parameters on parameters.id = patterns.id_parameter
               WHERE materials.material = ? 
               AND parts.type_part = ?
               AND materials.brand = ?
               ORDER BY patterns.id"""
        connect, cursor = self.__get_data_with_database(
            sql, (material, type_part, brand)
        )
        list_patterns, list_connect_text, list_id_parameter = [], [], []
        for pattern, connect_text, id_parameter in cursor.fetchall():
            list_patterns.append(pattern)
            list_connect_text.append(connect_text)
            list_id_parameter.append(id_parameter)
        return [list_patterns, list_connect_text, list_id_parameter]

    def get_id_parameters_with_database(self, type_part: str) -> List[int]:
        sql = """SELECT parameters.id
                 FROM parameters
                 JOIN parts ON parts.id = parameters.id_part
                 WHERE parts.type_part = ?"""
        connect, cursor = self.__get_data_with_database(sql, (type_part,))
        list_id_parameters = [
            id_parameters[0] for id_parameters in cursor.fetchall()
        ]
        connect.close()
        return list_id_parameters

    def add_data_in_materials(self, data: Tuple[Any]) -> None:
        """Добавить данные в таблицу materials."""
        self.__delete_data_in_materials()
        sql = """INSERT INTO materials VALUES(null, ?, ?, ?)"""
        connect, cursor = self.__get_many_data_with_database(sql, data)
        self.__commit_and_close(connect)

    def add_data_in_patterns(self, data: Tuple[Any]) -> None:
        """Добавить данные в табллицу patterns."""
        self.__delete_data_in_patterns()
        sql = """INSERT INTO patterns VALUES (null, ?, ?, ?, ?)"""
        connect, cursor = self.__get_many_data_with_database(sql, data)
        self.__commit_and_close(connect)

    def add_data_in_parameters(self, data: Tuple[Any]) -> None:
        """Добавить данные в таблицу parameters."""
        self.__delete_data_in_parameters()
        sql = """INSERT INTO parameters VALUES (null, ?, ?)"""
        connect, cursor = self.__get_many_data_with_database(sql, data)
        self.__commit_and_close(connect)

    def add_data_in_parts(self, data: Tuple[Any]) -> None:
        """Добавить данные в таблицу parts."""
        self.__delete_data_in_parts()
        sql = """INSERT INTO parts VALUES (null, ?)"""
        connect, cursor = self.__get_many_data_with_database(sql, data)
        self.__commit_and_close(connect)

    def add_data_in_material_pattern(self) -> None:
        """Добавление данных в таблицу material_pattern."""
        list_id = []
        for id_material in self.__get_id_materials():
            for id_pattern in self.__get_id_patterns():
                list_id.append((id_material, id_pattern))
        self.__add_data_in_material_pattern(list_id)

    def __delete_data_in_parameters(self) -> None:
        sql = """DELETE FROM parameters 
                 WHERE parameters.parameter IS NOT NULL"""
        connect, cursor = self.__get_data_with_database(sql)
        self.__commit_and_close(connect)

    def __delete_data_in_parts(self):
        sql = """DELETE FROM parts
                 WHERE parts.type_part IS NOT NULL"""
        connect, cursor = self.__get_data_with_database(sql)
        self.__commit_and_close(connect)

    def __get_id_materials(self):
        sql = """SELECT materials.id
                 FROM materials"""
        connect, cursor = self.__get_data_with_database(sql)
        list_materials_id = [
            id_material[0] for id_material in cursor.fetchall()
        ]
        connect.close()
        return list_materials_id

    def __delete_data_in_patterns(self) -> None:
        sql = """DELETE FROM patterns 
                 WHERE patterns.pattern IS NOT NULL"""
        connect, cursor = self.__get_data_with_database(sql)
        self.__commit_and_close(connect)

    def __get_id_patterns(self):
        sql = """SELECT patterns.id
                 FROM patterns"""
        connect, cursor = self.__get_data_with_database(sql)
        list_patterns_id = [id_pattern[0] for id_pattern in cursor.fetchall()]
        connect.close()
        return list_patterns_id

    def __delete_data_in_materials(self) -> None:
        sql = """DELETE FROM materials 
                 WHERE materials.material IS NOT NULL"""
        connect, _ = self.__get_data_with_database(sql)
        self.__commit_and_close(connect)

    def __add_data_in_material_pattern(
        self, id_list: Tuple[List[str]]
    ) -> None:
        self.__delete_data_in_material_pattern()
        sql = """INSERT INTO material_pattern VALUES (?, ?)"""
        connect, cursor = self.__get_many_data_with_database(sql, id_list)
        self.__commit_and_close(connect)
        self.__delete_duplicate_in_material_pattern()

    def __delete_data_in_material_pattern(self) -> None:
        sql = """DELETE FROM material_pattern 
                 WHERE id_material IS NOT NULL"""
        connect, _ = self.__get_data_with_database(sql)
        self.__commit_and_close(connect)

    def __delete_duplicate_in_material_pattern(self) -> None:
        """Удалить дубликаты в material_part"""
        sql = """DELETE FROM material_pattern
                 WHERE ROWID NOT IN
                 (SELECT ROWID 
                  FROM material_pattern GROUP BY id_material,
                                                 id_pattern);"""
        connect, cursor = self.__get_data_with_database(sql)
        self.__commit_and_close(connect)

    @staticmethod
    def __commit_and_close(connect: Connection) -> None:
        connect.commit()
        connect.close()

    @staticmethod
    def __create_database_with_table() -> None:
        request = """
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
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.executescript(request)
        connect.close()

    @staticmethod
    def __get_data_with_database(
        sql: str, data: Any = None
    ) -> Tuple[Connection, Cursor]:
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        if data:
            return connect, cursor.execute(sql, data)
        return connect, cursor.execute(sql)

    @staticmethod
    def __get_many_data_with_database(
        sql: str, data: Any = None
    ) -> Tuple[Connection, Cursor]:
        connect = sqlite3.connect("database.sqlite")
        cursor = connect.cursor()
        cursor.executemany(sql, data)
        return connect, cursor
