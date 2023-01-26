from PySide6.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget

from name_objects.name_objects import (
    NAME_CONTROL_WIDGET,
    NAME_LABEL_EXIT_DATABASE,
    NAME_LABEL_MATERIAL_DATABASE,
    NAME_LABEL_PATTERN_DATABASE,
    NAME_LABEL_SETTINGS_DATABASE,
    NAME_LABEL_TYPE_PART_DATABASE,
    NAME_PUSH_BUTTON_EXIT_DATABASE,
    NAME_PUSH_BUTTON_MATERIAL,
    NAME_PUSH_BUTTON_PATTERN,
    NAME_PUSH_BUTTON_SETTINGS,
    NAME_PUSH_BUTTON_TYPE_PART,
)
from style.size_objects import (
    HEIGHT_CONTROL_WIDGET,
    HEIGHT_PUSH_EDIT_DATABASE_EXIT,
    HEIGHT_PUSH_EDIT_MATERIAL,
    HEIGHT_PUSH_EDIT_PATTERN,
    HEIGHT_PUSH_EDIT_SETTINGS,
    HEIGHT_PUSH_EDIT_TYPE_PART,
    WIDTH_CONTROL_WIDGET,
    WIDTH_PUSH_BUTTON_DATABASE_EXIT,
    WIDTH_PUSH_BUTTON_MATERIAL,
    WIDTH_PUSH_BUTTON_PATTERN,
    WIDTH_PUSH_BUTTON_SETTINGS,
    WIDTH_PUSH_BUTTON_TYPE_PART,
)
from style.style import (
    STYLE_CONTROL_WIDGET,
    STYLE_PUSH_BUTTON_MATERIAL,
    STYLE_PUSH_BUTTON_TYPE_PART,
    STYLE_PUSH_BUTTON_PATTERN,
    STYLE_PUSH_BUTTON_SETTINGS,
    STYLE_PUSH_BUTTON_EXIT_DATABASE,
    STYLE_LABEL_MATERIAL_DATABASE,
    STYLE_LABEL_TYPE_PART_DATABASE,
    STYLE_LABEL_PATTERN_DATABASE,
    STYLE_LABEL_SETTINGS_DATABASE,
    STYLE_LABEL_EXIT_DATABASE,
)
from widgets.widget import Widget


