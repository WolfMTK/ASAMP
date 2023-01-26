from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLayout,
)

from name_objects.name_objects import (
    NAME_DATABASE_WIDGET,
    NAME_PUSH_BUTTON_ADD_DATA,
    NAME_PUSH_BUTTON_DELETE_DATA,
    NAME_PUSH_BUTTON_SAVE_DATA,
    NAME_DATABASE_TABLE_WIDGET,
)
from style.size_objects import (
    WIDTH_PUSH_BUTTON_ADD_DATA,
    HEIGHT_PUSH_BUTTON_ADD_DATA,
    WIDTH_PUSH_BUTTON_DELETE_DATA,
    HEIGHT_PUSH_BUTTON_DELETE_DATA,
    WIDTH_PUSH_BUTTON_SAVE_DATA,
    HEIGHT_PUSH_BUTTON_SAVE_DATA,
)
from style.style import (
    STYLE_DATABASE_WIDGET,
    STYLE_PUSH_BUTTON_ADD_DATA,
    STYLE_PUSH_BUTTON_DELETE_DATA,
    STYLE_PUSH_BUTTON_SAVE_DATA,
    STYLE_DATABASE_TABLE_WIDGET,
)
from widgets.widget import Widget


class DatabaseWidget(Widget):
    """Виджет данных из базы данных."""

    def __init__(self, widget: QWidget) -> None:
        self.widget = QWidget(widget)
        self.database_table_widget = QTableWidget(self.widget)
        self.action_widget = QWidget(self.widget)
        self.vertical_layout = QVBoxLayout(self.widget)
        self.horizontal_layout = QHBoxLayout(self.action_widget)
        self.push_button_add_data = QPushButton(self.action_widget)
        self.push_button_delete_data = QPushButton(self.action_widget)
        self.push_button_save_data = QPushButton(self.action_widget)
        self.add_objects_for_widget()

    def add_objects_for_widget(self) -> None:
        """Добавить объекты для виджета."""
        self.add_parameters_for_widget()
        self.add_parameters_for_push_buttons()
        self.add_parameters_for_table()

    def add_parameters_for_widget(self) -> None:
        """Добавить параметры для виджета."""
        self.name_objets = NAME_DATABASE_WIDGET
        self.style_widget = STYLE_DATABASE_WIDGET
        self.add_name_for_objects()
        self.add_style()
        self.add_vertical_layout_for_widgets()
        self.add_horizontal_layout_for_widgets()

    def add_vertical_layout_for_widgets(self) -> None:
        """Добавить выравнивание по вертикали для виджетов."""
        self.vertical_layout.addWidget(self.database_table_widget)
        self.vertical_layout.addWidget(self.action_widget)

    def add_horizontal_layout_for_widgets(self) -> None:
        """Добавить выравнивание по горизонтали для виджетов."""
        self.horizontal_layout.addWidget(self.push_button_add_data)
        self.horizontal_layout.addWidget(self.push_button_delete_data)
        self.horizontal_layout.addWidget(self.push_button_save_data)
        self.horizontal_layout.setSizeConstraint(
            QLayout.SizeConstraint.SetFixedSize
        )

    def add_parameters_for_push_buttons(self) -> None:
        """Добавить параметры для кнопок."""
        self.add_name_objects_for_push_buttons()
        self.add_style_for_push_buttons()
        self.add_fixed_size_for_push_buttons()

    def add_name_objects_for_push_buttons(self) -> None:
        """Добавить название объектов для кнопок."""
        self.push_button_add_data.setObjectName(NAME_PUSH_BUTTON_ADD_DATA)
        self.push_button_delete_data.setObjectName(
            NAME_PUSH_BUTTON_DELETE_DATA
        )
        self.push_button_save_data.setObjectName(NAME_PUSH_BUTTON_SAVE_DATA)

    def add_style_for_push_buttons(self) -> None:
        """Добавить стиль для кнопок."""
        self.push_button_add_data.setStyleSheet(STYLE_PUSH_BUTTON_ADD_DATA)
        self.push_button_delete_data.setStyleSheet(
            STYLE_PUSH_BUTTON_DELETE_DATA
        )
        self.push_button_save_data.setStyleSheet(STYLE_PUSH_BUTTON_SAVE_DATA)

    def add_fixed_size_for_push_buttons(self) -> None:
        """Добавить фиксированный размер для кнопок."""
        self.push_button_add_data.setFixedSize(
            WIDTH_PUSH_BUTTON_ADD_DATA, HEIGHT_PUSH_BUTTON_ADD_DATA
        )
        self.push_button_delete_data.setFixedSize(
            WIDTH_PUSH_BUTTON_DELETE_DATA, HEIGHT_PUSH_BUTTON_DELETE_DATA
        )
        self.push_button_save_data.setFixedSize(
            WIDTH_PUSH_BUTTON_SAVE_DATA, HEIGHT_PUSH_BUTTON_SAVE_DATA
        )

    def add_parameters_for_table(self) -> None:
        """Добавить параметры для таблицы."""
        self.add_name_objects_for_table_widget()
        self.add_style_for_table_widget()

    def add_name_objects_for_table_widget(self) -> None:
        """Добавить название объектам для таблицы."""
        self.database_table_widget.setObjectName(NAME_DATABASE_TABLE_WIDGET)

    def add_style_for_table_widget(self) -> None:
        """Добавить стиль для таблицы."""
        self.database_table_widget.setStyleSheet(STYLE_DATABASE_TABLE_WIDGET)
