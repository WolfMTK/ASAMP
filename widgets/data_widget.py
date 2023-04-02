from PySide6.QtWidgets import QWidget, QVBoxLayout

from .elements import LabelParameters, TableParameters, WidgetParameters
from .settings import NAME_WIDGET, NAME_LABEL, NAME_TABLE_WIDGET


class DataWidget:
    def __init__(self, widget: QWidget) -> None:
        self.widget = WidgetParameters(widget, NAME_WIDGET, style=True).widget
        self.__add_table()
        self.__add_label()
        self.__align_elements()

    def __add_table(self) -> None:
        self.table_analysis = TableParameters(
            self.widget, NAME_TABLE_WIDGET
        ).table

    def __add_label(self) -> None:
        self.label_analysis = LabelParameters(
            self.widget, NAME_LABEL, "Анализ технологичности детали"
        ).label

    def __align_elements(self) -> None:
        vertical_layout = QVBoxLayout(self.widget)
        vertical_layout.addWidget(self.label_analysis)
        vertical_layout.addWidget(self.table_analysis)
