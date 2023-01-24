from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton

from name_objects.name_objects import (NAME_ACTION_WIDGET,
                                       NAME_PUSH_BUTTON_CLEAR,
                                       NAME_PUSH_BUTTON_EXIT,
                                       NAME_PUSH_BUTTON_RESULT,
                                       NAME_PUSH_BUTTON_SAVE)
from style.size_objects import WIDTH_ACTION_WIDGET, HEIGHT_ACTION_WIDGET
from style.style import (STYLE_ACTION_WIDGET, STYLE_PUSH_BUTTON_CLEAR,
                         STYLE_PUSH_BUTTON_RESULT, STYLE_PUSH_BUTTON_SAVE,
                         STYLE_PUSH_BUTTON_EXIT)
from widgets.widget import Widget


class ActionWidget(Widget):
    """Виджет с действиями."""

    def __init__(self, widget: QWidget) -> None:
        self.widget = QWidget(widget)
        self.grid_layout = QGridLayout(self.widget)
        self.push_button_clear = QPushButton(self.widget)
        self.push_button_exit = QPushButton(self.widget)
        self.push_button_result = QPushButton(self.widget)
        self.push_button_save = QPushButton(self.widget)
        self.add_objects_for_widget()

    def add_objects_for_widget(self) -> None:
        """Добавить объекты для виджета."""
        self.add_parameters_for_widget()
        self.add_name_objects_for_push_buttons()
        self.add_parameters_for_push_buttons()

    def add_parameters_for_widget(self) -> None:
        """Добавить параметры для виджета."""
        self.name_objets = NAME_ACTION_WIDGET
        self.style_widget = STYLE_ACTION_WIDGET
        self.add_name_for_objects()
        self.add_style()
        self.add_size_fixed_for_widget()
        self.add_grid_layout_for_widgets()

    def add_parameters_for_push_buttons(self) -> None:
        """Добавить параметры для кнопок."""
        self.add_style_for_push_buttons()
        self.add_text_in_push_buttons()

    def add_size_fixed_for_widget(self) -> None:
        """Добавить фиксированные размеры для виджета."""
        self.widget.setFixedSize(WIDTH_ACTION_WIDGET, HEIGHT_ACTION_WIDGET)

    def add_name_objects_for_push_buttons(self) -> None:
        """Добавить название объектов для кнопок."""
        self.push_button_clear.setObjectName(NAME_PUSH_BUTTON_CLEAR)
        self.push_button_exit.setObjectName(NAME_PUSH_BUTTON_EXIT)
        self.push_button_result.setObjectName(NAME_PUSH_BUTTON_RESULT)
        self.push_button_save.setObjectName(NAME_PUSH_BUTTON_SAVE)

    def add_style_for_push_buttons(self) -> None:
        """Добавить стиль для кнопок."""
        self.push_button_clear.setStyleSheet(STYLE_PUSH_BUTTON_CLEAR)
        self.push_button_exit.setStyleSheet(STYLE_PUSH_BUTTON_EXIT)
        self.push_button_result.setStyleSheet(STYLE_PUSH_BUTTON_RESULT)
        self.push_button_save.setStyleSheet(STYLE_PUSH_BUTTON_SAVE)

    def add_grid_layout_for_widgets(self) -> None:
        """Добавить выравнивание по сетке для виджетов."""
        self.grid_layout.addWidget(self.push_button_clear, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.push_button_exit, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.push_button_result, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.push_button_save, 0, 1, 1, 1)

    def add_text_in_push_buttons(self) -> None:
        """Добавить текст в кнопки."""
        self.push_button_clear.setText("ОЧИСТИТЬ")
        self.push_button_exit.setText("ВЫХОД")
        self.push_button_result.setText("РЕЗУЛЬТАТ")
        self.push_button_save.setText("СОХРАНИТЬ")
