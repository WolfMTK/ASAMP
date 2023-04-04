import logging
from typing import List, Any, Tuple

from PySide6.QtWidgets import QMainWindow, QGridLayout, QTableWidgetItem
from PySide6.QtCore import Qt

from database import Database
from widgets import CentralWidget, ControlWidget, DatabaseWidget
from .elements import WindowParameters
from .settings import WIDTH_WINDOW, HEIGHT_WINDOW, TITLE_DATABASE
from .settings_patern_window import SettingsPattern


logger = logging.getLogger(__name__)

CLEAR_INDEX = 0


class DatabaseWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__keys = {
            "materials": False,
            "settings": False,
            "type_part": False,
        }
        self.row: int | None = None
        self.col: int | None = None
        self.__parameters: None | List[str] = None
        self.__add_widgets()
        self.__set_parameters_window()
        self.__align_elements()
        self.__add_elements()
        self.__set_click_push_buttons()

    def __add_widgets(self) -> None:
        self.central_widget = CentralWidget(self).widget
        self.control_widget = ControlWidget(self)
        self.database_widget = DatabaseWidget(self)

    def __set_parameters_window(self) -> None:
        WindowParameters(
            self,
            self.central_widget,
            TITLE_DATABASE,
            min_width=WIDTH_WINDOW,
            min_height=HEIGHT_WINDOW,
        ).set_parameters()

    def __align_elements(self) -> None:
        grid_layout = QGridLayout(self.central_widget)
        grid_layout.addWidget(self.control_widget.widget, 0, 0, 1, 1)
        grid_layout.addWidget(self.database_widget.widget, 0, 1, 2, 2)

    def __add_elements(self) -> None:
        self.table_database = self.database_widget.table_database
        self.push_button_add = self.database_widget.push_button_add
        self.push_button_delete = self.database_widget.push_button_delete
        self.push_button_save = self.database_widget.push_button_save
        self.push_button_exit = self.control_widget.push_button_exit
        self.push_button_material = self.control_widget.push_button_material
        self.push_button_pattern = self.control_widget.push_button_pattern
        self.push_button_settings = self.control_widget.push_button_settings
        self.push_button_type_part = self.control_widget.push_button_type_part

    def __set_click_push_buttons(self) -> None:
        self.push_button_exit.clicked.connect(self.__close_window)
        self.push_button_material.clicked.connect(self.__active_key_material)
        self.push_button_settings.clicked.connect(self.__active_key_settings)
        self.push_button_type_part.clicked.connect(self.__active_key_type_part)
        self.push_button_pattern.clicked.connect(self.__open_settings_pattern)
        self.push_button_add.clicked.connect(self.__add_row)
        self.push_button_delete.clicked.connect(self.__delete_row)
        self.push_button_save.clicked.connect(self.__save_data)

    def __close_window(self) -> None:
        self.close()

    def __active_key_material(self) -> None:
        self.__return_keys_to_original_state()
        self.__keys["materials"] = True
        self.__update_table()

    def __active_key_type_part(self) -> None:
        self.__return_keys_to_original_state()
        self.__keys["type_part"] = True
        self.__update_table()

    def __active_key_settings(self) -> None:
        self.__return_keys_to_original_state()
        self.__keys["settings"] = True
        self.__update_table()

    def __update_table(self) -> None:
        self.__clear_table()
        data = self.__get_data()
        self.__add_data_in_table(data)
        self.__connect_table()

    def __open_settings_pattern(self) -> None:
        self.__return_keys_to_original_state()
        self.__clear_table()
        self.row = None
        self.col = None
        self.settings_pattern = SettingsPattern()
        self.settings_pattern.setWindowModality(
            Qt.WindowModality.ApplicationModal
        )
        self.settings_pattern.show()

    def __return_keys_to_original_state(self) -> None:
        for key in self.__keys.keys():
            self.__keys[key] = False

    def __get_data(self) -> Tuple[List[Any]]:
        if self.__keys.get("materials"):
            data = Database("sql/materials.sql").get_data()
            return data
        elif self.__keys.get("type_part"):
            data = Database("sql/type_parts.sql").get_data()
            return data
        elif self.__keys.get("settings"):
            data = Database("sql/parameters.sql").get_data()
            return data

    def __add_data_in_table(self, data) -> None:
        if data and data != self.__parameters:
            self.__parameters = data
            self.table_database.setRowCount(len(data))
            self.table_database.setColumnCount(len(data[0]))
            self.table_database.horizontalHeader().setVisible(False)
            self.table_database.verticalHeader().setVisible(False)
            for i in range(len(data)):
                for j in range(len(data[0])):
                    self.table_database.setItem(
                        i, j, QTableWidgetItem(str(data[i][j]))
                    )
            self.table_database.resizeColumnsToContents()
        if not data and self.__parameters is None:
            self.__create_table()

    def __create_table(self) -> None:
        if self.__keys.get("materials"):
            self.table_database.setRowCount(1)
            self.table_database.setColumnCount(5)
        elif self.__keys.get("type_part"):
            self.table_database.setRowCount(1)
            self.table_database.setColumnCount(2)
        elif self.__keys.get("settings"):
            self.table_database.setRowCount(1)
            self.table_database.setColumnCount(4)
        self.table_database.horizontalHeader().setVisible(False)
        self.table_database.verticalHeader().setVisible(False)

    def __clear_table(self) -> None:
        self.__parameters = None
        self.table_database.setColumnCount(CLEAR_INDEX)
        self.table_database.setRowCount(CLEAR_INDEX)

    def __connect_table(self) -> None:
        self.table_database.cellClicked.connect(self.__row_and_column)

    def __row_and_column(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def __add_row(self) -> None:
        count = self.table_database.rowCount()
        if self.row:
            self.table_database.insertRow(self.row + 1)
        elif count:
            self.table_database.insertRow(count)

    def __delete_row(self) -> None:
        count = self.table_database.rowCount()
        if self.row:
            self.table_database.removeRow(self.row)
        elif count:
            self.table_database.removeRow(count - 1)

    def __save_data(self) -> None:
        if self.__keys.get("materials"):
            self.__connect_database(
                "sql/adding_materials.sql", "sql/deleted_materials.sql"
            )
            self.__update_table()
        elif self.__keys.get("type_part"):
            self.__connect_database(
                "sql/adding_type_parts.sql", "sql/deleted_type_parts.sql"
            )
            self.__update_table()
        elif self.__keys.get("settings"):
            self.__connect_database(
                "sql/adding_settings.sql", "sql/deleted_settings.sql"
            )
            self.__update_table()

    def __connect_database(self, path_add: str, path_del: str) -> None:
        try:
            data = self.__get_data_with_table()
            Database(path_del).requests_with_database()
            Database(path_add).requests_with_database(data=data)
        except (AttributeError, TypeError):
            pass
        else:
            logger.info("База данных обновлена!")

    def __get_data_with_table(self) -> Tuple[List[Any]]:
        col_count = self.table_database.columnCount()
        row_count = self.table_database.rowCount()
        data = ()
        for i in range(row_count):
            data_table = []
            for j in range(1, col_count):
                data_table.append(self.table_database.item(i, j).text())
            data += ([*data_table],)
        return data