class ControlWidget(Widget):
    """Виджет управления базой данных."""

    def __init__(self, widget: QWidget) -> None:
        self.widget = QWidget(widget)
        self.grid_layout = QGridLayout(self.widget)
        self.label_material = QLabel(self.widget)
        self.label_type_part = QLabel(self.widget)
        self.label_pattern = QLabel(self.widget)
        self.label_settings = QLabel(self.widget)
        self.label_exit = QLabel(self.widget)
        self.push_button_material = QPushButton(self.widget)
        self.push_button_type_part = QPushButton(self.widget)
        self.push_button_pattern = QPushButton(self.widget)
        self.push_button_settings = QPushButton(self.widget)
        self.push_button_exit = QPushButton(self.widget)
        self.add_objects_for_widget()

    def add_objects_for_widget(self) -> None:
        """Добавить объекты для виджета."""
        self.add_parameters_for_widget()
        self.add_parameters_for_push_buttons()
        self.add_parameters_for_label()

    def add_parameters_for_widget(self) -> None:
        """Добавить параметры для виджета."""
        self.name_objets = NAME_CONTROL_WIDGET
        self.style_widget = STYLE_CONTROL_WIDGET
        self.add_name_for_objects()
        self.add_style()
        self.add_size_fixed_for_widget()
        self.add_grid_layout_for_widgets()

    def add_parameters_for_push_buttons(self) -> None:
        """Добавить параметры для кнопок."""
        self.add_name_objects_for_push_buttons()
        self.add_style_for_push_buttons()
        self.add_fixed_size_for_push_buttons()

    def add_parameters_for_label(self) -> None:
        """Добавить параметры для элементов текста."""
        self.add_name_objects_for_label()
        self.add_style_for_label()
        self.add_text_for_label()

    def add_size_fixed_for_widget(self) -> None:
        """Добавить фиксированные размеры для виджета."""
        self.widget.setFixedSize(WIDTH_CONTROL_WIDGET, HEIGHT_CONTROL_WIDGET)

    def add_grid_layout_for_widgets(self) -> None:
        """Добавить выравнивание по сетке для виджетов."""
        self.grid_layout.addWidget(self.label_material, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.push_button_material, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.label_type_part, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.push_button_type_part, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.label_settings, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.push_button_settings, 2, 1, 1, 1)
        self.grid_layout.addWidget(self.label_pattern, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.push_button_pattern, 3, 1, 1, 1)
        self.grid_layout.addWidget(self.label_exit, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.push_button_exit, 4, 1, 1, 1)

    def add_name_objects_for_push_buttons(self) -> None:
        """Добавить название объектов для кнопок."""
        self.push_button_material.setObjectName(NAME_PUSH_BUTTON_MATERIAL)
        self.push_button_type_part.setObjectName(NAME_PUSH_BUTTON_TYPE_PART)
        self.push_button_pattern.setObjectName(NAME_PUSH_BUTTON_PATTERN)
        self.push_button_settings.setObjectName(NAME_PUSH_BUTTON_SETTINGS)
        self.push_button_exit.setObjectName(NAME_PUSH_BUTTON_EXIT_DATABASE)

    def add_style_for_push_buttons(self) -> None:
        """Добавить стиль для кнопок."""
        self.push_button_material.setStyleSheet(STYLE_PUSH_BUTTON_MATERIAL)
        self.push_button_type_part.setStyleSheet(STYLE_PUSH_BUTTON_TYPE_PART)
        self.push_button_pattern.setStyleSheet(STYLE_PUSH_BUTTON_PATTERN)
        self.push_button_settings.setStyleSheet(STYLE_PUSH_BUTTON_SETTINGS)
        self.push_button_exit.setStyleSheet(STYLE_PUSH_BUTTON_EXIT_DATABASE)

    def add_fixed_size_for_push_buttons(self) -> None:
        """Добавить фиксированный размер для кнопок."""
        self.push_button_material.setFixedSize(
            WIDTH_PUSH_BUTTON_MATERIAL, HEIGHT_PUSH_EDIT_MATERIAL
        )
        self.push_button_type_part.setFixedSize(
            WIDTH_PUSH_BUTTON_TYPE_PART, HEIGHT_PUSH_EDIT_TYPE_PART
        )
        self.push_button_pattern.setFixedSize(
            WIDTH_PUSH_BUTTON_PATTERN, HEIGHT_PUSH_EDIT_PATTERN
        )
        self.push_button_settings.setFixedSize(
            WIDTH_PUSH_BUTTON_SETTINGS, HEIGHT_PUSH_EDIT_SETTINGS
        )
        self.push_button_exit.setFixedSize(
            WIDTH_PUSH_BUTTON_DATABASE_EXIT, HEIGHT_PUSH_EDIT_DATABASE_EXIT
        )

    def add_name_objects_for_label(self) -> None:
        """Добавить название объектов для текста."""
        self.label_material.setObjectName(NAME_LABEL_MATERIAL_DATABASE)
        self.label_type_part.setObjectName(NAME_LABEL_TYPE_PART_DATABASE)
        self.label_pattern.setObjectName(NAME_LABEL_PATTERN_DATABASE)
        self.label_settings.setObjectName(NAME_LABEL_SETTINGS_DATABASE)
        self.label_exit.setObjectName(NAME_LABEL_EXIT_DATABASE)

    def add_style_for_label(self) -> None:
        """Добавить стиль для текста."""
        self.label_material.setStyleSheet(STYLE_LABEL_MATERIAL_DATABASE)
        self.label_type_part.setStyleSheet(STYLE_LABEL_TYPE_PART_DATABASE)
        self.label_pattern.setStyleSheet(STYLE_LABEL_PATTERN_DATABASE)
        self.label_settings.setStyleSheet(STYLE_LABEL_SETTINGS_DATABASE)
        self.label_exit.setStyleSheet(STYLE_LABEL_EXIT_DATABASE)

    def add_text_for_label(self) -> None:
        """Добавить текст для элемента текста."""
        self.label_material.setText("Материал:")
        self.label_type_part.setText("Класс детали:")
        self.label_pattern.setText("Шаблон:")
        self.label_settings.setText("Параметры:")
        self.label_exit.setText("Выход:")
