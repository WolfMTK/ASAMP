from typing import List, Tuple, Any

from PySide6.QtWidgets import (QMainWindow, QGridLayout, QTableWidgetItem,
                               QHeaderView)

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

        # self.database_widget.push_button_add_data
        # self.database_widget.push_button_delete_data
        # self.database_widget.push_button_save_data

    def add_functional_for_table_material(self) -> None:
        """Добавить функционал для таблицы."""
        self.clear_data_in_table_widget()
        data = self.materials
        self.add_column_in_table_widgets(len(data), len(data[0]))
        self.remove_name_column_with_table_widget()
        self.add_data_in_table_widget(data)
        self.set_sections_in_table_widget(len(data[0]))
        self.show_widget_with_buttons()

    def add_functional_for_table_pattern(self) -> None:
        """Добавить функционал для таблицы."""
        self.clear_data_in_table_widget()
        data = self.patterns
        self.add_column_in_table_widgets(len(data), len(data[0]))
        self.remove_name_column_with_table_widget()
        self.add_data_in_table_widget(data)
        self.set_sections_in_table_widget(len(data[0]))
        self.show_widget_with_buttons()

    def add_functional_for_table_parameters(self) -> None:
        """Добавить функционал для таблицы."""
        self.clear_data_in_table_widget()
        data = self.parameters
        self.add_column_in_table_widgets(len(data), len(data[0]))
        self.remove_name_column_with_table_widget()
        self.add_data_in_table_widget(data)
        self.set_sections_in_table_widget(len(data[0]))
        self.show_widget_with_buttons()

    def add_functional_for_table_type_part(self) -> None:
        """Добавить функционал для таблицы."""
        self.clear_data_in_table_widget()
        data = self.type_parts
        self.add_column_in_table_widgets(len(data), len(data[0]))
        self.remove_name_column_with_table_widget()
        self.add_data_in_table_widget(data)
        self.set_sections_in_table_widget(len(data[0]))
        self.show_widget_with_buttons()

    def clear_data_in_table_widget(self) -> None:
        """Очистить данные в таблице."""
        index_column = 0
        self.database_widget.database_table_widget.clear()
        self.database_widget.database_table_widget.setColumnCount(
            index_column
        )
        self.database_widget.database_table_widget.setRowCount(index_column)

    def add_column_in_table_widgets(self,
                                    row_count: int,
                                    column_count: int) -> None:
        """Добавить колонки в таблицу материалов."""
        self.database_widget.database_table_widget.setRowCount(row_count)
        self.database_widget.database_table_widget.setColumnCount(
            column_count
        )

    def add_data_in_table_widget(self, data: Any) -> None:
        """Добавить данные в таблицу."""
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.database_widget.database_table_widget.setItem(
                    i, j, QTableWidgetItem(str(data[i][j]))
                )

    def set_sections_in_table_widget(self, size) -> None:
        """Задать размеры секций в таблице."""
        (self.database_widget
         .database_table_widget
         .horizontalHeader()
         .setMinimumSectionSize(30))
        for i in range(size):
            (self.database_widget
             .database_table_widget
             .horizontalHeader()
             .setSectionResizeMode(
                i, QHeaderView.ResizeMode.ResizeToContents)
            )

    def remove_name_column_with_table_widget(self) -> None:
        """Убрать название колонок с таблице."""
        (self.database_widget.
         database_table_widget.
         horizontalHeader().
         setVisible(False))
        (self.database_widget.
         database_table_widget.
         verticalHeader().
         setVisible(False))
