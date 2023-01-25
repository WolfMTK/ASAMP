from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QLabel

from name_objects.name_objects import (NAME_DATA_TABLE_WIDGET,
                                       NAME_LABEL_DATA_TABLE_WIDGET,
                                       NAME_DATA_WIDGET)
from style.size_objects import WIDTH_DATA_WIDGET, HEIGHT_DATA_WIDGET
from style.style import (STYLE_DATA_TABLE_WIDGET,
                         STYLE_LABEL_DATA_TABLE_WIDGET,
                         STYLE_DATA_WIDGET)
from widgets.widget import Widget


class DataWidget(Widget):
    """Виджет с данными ввода."""

    def __init__(self, widget: QWidget) -> None:
        self.widget = QWidget(widget)
        self.vertical_layout = QVBoxLayout(self.widget)
        self.data_table_widget = QTableWidget(self.widget)
        self.data_label_widget = QLabel(self.widget)
        self.add_objects_for_widget()

    def add_objects_for_widget(self) -> None:
        """Добавить объекты для виджета."""
        self.add_parameters_for_widget()
        self.add_parameters_for_table()
        self.add_parameters_for_label()

    def add_parameters_for_widget(self) -> None:
        """Добавить параметры для виджета."""
        self.name_objets = NAME_DATA_WIDGET
        self.style_widget = STYLE_DATA_WIDGET
        self.add_name_for_objects()
        self.add_style()
        self.add_vertical_layout_for_widgets()

    # TODO: в данный момент метод не применяется.
    def add_fixed_size_for_widget(self) -> None:
        """Добавить фиксированные размеры для виджета."""
        self.widget.setFixedSize(WIDTH_DATA_WIDGET, HEIGHT_DATA_WIDGET)

    def add_vertical_layout_for_widgets(self) -> None:
        """Добавить вертикальное выравнивание для виджетов."""
        self.vertical_layout.addWidget(self.data_label_widget)
        self.vertical_layout.addWidget(self.data_table_widget)

    def add_parameters_for_table(self) -> None:
        """Добавить параметры для таблицы."""
        self.add_name_objects_for_table_widget()
        self.add_style_for_table_widget()

    def add_name_objects_for_table_widget(self) -> None:
        """Добавить название объектам для таблицы."""
        self.data_table_widget.setObjectName(NAME_DATA_TABLE_WIDGET)

    def add_style_for_table_widget(self) -> None:
        """Добавить стиль для таблицы."""
        self.data_table_widget.setStyleSheet(STYLE_DATA_TABLE_WIDGET)

    def add_parameters_for_label(self) -> None:
        """Добавить параметры для элементов текста."""
        self.add_name_objects_for_label()
        self.add_style_for_label()
        self.add_text_for_label()

    def add_name_objects_for_label(self) -> None:
        """Добавить название объектов для текста."""
        self.data_label_widget.setObjectName(NAME_LABEL_DATA_TABLE_WIDGET)

    def add_style_for_label(self) -> None:
        """Добавить стиль для текста."""
        self.data_label_widget.setStyleSheet(STYLE_LABEL_DATA_TABLE_WIDGET)

    def add_text_for_label(self) -> None:
        """Добавить текст для элемента текста."""
        self.data_label_widget.setText('Анализ технологичности детали')
