from typing import Set, List

from database.database import Database


class Part(Database):
    @property
    def get_part(self) -> Set[str]:
        cursor, _ = self.connect
        self.sql = 'sql/part.sql'
        res = cursor.execute(self.open_sql)
        part_list: List[str] = [part[0] for part in res.fetchall()]
        self.close()
        return set(part_list)

    def update_database(self, data: str) -> None:
        """ОБновить базу данных класса детали."""
        self.sql = 'sql/update_type_part.sql'
        self.update(self.open_sql, data)
        self.sql = 'sql/sorted_type_part.sql'
        self.clean_repeat(self.open_sql)

    def delete_data(self, name: str) -> None:
        """Удалить элемент с базы данных."""
        self.sql = 'sql/delete_type_part.sql'
        self.delete(self.open_sql, name)
