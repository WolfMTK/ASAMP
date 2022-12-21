from typing import Tuple, List

from PySide6.QtWidgets import QTableWidgetItem

from database.material import Material
from database.part import Part
from interface.settings_database_widgets import SettingsDatabaseWidget


class Functional(SettingsDatabaseWidget):
    """Функционал для виждетов."""

    def __init__(self):
        super(Functional, self).__init__()
        self.row: int = None
        self.col: int = None
        self.key: bool = False
        self.key_save: List[bool] = [False] * 4
        self.brand: List[str | int] = None
        self.material: List[str] = None
        self.type_part: List[str] = None
        self.settings: List[str] = None
        self.pattern: List[str] = None
        self.delete_element: str | int = None
        self.add_functional()

    def add_functional(self):
        """Добавить функционал."""
        self.add_functional_button()
        self.hide_table()

    def hide_table(self):
        """Скрыть таблицу."""
        self.button_widget.hide()
        self.table_widget.hide()

    def add_functional_button(self):
        """Добавить функционал для кнопок."""
        self.push_button_add.clicked.connect(self.add_columns)
        self.push_button_clear.clicked.connect(self.delete_columns)
        self.push_button_save.clicked.connect(self.save_columns)

        self.push_button_material.clicked.connect(self.active_key_material)
        self.push_button_type_part.clicked.connect(self.activate_key_type_part)
        self.push_button_settings.clicked.connect(self.activate_key_settings)
        self.push_button_pattern.clicked.connect(self.activate_key_pattern)
        self.push_button_exit.clicked.connect(self.close)

    def activate_key_type_part(self):
        """Активировать ключ для класса детали."""
        self.deactivate_list_key()
        self.key_save[1] = True
        self.key = True
        self.activate_table_type_part()

    def activate_key_settings(self):
        """Активировать ключ дня настроек."""
        self.deactivate_list_key()
        self.key_save[2] = True
        self.key = True
        self.activate_table_settings()

    def activate_key_pattern(self):
        """Активировать ключ для шаблона."""
        self.deactivate_list_key()
        self.key_save[3] = True
        self.key = True
        self.activate_table_pattern()

    def active_key_material(self):
        """Активировать ключ для материала."""
        self.deactivate_list_key()
        self.key_save[0] = True
        self.key = True
        self.activate_table_material()

    def deactivate_list_key(self):
        """Деактивация списка ключей"""
        for index, key in enumerate(self.key_save):
            self.key_save[index] = False

    def clear_table(self):
        """Очистить таблицу таблицы."""
        self.table_database.clear()
        self.table_database.setColumnCount(0)
        self.table_database.setRowCount(0)

    def activate_table_type_part(self):
        """Активировать таблицу для класса детали."""
        self.clear_table()
        self.add_functional_part_table()

    def activate_table_settings(self):
        """Активировать таблицу для настроек."""
        self.clear_table()
        self.add_functional_settings()

    def activate_table_pattern(self):
        """Активировать таблицу для шаблона."""
        self.clear_table()
        self.add_functional_pattern()

    def activate_table_material(self):
        """Активировать таблицу для материла."""
        self.clear_table()
        self.add_functional_material_table()

    def add_functional_part_table(self):
        """Добавить функционал для таблицы с классом детали."""
        self.type_part = Part().get_part
        self.show_table()
        self.add_column_in_table(len(self.type_part), 1)
        self.add_type_part()
        self.table_database.resizeColumnsToContents()

    def add_functional_settings(self):
        """Добавить функционал для таблицы с настройкми."""
        self.settings = ...
        self.show_table()
        # self.add_column_in_table(len(self.settings), 1)
        # self.add_settings_in_table()
        # self.table_database.resizeColumnsToContents()

    def add_functional_pattern(self):
        """Добавить функционал для шаблона."""
        self.pattern = ...
        self.show_table()
        # self.add_column_in_table(len(self.pattern), 1)
        # self.add_pattern()
        # self.table_database.resizeColumnsToContents()

    def add_functional_material_table(self):
        """Добавить функционал для таблицы с материалом."""
        self.material, self.brand = Material().get_material_and_brand
        self.show_table()
        self.add_column_in_table(len(self.material), 2)
        self.add_material_and_brand()
        self.table_database.resizeColumnsToContents()

    def add_column_in_table(self, row, col):
        """Добавить колонки в таблицу."""
        self.table_database.setRowCount(row)
        self.table_database.setColumnCount(col)
        self.table_database.horizontalHeader().setVisible(False)
        self.table_database.cellClicked.connect(self.get_row_and_col)

    def add_type_part(self):
        """Добавить класс детали в таблицу."""
        for index, name in enumerate(self.type_part):
            self.table_database.setItem(index, 0, QTableWidgetItem(name))

    def add_settings_in_table(self):
        """Добавить настройки в таблицу."""

    def add_pattern(self):
        """Добавить шаблон в таблицу."""

    def add_material_and_brand(self):
        """Добавить материал и марку материала в таблицу."""
        for index in range(len(self.material)):
            self.table_database.setItem(index, 0, QTableWidgetItem(self.brand[index]))
            self.table_database.setItem(index, 1, QTableWidgetItem(self.material[index]))

    def show_table(self):
        """Показать таблицу."""
        if self.key:
            self.button_widget.show()
            self.table_widget.show()
            self.key = False

    def get_row_and_col(self, row: int, col: int) -> None:
        """Получить строки и столбцы таблицы."""
        self.row = row
        self.col = col

    def add_columns(self):
        """Добавить колонки."""
        count = self.table_database.rowCount()
        if self.row:
            self.table_database.insertRow(self.row + 1)
        else:
            self.table_database.insertRow(count)

    def delete_columns(self):
        """Удаление колонки."""
        count = self.table_database.rowCount()
        if self.row:
            try:
                self.delete_element = self.table_database.item(self.row, 0).text()
            except AttributeError:
                pass
            self.table_database.removeRow(self.row)
        else:
            self.table_database.removeRow(count - 1)

    def get_type_part(self) -> List[str]:
        """Получить класс детали."""
        row_count, col_count = self.get_row_and_column()
        list_type_part: List[str] = []
        for row in range(row_count):
            list_type_part.append(self.table_database.item(row, col_count - 1).text())
        return list_type_part

    def get_settings(self):
        """Получить настройки."""

    def get_pattern(self):
        """Получить шаблон."""

    def get_material_and_brand(self) -> Tuple[List[str], List[str | int]]:
        """Получение списка материалов и марки материалов."""
        row_count, col_count = self.get_row_and_column()
        list_material: List[str] = []
        list_brand: List[str | int] = []
        for row in range(row_count):
            list_brand.append(self.table_database.item(row, col_count - 2).text())
            list_material.append(self.table_database.item(row, col_count - 1).text())
        return list_brand, list_material

    def get_row_and_column(self) -> Tuple[int, int]:
        """Получить ячейки и столбцы детали."""
        return self.table_database.rowCount(), self.table_database.columnCount()

    def save_columns(self):
        """Сохранение колонок."""
        # self.check_keys()
        if self.key_save[0]:
            self.save_material()
        elif self.key_save[1]:
            self.save_type_part()
        elif self.key_save[2]:
            print(3)
            ...
        elif self.key_save[3]:
            print(4)
            ...

    def save_material(self):
        """Сохранить материал в базе данных."""
        Material().update_database(self.get_material_and_brand())
        self.key_save[0] = True
        if self.delete_element:
            Material().delete_data(self.delete_element)
            self.delete_element = None

    def save_type_part(self):
        """Сохранить класс детали в базе данных"""
        Part().update_database(self.get_type_part())
        self.key_save[1] = True
        if self.delete_element:
            Part().delete_data(self.delete_element)
            self.delete_element = None

    def save_settings(self):
        """Сохранить настройки в базе данных"""

    def save_pattern(self):
        """Сохранить шаблон в базе данных."""
