from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout

from name_objects.name_objects import NAME_RESULT_WIDGET, NAME_TEXT_EDIT_RESULT
from style.size_objects import WIDTH_RESULT_WIDGET, HEIGHT_RESULT_WIDGET
from style.style import STYLE_RESULT_WIDGET, STYLE_TEXT_EDIT_RESULT
from widgets.widget import Widget


class ResultWidget(Widget):
    """Виджет с результатом."""
    def __init__(self, widget: QWidget) -> None:
        self.widget = QWidget(widget)
        self.text_edit_result = QTextEdit(self.widget)
        self.horizontal_layout = QHBoxLayout(self.widget)
        self.add_objects_for_widget()

    def add_objects_for_widget(self) -> None:
        """Добавить объекты для виджета."""
        self.add_parameters_for_widget()
        self.add_parameters_for_text_edit()

    def add_parameters_for_widget(self) -> None:
        """Добавить параметры для виджета."""
        self.name_objets = NAME_RESULT_WIDGET
        self.style_widget = STYLE_RESULT_WIDGET
        self.add_name_for_objects()
        self.add_style()
        self.add_fixed_size_width_for_widget()
        self.add_horizontal_layout_for_widgets()

    def add_parameters_for_text_edit(self) -> None:
        """Добавить параметры для изменяемого текста."""
        self.add_name_objects_for_text_edit()
        self.add_style_for_text_edit()

    def add_fixed_size_width_for_widget(self) -> None:
        """Добавить фиксированные размеры для виджета."""
        self.widget.setFixedWidth(WIDTH_RESULT_WIDGET)

    def add_name_objects_for_text_edit(self) -> None:
        """Добавить название объектов для изменяемого текста."""
        self.text_edit_result.setObjectName(NAME_TEXT_EDIT_RESULT)

    def add_style_for_text_edit(self) -> None:
        """Добавить стиль для изменяемого текста."""
        self.text_edit_result.setStyleSheet(STYLE_TEXT_EDIT_RESULT)

    def add_horizontal_layout_for_widgets(self) -> None:
        """Добавить горизонтальное выравнивание для виджетов."""
        self.horizontal_layout.addWidget(self.text_edit_result)
        self.horizontal_layout.setContentsMargins(10, 10, 10, 10)
