import sys
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QGridLayout,
                               QCompleter, QTableWidgetItem, QHeaderView)

from database.database import Database
from style.size_objects import WIDTH_MAIN_WINDOW, HEIGHT_MAIN_WINDOW
from style.style import STYLE_COMBO_BOX_BRAND
from views.database_window import DatabaseWindow
from widgets.action_widget import ActionWidget
from widgets.central_widget import CentralWidget
from widgets.data_widget import DataWidget
from widgets.parameters_widget import ParametersWidget
from widgets.result_widget import ResultWidget

VALUE_COLUMN_IN_TABLE = 2


class MainWindow(QMainWindow):
    """Главное окно программы."""

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.central_widget = CentralWidget(self).widget
        self.action_widget = ActionWidget(self.central_widget)
        self.parameters_widget = ParametersWidget(self.central_widget)
        self.result_widget = ResultWidget(self.central_widget)
        self.database_window = DatabaseWindow()
        self.data_widget = DataWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.add_functional_for_window()

    def add_functional_for_window(self) -> None:
        """Добавить функционал для окна."""
        self.add_minimum_size_for_window()
        self.add_title_for_window()
        self.set_central_widget()
        self.add_grid_layout_for_widgets()
        self.add_click_for_buttons()
        self.add_functional_for_combo_box()
        self.deactivate_text_edit_result()

    def add_minimum_size_for_window(self) -> None:
        """Добавить минимальный размер окна."""
        self.setMinimumSize(WIDTH_MAIN_WINDOW, HEIGHT_MAIN_WINDOW)

    def add_title_for_window(self) -> None:
        """Добавить название для приложения."""
        self.setWindowTitle("ASAMP")

    def set_central_widget(self) -> None:
        """Установить центральный виджет для окна."""
        self.setCentralWidget(self.central_widget)

    def add_grid_layout_for_widgets(self) -> None:
        """Добавить выравнивание по сетке для виджетов."""
        self.grid_layout.addWidget(self.action_widget.widget, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.parameters_widget.widget, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.data_widget.widget, 0, 1, 3, 1)
        self.grid_layout.addWidget(self.result_widget.widget, 1, 0, 1, 1)

    def add_click_for_buttons(self) -> None:
        """Добавить нажатие для кнопок."""
        self.action_widget.push_button_exit.clicked.connect(self.close)
        self.action_widget.push_button_clear.clicked.connect(self.close)
        self.action_widget.push_button_result.clicked.connect(self.close)
        self.action_widget.push_button_save.clicked.connect(self.close)
        self.parameters_widget.push_button_edit_database.clicked.connect(
            self.open_window_database_for_editing)

    def open_window_database_for_editing(self) -> None:
        """Открыть базы данных для редактирования."""
        self.database_window.setWindowModality(
            Qt.WindowModality.ApplicationModal
        )
        self.database_window.show()

    def add_functional_for_combo_box(self) -> None:
        """Добавить функционал для комбинированных кнопок."""
        self.add_data_in_combo_boxes()
        self.add_to_enter_for_combo_boxes()
        self.add_connect_for_combo_box()

    def add_data_in_combo_boxes(self) -> None:
        """Добавить данные для комбинированных кнопок."""
        material = self.__get_material()
        type_part = self.__get_type_part()
        self.parameters_widget.combo_box_material.addItems(
            self.__add_null_argument(material)
        )
        self.parameters_widget.combo_box_type_part.addItems(
            self.__add_null_argument(type_part)
        )
        self.add_completer_for_combo_boxes([material, type_part])

    def add_completer_for_combo_boxes(self, data: List[List[str]]):
        """Добавить подсказки ввода для комбинированных кнопок."""
        self.parameters_widget.combo_box_material.setCompleter(
            QCompleter(data[0])
        )
        self.parameters_widget.combo_box_type_part.setCompleter(
            QCompleter(data[1])
        )

    def add_to_enter_for_combo_boxes(self) -> None:
        """Добавить ввод текста для комбинированных кнопок."""
        self.parameters_widget.combo_box_material.setEditable(True)
        self.parameters_widget.combo_box_type_part.setEditable(True)

    def add_connect_for_combo_box(self):
        """Добавить подключение для комбинированной кнопки."""
        self.parameters_widget.combo_box_material.currentTextChanged.connect(
            self.activate_an_inactive_combo_box
        )
        self.parameters_widget.combo_box_type_part.currentTextChanged.connect(
            self.add_functional_for_table_widget
        )

    def activate_an_inactive_combo_box(self) -> None:
        """Активировать неактивную комбинированную кнопку."""
        material = self.get_text_from_combo_box_material()
        self.delete_items_in_combo_box_brand()
        if len(material) != 0:
            self.add_to_enter_for_combo_box_brand()
            self.add_data_in_combo_box_brand(material)

    def get_text_from_combo_box_material(self) -> str:
        """Получить текст из комбинированной кнопки с материалом"""
        return self.parameters_widget.combo_box_material.currentText()

    def delete_items_in_combo_box_brand(self) -> None:
        """
        Добавить удаление элементов в комбинированной
        кнопке для марки материала
        """
        self.parameters_widget.combo_box_brand.clear()
        self.parameters_widget.combo_box_brand.setEditable(False)

    def add_to_enter_for_combo_box_brand(self) -> None:
        """
        Добавить ввод текста для комбинированной
        кнопки марки материала
        """
        self.parameters_widget.combo_box_brand.setEditable(True)
        self.parameters_widget.combo_box_brand.setStyleSheet(
            STYLE_COMBO_BOX_BRAND
        )

    def add_data_in_combo_box_brand(self, material: str) -> None:
        """
        Добавить данные в комбинированную кнопку марки материала
        """
        brand = self.__get_brand(material)
        self.parameters_widget.combo_box_brand.addItems(
            self.__add_null_argument(brand)
        )
        self.add_completer_for_combo_box_brand(brand)

    def add_completer_for_combo_box_brand(self, data: List[str]) -> None:
        """
        Добавить подсказки ввода длящ комбинированой
        кнопки марки материала.
        """
        self.parameters_widget.combo_box_brand.setCompleter(
            QCompleter(data)
        )

    def deactivate_text_edit_result(self) -> None:
        """Деактивировать изменяемый текст с результатом."""
        self.result_widget.text_edit_result.setEnabled(False)

    def add_functional_for_table_widget(self) -> None:
        parameters = self.__get_parameters(
            self.get_text_from_combo_box_type_part()
        )
        self.clear_data_in_table_widget()
        self.add_column_in_table_widget(parameters)
        self.remove_name_column_with_table_widget()
        self.add_data_in_table_widget(parameters)
        self.set_sections_in_table_widget()

    def get_text_from_combo_box_type_part(self) -> None:
        """Получение текста с комбинированной кнопки класса детали"""
        return self.parameters_widget.combo_box_type_part.currentText()

    def clear_data_in_table_widget(self) -> None:
        """Очистить данные в таблице."""
        index_column = 0
        self.data_widget.data_table_widget.clear()
        self.data_widget.data_table_widget.setColumnCount(index_column)
        self.data_widget.data_table_widget.setRowCount(index_column)

    def add_column_in_table_widget(self, data: List[str]) -> None:
        """Добавить колонки в таблицу."""
        self.data_widget.data_table_widget.setRowCount(len(data))
        self.data_widget.data_table_widget.setColumnCount(
            VALUE_COLUMN_IN_TABLE
        )

    def remove_name_column_with_table_widget(self) -> None:
        """Убрать название колонок с таблице."""
        self.data_widget.data_table_widget.horizontalHeader().setVisible(False)
        self.data_widget.data_table_widget.verticalHeader().setVisible(False)

    def add_data_in_table_widget(self, data: List[str]) -> None:
        """Добавление данных в таблицу."""
        for index, parameter in enumerate(data):
            self.data_widget.data_table_widget.setItem(
                index, 0, QTableWidgetItem(parameter)
            )

    def set_sections_in_table_widget(self) -> None:
        """Задать размеры секций в таблице."""
        (self.data_widget
         .data_table_widget
         .horizontalHeader()
         .setMinimumSectionSize(30))
        (self.data_widget
         .data_table_widget
         .horizontalHeader()
         .setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents))
        (self.data_widget
         .data_table_widget
         .horizontalHeader()
         .setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents))

    def clear_field_data(self) -> None:
        """Очистить данные полей."""

    @staticmethod
    def __get_material() -> List[str]:
        return Database().get_material_with_database

    @staticmethod
    def __get_type_part() -> List[str]:
        return Database().get_type_part_with_database

    @staticmethod
    def __get_brand(material: str) -> List[str]:
        return Database().get_brand_with_database(material)

    @staticmethod
    def __get_parameters(type_part: str) -> List[str]:
        return Database().get_parameters_with_database(type_part)

    @staticmethod
    def __add_null_argument(data: List[str]) -> List[str]:
        data = data.copy()
        data.insert(0, '')
        return data


def run_main_window() -> None:
    """Запуск главного окна."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
