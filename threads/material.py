import logging
from itertools import count
from typing import List

from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QThread

from database import Database


logger = logging.getLogger(__name__)


class Material(QThread):
    def __init__(self, combo_box_material: QComboBox) -> None:
        super().__init__()
        self.combo_box_material = combo_box_material
        self.status = True
        self.materials: List[str] | None = None

    def run(self) -> None:
        for _ in count(1):
            data = [
                material[0]
                for material in Database("sql/material.sql").get_data()
            ]
            self.__add_data_in_combo_box(data)
            if not self.status:
                break
            self.msleep(10)

    def close_thread(self) -> None:
        self.status = False

    def __add_data_in_combo_box(self, data):
        if data and data != self.materials:
            self.materials = data
            self.combo_box_material.clear()
            self.combo_box_material.addItems([""] + self.materials)
            self.combo_box_material.setEnabled(True)
            logger.info('Добавление материала в combo_box_material!')
        elif not self.materials:
            self.combo_box_material.setEnabled(False)
