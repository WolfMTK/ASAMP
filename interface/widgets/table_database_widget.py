from PySide6.QtWidgets import (
    QWidget, QTableWidget, QVBoxLayout, QHBoxLayout,
    QPushButton
)

from interface.widgets.database_widget import DatabaseWidget


class TableDatabaseWidget(DatabaseWidget):
    def __init__(self) -> None:
        super(TableDatabaseWidget, self).__init__()
        self.table_database_widget = QWidget(self.database_widget)
        self.table_widget = QWidget(self.table_database_widget)
        self.button_widget = QWidget(self.table_database_widget)

        self.table_database = QTableWidget(self.table_widget)

        self.v_layout_database_table = QVBoxLayout(self.table_database_widget)

        self.h_layout_table = QHBoxLayout(self.table_widget)
        self.h_layout_button = QHBoxLayout(self.button_widget)

        self.push_button_add = QPushButton(self.button_widget)
        self.push_button_clear = QPushButton(self.button_widget)
        self.push_button_save = QPushButton(self.button_widget)
