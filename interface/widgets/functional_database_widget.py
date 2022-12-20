from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton

from interface.widgets.database_widget import DatabaseWidget


class FunctionalDatabaseWidget(DatabaseWidget):
    """Виджет: функционал базы данных."""

    def __init__(self):
        super(FunctionalDatabaseWidget, self).__init__()
        self.functional_widget = QWidget(self.database_widget)

        self.grid_layout_functional = QGridLayout(self.functional_widget)

        self.label_material = QLabel(self.functional_widget)
        self.label_type_part = QLabel(self.functional_widget)
        self.label_pattern = QLabel(self.functional_widget)
        self.label_exit = QLabel(self.functional_widget)
        self.label_settings = QLabel(self.functional_widget)

        self.push_button_material = QPushButton(self.functional_widget)
        self.push_button_type_part = QPushButton(self.functional_widget)
        self.push_button_pattern = QPushButton(self.functional_widget)
        self.push_button_settings = QPushButton(self.functional_widget)
        self.push_button_exit = QPushButton(self.functional_widget)
