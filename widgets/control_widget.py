from PySide6.QtWidgets import QGridLayout, QWidget

from .elements import PushButtonParameters, LabelParameters, WidgetParameters
from .settings import (
    NAME_WIDGET,
    NAME_PUSH_BUTTON,
    NAME_LABEL,
    WIDTH_PUSH_BUTTON_WITH_IMAGE,
    HEIGHT_PUSH_BUTTON_WITH_IMAGE,
    WIDTH_CONTROL_WIDGET,
    HEIGHT_CONTROL_WIDGET,
)


class ControlWidget:
    def __init__(self, widget: QWidget) -> None:
        self.widget = WidgetParameters(
            widget,
            NAME_WIDGET,
            width=WIDTH_CONTROL_WIDGET,
            height=HEIGHT_CONTROL_WIDGET,
            style=True,
        ).widget
        self.__add_labels()
        self.__add_push_buttons()
        self.__align_elements()

    def __add_labels(self) -> None:
        self.label_material = LabelParameters(
            self.widget, NAME_LABEL, "Материал:"
        ).label
        self.label_type_part = LabelParameters(
            self.widget, NAME_LABEL, "Класс детали:"
        ).label
        self.label_pattern = LabelParameters(
            self.widget, NAME_LABEL, "Параметры:"
        ).label
        self.label_settings = LabelParameters(
            self.widget, NAME_LABEL, "Параметры:"
        ).label
        self.label_exit = LabelParameters(
            self.widget, NAME_LABEL, "Выход:"
        ).label

    def __add_push_buttons(self) -> None:
        self.push_button_material = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/material.png",
        ).push_button
        self.push_button_type_part = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/part.png",
        ).push_button
        self.push_button_pattern = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/pattern.png",
        ).push_button
        self.push_button_settings = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/settings.png",
        ).push_button
        self.push_button_exit = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/exit.png",
        ).push_button

    def __align_elements(self) -> None:
        grid_layout = QGridLayout(self.widget)
        grid_layout.addWidget(self.label_material, 0, 0, 1, 1)
        grid_layout.addWidget(self.push_button_material, 0, 1, 1, 1)
        grid_layout.addWidget(self.label_type_part, 1, 0, 1, 1)
        grid_layout.addWidget(self.push_button_type_part, 1, 1, 1, 1)
        grid_layout.addWidget(self.label_settings, 2, 0, 1, 1)
        grid_layout.addWidget(self.push_button_settings, 2, 1, 1, 1)
        grid_layout.addWidget(self.label_pattern, 3, 0, 1, 1)
        grid_layout.addWidget(self.push_button_pattern, 3, 1, 1, 1)
        grid_layout.addWidget(self.label_exit, 4, 0, 1, 1)
        grid_layout.addWidget(self.push_button_exit, 4, 1, 1, 1)
