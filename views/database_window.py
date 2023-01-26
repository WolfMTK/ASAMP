from typing import List, Tuple, Any

from PySide6.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QTableWidgetItem,
    QHeaderView,
)

from database.database import Database
from style.size_objects import WIDTH_DATABASE_WINDOW, HEIGHT_DATABASE_WINDOW
from widgets.central_widget import CentralWidget
from widgets.control_widget import ControlWidget
from widgets.database_widget import DatabaseWidget


class DatabaseWindow(QMainWindow):
    """Окно базы данных."""

    def __init__(self):
        super(DatabaseWindow, self).__init__()
        self.central_widget = CentralWidget(self).widget
        self.control_widget = ControlWidget(self)
        self.database_widget = DatabaseWidget(self)
        self.grid_layout = QGridLayout(self.central_widget)
        self.row: int = ...
        self.column: int = ...
        self.keys = {
            "materials": False,
            "parts": False,
            "patterns": False,
            "parameters": False,
        }
        self.add_functional_for_window()

    @property
    def materials(self) -> List[Tuple[Any]]:
        """Материал с базы данных."""
        return Database().materials_for_database

    @property
    def parameters(self) -> List[Tuple[Any]]:
        """Параметры с базы данных."""
        return Database().parameters_for_database

    @property
    def patterns(self) -> List[Tuple[Any]]:
        """Шаблоны с базы данных."""
        return Database().patterns_for_database

    @property
    def type_parts(self):
        """Классы деталей с базы данных."""
        return Database().type_parts_for_database

    def add_functional_for_window(self) -> None:
        """Добавить функционал для окна."""
        self.add_minimum_size_for_window()
        self.add_title_for_window()
        self.set_central_widget()
        self.add_grid_layout_for_widgets()
        self.hide_widget_with_buttons()
        self.add_click_for_buttons()

    def add_minimum_size_for_window(self) -> None:
        """Добавить минимальный размер окна."""
        self.setMinimumSize(WIDTH_DATABASE_WINDOW, HEIGHT_DATABASE_WINDOW)

    def add_title_for_window(self) -> None:
        """Добавить название для приложения."""
        self.setWindowTitle("DATABASE")

    def set_central_widget(self) -> None:
        """Установить центральный виджет для окна."""
        self.setCentralWidget(self.central_widget)

    def add_grid_layout_for_widgets(self) -> None:
        """Добавить выравнивание по сетке для виджетов."""
        self.grid_layout.addWidget(self.control_widget.widget, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.database_widget.widget, 0, 1, 2, 2)

    def hide_widget_with_buttons(self) -> None:
        """Скрыть виджет с кнопками."""
        self.database_widget.action_widget.hide()

    def show_widget_with_buttons(self) -> None:
        """Показать виджет с кнопками."""
        self.database_widget.action_widget.show()

    def add_click_for_buttons(self) -> None:
        """Добавить нажатие для кнопок."""

        self.control_widget.push_button_material.clicked.connect(
            self.add_functional_for_table_material
        )
        self.control_widget.push_button_pattern.clicked.connect(
            self.add_functional_for_table_pattern
        )
        self.control_widget.push_button_settings.clicked.connect(
            self.add_functional_for_table_parameters
        )
        self.control_widget.push_button_type_part.clicked.connect(
            self.add_functional_for_table_type_part
        )
        self.control_widget.push_button_exit.clicked.connect(self.close)

        self.database_widget.push_button_add_data.clicked.connect(
            self.__add_row_in_table_widget
        )
        self.database_widget.push_button_delete_data.clicked.connect(
            self.__delete_row_in_table_widget
        )
        self.database_widget.push_button_save_data.clicked.connect(
            self.add_data_in_database
        )

    def add_functional_for_table_material(self) -> None:
        """Добавить функционал для таблицы."""
        data = self.materials
        self.__add_functional_for_table_widget(data)
        self.keys["materials"] = True

    def add_functional_for_table_pattern(self) -> None:
        """Добавить функционал для таблицы."""
        data = self.patterns
        self.__add_functional_for_table_widget(data)
        self.keys["patterns"] = True

    def add_functional_for_table_parameters(self) -> None:
        """Добавить функционал для таблицы."""
        data = self.parameters
        self.__add_functional_for_table_widget(data)
        self.keys["parameters"] = True

    def add_functional_for_table_type_part(self) -> None:
        """Добавить функционал для таблицы."""
        data = self.type_parts
        self.__add_functional_for_table_widget(data)
        self.keys["parts"] = True

    def __add_functional_for_table_widget(self, data):
        self.return_keys_to_original_state()
        self.clear_data_in_table_widget()
        self.add_column_in_table_widgets(len(data), len(data[0]))
        self.remove_name_column_with_table_widget()
        self.add_data_in_table_widget(data)
        self.set_sections_in_table_widget(len(data[0]))
        self.show_widget_with_buttons()
        self.__set_row_and_column_with()

    def clear_data_in_table_widget(self) -> None:
        """Очистить данные в таблице."""
        index_column = 0
        self.database_widget.database_table_widget.clear()
        self.database_widget.database_table_widget.setColumnCount(index_column)
        self.database_widget.database_table_widget.setRowCount(index_column)

    def add_column_in_table_widgets(
        self, row_count: int, column_count: int
    ) -> None:
        """Добавить колонки в таблицу материалов."""
        self.database_widget.database_table_widget.setRowCount(row_count)
        self.database_widget.database_table_widget.setColumnCount(column_count)

    def add_data_in_table_widget(self, data: Any) -> None:
        """Добавить данные в таблицу."""
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.database_widget.database_table_widget.setItem(
                    i, j, QTableWidgetItem(str(data[i][j]))
                )

    def set_sections_in_table_widget(self, size) -> None:
        """Задать размеры секций в таблице."""
        (
            self.database_widget.database_table_widget.horizontalHeader().setMinimumSectionSize(
                30
            )
        )
        for i in range(size):
            (
                self.database_widget.database_table_widget.horizontalHeader().setSectionResizeMode(
                    i, QHeaderView.ResizeMode.ResizeToContents
                )
            )

    def remove_name_column_with_table_widget(self) -> None:
        """Убрать название колонок с таблицы."""
        (
            self.database_widget.database_table_widget.horizontalHeader().setVisible(
                False
            )
        )
        (
            self.database_widget.database_table_widget.verticalHeader().setVisible(
                False
            )
        )

    def return_keys_to_original_state(self) -> None:
        """Вернуть ключи в исходное состояние."""
        for key in self.keys.keys():
            self.keys[key] = False

    def add_data_in_database(self) -> None:
        """Добавить данные в базу данных."""
        data = convert_string_id_in_int(self.get_data_with_table_widget())
        if self.keys["materials"]:
            self.__add_material_in_database(data)
        elif self.keys["patterns"]:
            self.__add_patterns_in_database(data)
        elif self.keys["parameters"]:
            self.__add_parameters_id_database(data)
        elif self.keys["parts"]:
            self.__add_parts_in_database(data)

    def get_data_with_table_widget(self) -> Tuple[List[Any]]:
        """Получить данные с таблицы."""
        col_count = self.database_widget.database_table_widget.columnCount()
        row_count = self.database_widget.database_table_widget.rowCount()
        data_list = []
        for i in range(row_count):
            data_table = []
            for j in range(col_count):
                data_table.append(
                    self.database_widget.database_table_widget.item(
                        i, j
                    ).text()
                )
            data_list.append(data_table)
        return tuple(data_list)

    def __add_row_in_table_widget(self) -> None:
        count = self.database_widget.database_table_widget.rowCount()
        if self.row:
            try:
                self.database_widget.database_table_widget.insertRow(
                    self.row + 1
                )
            except TypeError:
                self.database_widget.database_table_widget.insertRow(count)
        else:
            self.database_widget.database_table_widget.insertRow(count)

    def __delete_row_in_table_widget(self) -> None:
        count = self.database_widget.database_table_widget.rowCount()
        if self.row:
            try:
                self.database_widget.database_table_widget.removeRow(self.row)
            except TypeError:
                self.database_widget.database_table_widget.removeRow(count - 1)
        else:
            self.database_widget.database_table_widget.removeRow(count - 1)

    def __set_row_and_column_with(self):
        self.database_widget.database_table_widget.cellClicked.connect(
            self.__get_row_and_column
        )

    def __get_row_and_column(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    @staticmethod
    def __add_material_in_database(data: Tuple[List[Any]]) -> None:
        Database().add_data_in_materials(data)
        Database().add_data_in_material_pattern()

    @staticmethod
    def __add_patterns_in_database(data: Tuple[List[Any]]) -> None:
        Database().add_data_in_patterns(data)
        Database().add_data_in_material_pattern()

    @staticmethod
    def __add_parameters_id_database(data: Tuple[List[Any]]) -> None:
        Database().add_data_in_parameters(data)

    @staticmethod
    def __add_parts_in_database(data: Tuple[List[Any]]) -> None:
        Database().add_data_in_parts(data)


def convert_string_id_in_int(data) -> Tuple[List[Any]]:
    """Конвертировать id в целое."""
    for index in range(len(data)):
        data[index].pop(0)
    return data
