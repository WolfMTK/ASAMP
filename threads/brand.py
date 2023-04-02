import logging
from itertools import count
from typing import List

from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QThread

from database import Database


logger = logging.getLogger(__name__)


class Brand(QThread):
    def __init__(
        self, combo_box_brand: QComboBox, combo_box_material: QComboBox
    ) -> None:
        super().__init__()
        self.combo_box_brand = combo_box_brand
        self.combo_box_material = combo_box_material
        self.status = True
        self.brand: List[str] | None = None

    def run(self) -> None:
        for _ in count(1):
            material = self.combo_box_material.currentText()
            data = None
            if all([material]):
                data = self.__get_data(material)
            else:
                self.brand = None
            self.__add_data_in_combo_box(data)
            if not self.status:
                break
            self.msleep(10)

    def close_thread(self) -> None:
        self.status = False

    def __get_data(self, material) -> None:
        data = []
        for brand in Database("sql/brand.sql").get_data(
            material_part=material
        ):
            data.append(brand[0])
        return data

    def __add_data_in_combo_box(self, data):
        if data and data != self.brand:
            self.brand = data
            self.combo_box_brand.clear()
            self.combo_box_brand.addItems([""] + self.brand)
            self.combo_box_brand.setEnabled(True)
            logger.info('Материал добавлен в combo_box_brand!')
        elif not self.brand:
            try:
                self.combo_box_brand.setEnabled(False)
                self.combo_box_brand.setCurrentIndex(0)
            except RuntimeError as error:
                logger.error(
                    f"Ошибка: {error}! Неправильное завершение программы!"
                )
                raise RuntimeError("Неправильное завершение программы!")
