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
