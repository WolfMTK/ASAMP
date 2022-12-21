from typing import Set, List, Tuple

from database.database import Database


class Material(Database):
    def __init__(self, material: str = None) -> None:
        super(Material, self).__init__()
        self.material = material

    @property
    def get_material(self) -> Set[str]:
        """Получение множества из списка материало."""
        cursor, _ = self.connect
        self.sql = 'sql/material.sql'
        res = cursor.execute(self.open_sql)
        material_list: List[str] = [material[0] for material in res.fetchall()]
        self.close()
        return set(material_list)

    @property
    def get_brand(self):
        """Получение списка марки материала."""
        if self.material:
            cursor, _ = self.connect
            self.sql = 'sql/brand.sql'
            res = cursor.execute(self.open_sql, (self.material,))
            brand_list: List[str | int] = [brand[0] for brand in res.fetchall()]
            self.close()
            return brand_list

    @property
    def get_material_and_brand(self):
        """Получение материала и марки материала."""
        cursor, _ = self.connect
        self.sql = 'sql/material_and_brand.sql'
        res = cursor.execute(self.open_sql)
        material_list: List[str] = []
        brand_list: List[str | int] = []
        for material, brand in res.fetchall():
            material_list.append(material)
            brand_list.append(brand)
        self.close()
        return material_list, brand_list

    def update_database(self, data: Tuple[List[str], List[str | int]]):
        """Обновить базу данных материалов."""
        self.sql = 'sql/update_material_part.sql'
        self.update(self.open_sql, data)
        self.sql = 'sql/sorted_material_part.sql'
        self.clean_repeat(self.open_sql)

    def delete_data(self, name: str | int) -> None:
        """Удалить элемент с базы данных."""
        self.sql = 'sql/delete_material_part.sql'
        self.delete(self.open_sql, name)
