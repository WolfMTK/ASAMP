from PySide6.QtWidgets import (
    QGridLayout,
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLayout,
)

from .elements import (
    PushButtonParameters,
    LabelParameters,
    ComboBoxParameters,
    LineEditParameters,
    TextEditParameters,
    TableParameters,
    WidgetParameters,
)
from .settings import (
    NAME_WIDGET,
    NAME_PUSH_BUTTON,
    NAME_LINE_EDIT,
    NAME_LABEL,
    NAME_COMBO_BOX,
    NAME_TEXT_EDIT,
    NAME_TABLE_WIDGET,
    WIDTH_WIDGET,
    HEIGHT_ACTION_WIDGET,
    HEIGHT_PARAMETERS_WIDGET,
    WIDTH_PUSH_BUTTON,
    HEIGHT_PUSH_BUTTON,
    WIDTH_PUSH_BUTTON_WITH_IMAGE,
    HEIGHT_PUSH_BUTTON_WITH_IMAGE,
    WIDTH_COMBO_BOX,
    HEIGHT_COMBO_BOX,
    WIDTH_LINE_EDIT,
    HEIGHT_LINE_EDIT,
    WIDTH_CONTROL_WIDGET,
    HEIGHT_CONTROL_WIDGET,
)


class CentralWidget:
    def __init__(self, window: QMainWindow) -> None:
        self.widget = WidgetParameters(
            window, NAME_WIDGET, style_central_widget=True
        ).widget


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

    def __align_elements(self):
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

    def __add_widget(self):
        self.widget_settings = SettingsWindget(self.widget)

    def __add_push_button(self):
        self.push_button_settings = self.widget_settings.push_button_settings

    def __add_labels(self):
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

    def __align_elements(self):
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


class DataWidget:
    def __init__(self, widget: QWidget) -> None:
        self.widget = WidgetParameters(widget, NAME_WIDGET, style=True).widget
        self.__add_table()
        self.__add_label()
        self.__align_elements()

    def __add_table(self) -> None:
        self.table_analysis = TableParameters(
            self.widget, NAME_TABLE_WIDGET
        ).table

    def __add_label(self) -> None:
        self.label_analysis = LabelParameters(
            self.widget, NAME_LABEL, "Анализ технологичности детали"
        ).label

    def __align_elements(self) -> None:
        vertical_layout = QVBoxLayout(self.widget)
        vertical_layout.addWidget(self.label_analysis)
        vertical_layout.addWidget(self.table_analysis)


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
