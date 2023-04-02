from PySide6.QtWidgets import QWidget, QHBoxLayout

from .elements import TextEditParameters, WidgetParameters
from .settings import NAME_WIDGET, NAME_TEXT_EDIT, WIDTH_WIDGET


class ResultWidget:
    def __init__(self, widget: QWidget) -> None:
        self.widget = WidgetParameters(
            widget, NAME_WIDGET, width=WIDTH_WIDGET, style=True
        ).widget
        self.__add_text_edit()
        self.__align_elemet()

    def __add_text_edit(self) -> None:
        self.text_edit_result = TextEditParameters(
            self.widget, NAME_TEXT_EDIT
        ).text_edit

    def __align_elemet(self) -> None:
        horizontal_layout = QHBoxLayout(self.widget)
        horizontal_layout.addWidget(self.text_edit_result)
        horizontal_layout.setContentsMargins(10, 10, 10, 10)
