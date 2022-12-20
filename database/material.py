from typing import Set, List

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

    def get_brand(self):
        """Получение списка марки материала."""
        if self.material:
            cursor, _ = self.connect
            self.sql = 'sql/brand.sql'
            res = cursor.execute(self.open_sql, (self.material,))
            brand_list: List[str | int] = [brand[0] for brand in res.fetchall()]
            self.close()
            return brand_list
