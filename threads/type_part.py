import logging
from itertools import count
from typing import List

from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QThread

from database import Database


logger = logging.getLogger(__name__)


class TypePart(QThread):
    def __init__(self, combo_box_type_part: QComboBox) -> None:
        super().__init__()
        self.combo_box_type_part = combo_box_type_part
        self.status = True
        self.type_parts: List[str] | None = None

    def run(self) -> None:
        for _ in count(1):
            data = [
                type_part[0]
                for type_part in Database("sql/type_part.sql").get_data()
            ]
            self.__add_data_in_combo_box(data)
            if not self.status:
                break
            self.msleep(10)

    def close_thread(self) -> None:
        self.status = False

    def __add_data_in_combo_box(self, data) -> None:
        if data and data != self.type_parts:
            self.type_parts = data
            self.combo_box_type_part.clear()
            self.combo_box_type_part.addItems([""] + self.type_parts)
            self.combo_box_type_part.setEnabled(True)
            logger.info('Класс детали добавлен в combo_box_type_part!')
        elif not self.type_parts:
            self.combo_box_type_part.setEnabled(False)
