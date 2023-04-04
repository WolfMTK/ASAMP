from PySide6.QtWidgets import (
    QGridLayout,
    QWidget,
    QHBoxLayout,
)

from .elements import (
    PushButtonParameters,
    LabelParameters,
    ComboBoxParameters,
    LineEditParameters,
    WidgetParameters,
)
from .settings import (
    NAME_WIDGET,
    NAME_PUSH_BUTTON,
    NAME_LINE_EDIT,
    NAME_LABEL,
    NAME_COMBO_BOX,
    WIDTH_WIDGET,
    HEIGHT_PARAMETERS_WIDGET,
    WIDTH_PUSH_BUTTON_WITH_IMAGE,
    HEIGHT_PUSH_BUTTON_WITH_IMAGE,
    WIDTH_COMBO_BOX,
    HEIGHT_COMBO_BOX,
    WIDTH_LINE_EDIT,
    HEIGHT_LINE_EDIT,
)


class SettingsWindget:
    def __init__(self, widget: QWidget) -> None:
        self.widget = QWidget(widget)
        self.__add_push_button()
        self.__add_label()
        self.__align_elements()

    def __add_push_button(self) -> None:
        self.push_button_settings = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            WIDTH_PUSH_BUTTON_WITH_IMAGE,
            HEIGHT_PUSH_BUTTON_WITH_IMAGE,
            style_image=True,
            image_path="./icons/edit.png",
        ).push_button

    def __add_label(self) -> None:
        self.label_settings = LabelParameters(
            self.widget, NAME_LABEL, "Параметры:"
        ).label

    def __align_elements(self) -> None:
        horizontal_layout = QHBoxLayout(self.widget)
        horizontal_layout.addWidget(self.label_settings)
        horizontal_layout.addWidget(self.push_button_settings)
        horizontal_layout.setContentsMargins(110, 0, 110, 0)


class ParametersWidget:
    def __init__(self, widget: QWidget) -> None:
        self.widget = WidgetParameters(
            widget,
            NAME_WIDGET,
            WIDTH_WIDGET,
            HEIGHT_PARAMETERS_WIDGET,
            style=True,
        ).widget
        self.__add_widget()
        self.__add_push_button()
        self.__add_labels()
        self.__add_comobo_box()
        self.__add_line_edit()
        self.__align_elements()

    def __add_widget(self) -> None:
        self.widget_settings = SettingsWindget(self.widget)

    def __add_push_button(self) -> None:
        self.push_button_settings = self.widget_settings.push_button_settings

    def __add_labels(self) -> None:
        self.label_settings = self.widget_settings.label_settings
        self.label_material = LabelParameters(
            self.widget, NAME_LABEL, "Материал детали:"
        ).label
        self.label_brand = LabelParameters(
            self.widget, NAME_LABEL, "Марка:"
        ).label
        self.label_type_part = LabelParameters(
            self.widget, NAME_LABEL, "Класс детали:"
        ).label
        self.label_name_part = LabelParameters(
            self.widget, NAME_LABEL, "Название детали:"
        ).label

    def __add_comobo_box(self) -> None:
        self.combo_box_material = ComboBoxParameters(
            self.widget,
            NAME_COMBO_BOX,
            WIDTH_COMBO_BOX,
            HEIGHT_COMBO_BOX,
        ).combo_box
        self.combo_box_brand = ComboBoxParameters(
            self.widget,
            NAME_COMBO_BOX,
            WIDTH_COMBO_BOX,
            HEIGHT_COMBO_BOX,
        ).combo_box
        self.combo_box_type_part = ComboBoxParameters(
            self.widget,
            NAME_COMBO_BOX,
            WIDTH_COMBO_BOX,
            HEIGHT_COMBO_BOX,
        ).combo_box

    def __add_line_edit(self) -> None:
        self.line_edit_name_part = LineEditParameters(
            self.widget, NAME_LINE_EDIT, WIDTH_LINE_EDIT, HEIGHT_LINE_EDIT
        ).line_edit

    def __align_elements(self) -> None:
        grid_layout = QGridLayout(self.widget)
        grid_layout.addWidget(self.combo_box_material, 3, 1, 1, 1)
        grid_layout.addWidget(self.combo_box_brand, 4, 1, 1, 1)
        grid_layout.addWidget(self.combo_box_type_part, 2, 1, 1, 1)
        grid_layout.addWidget(self.label_material, 3, 0, 1, 1)
        grid_layout.addWidget(self.label_brand, 4, 0, 1, 1)
        grid_layout.addWidget(self.label_name_part, 0, 0, 1, 1)
        grid_layout.addWidget(self.label_type_part, 2, 0, 1, 1)
        grid_layout.addWidget(self.line_edit_name_part, 0, 1, 1, 1)
        grid_layout.addWidget(self.widget_settings.widget, 5, 0, 1, 2)
        grid_layout.setContentsMargins(10, 10, 10, 10)
