from PySide6.QtWidgets import QGridLayout, QWidget

from .elements import PushButtonParameters, WidgetParameters
from .settings import (
    NAME_WIDGET,
    NAME_PUSH_BUTTON,
    WIDTH_WIDGET,
    HEIGHT_ACTION_WIDGET,
    WIDTH_PUSH_BUTTON,
    HEIGHT_PUSH_BUTTON,
)


class ActionWidget:
    def __init__(self, widget: QWidget) -> None:
        self.widget = WidgetParameters(
            widget,
            NAME_WIDGET,
            WIDTH_WIDGET,
            HEIGHT_ACTION_WIDGET,
            style=True,
        ).widget
        self.__add_push_button()
        self.__align_elements()

    def __add_push_button(self):
        self.push_button_clear = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON,
            HEIGHT_PUSH_BUTTON,
            style=True,
            text="ОЧИСТИТЬ",
        ).push_button
        self.push_button_close = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON,
            HEIGHT_PUSH_BUTTON,
            style=True,
            text="ВЫХОД",
        ).push_button
        self.push_button_result = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON,
            HEIGHT_PUSH_BUTTON,
            style=True,
            text="РЕЗУЛЬТАТ",
        ).push_button
        self.push_button_save = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON,
            HEIGHT_PUSH_BUTTON,
            style=True,
            text="СОХРАНИТЬ",
        ).push_button

    def __align_elements(self) -> None:
        grid_layout = QGridLayout(self.widget)
        grid_layout.addWidget(self.push_button_clear, 1, 0, 1, 1)
        grid_layout.addWidget(self.push_button_close, 1, 1, 1, 1)
        grid_layout.addWidget(self.push_button_result, 0, 0, 1, 1)
        grid_layout.addWidget(self.push_button_save, 0, 1, 1, 1)
