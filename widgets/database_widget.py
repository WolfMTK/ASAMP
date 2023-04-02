from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLayout

from .elements import PushButtonParameters, TableParameters, WidgetParameters
from .settings import (
    NAME_WIDGET,
    NAME_PUSH_BUTTON,
    NAME_TABLE_WIDGET,
    WIDTH_PUSH_BUTTON_WITH_IMAGE,
    HEIGHT_PUSH_BUTTON_WITH_IMAGE,
)


class WidgetELements:
    def __init__(self, widget: QWidget) -> None:
        self.widget = QWidget(widget)
        self.__add_push_buttons()
        self.__align_elemenets()

    def __add_push_buttons(self) -> None:
        self.push_button_add = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/add.png",
        ).push_button
        self.push_button_delete = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/clear.png",
        ).push_button
        self.push_button_save = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/save.png",
        ).push_button

    def __align_elemenets(self) -> None:
        horizontal_layout = QHBoxLayout(self.widget)
        horizontal_layout.addWidget(self.push_button_add)
        horizontal_layout.addWidget(self.push_button_delete)
        horizontal_layout.addWidget(self.push_button_save)
        horizontal_layout.setSizeConstraint(
            QLayout.SizeConstraint.SetFixedSize
        )


class DatabaseWidget:
    def __init__(self, widget: QWidget) -> None:
        self.widget = WidgetParameters(widget, NAME_WIDGET, style=True).widget
        self.__add_widget()
        self.__add_push_buttons()
        self.__add_table()
        self.__align_elements()

    def __add_widget(self) -> None:
        self.elements_widget = WidgetELements(self.widget)

    def __add_push_buttons(self) -> None:
        self.push_button_add = self.elements_widget.push_button_add
        self.push_button_delete = self.elements_widget.push_button_delete
        self.push_button_save = self.elements_widget.push_button_save

    def __add_table(self) -> None:
        self.table_database = TableParameters(
            self.widget, NAME_TABLE_WIDGET
        ).table

    def __align_elements(self) -> None:
        vertical_layout = QVBoxLayout(self.widget)
        vertical_layout.addWidget(self.table_database)
        vertical_layout.addWidget(self.elements_widget.widget)
