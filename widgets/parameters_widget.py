from PySide6.QtWidgets import (QWidget,
                               QGridLayout,
                               QHBoxLayout,
                               QComboBox,
                               QLabel,
                               QLineEdit,
                               QPushButton)

from name_objects.name_objects import (NAME_PARAMETERS_WIDGET,
                                       NAME_PUSH_BUTTON_EDIT_DATABASE,
                                       NAME_LINE_EDIT_DATABASE_EDIT,
                                       NAME_LABEL_MATERIAL,
                                       NAME_LABEL_EDIT_DATABASE,
                                       NAME_LABEL_BRAND,
                                       NAME_LABEL_TYPE_PART,
                                       NAME_LABEL_NAME_PART,
                                       NAME_COMBO_BOX_MATERIAL,
                                       NAME_COMBO_BOX_BRAND,
                                       NAME_COMBO_BOX_TYPE_PART)
from style.size_objects import (WIDTH_PARAMETERS_WIDGET,
                                HEIGHT_PARAMETERS_WIDGET,
                                WIDTH_PUSH_BUTTON_EDIT_DATABASE,
                                HEIGHT_PUSH_EDIT_DATABASE,
                                WIDTH_COMBO_BOX_MATERIAL,
                                HEIGHT_COMBO_BOX_MATERIAL,
                                HEIGHT_COMBO_BOX_BRAND, WIDTH_COMBO_BOX_BRAND,
                                WIDTH_COMBO_BOX_TYPE_PART,
                                HEIGHT_COMBO_BOX_TYPE_PART)
from style.style import (STYLE_PARAMETERS_WIDGET,
                         STYLE_PUSH_BUTTON_EDIT_DATABASE,
                         STYLE_LINE_EDIT_DATABASE,
                         STYLE_LABEL_BRAND,
                         STYLE_LABEL_EDIT_DATABASE,
                         STYLE_LABEL_MATERIAL,
                         STYLE_LABEL_TYPE_PART,
                         STYLE_LABEL_NAME_PART,
                         STYLE_COMBO_BOX_MATERIAL,
                         STYLE_COMBO_BOX_BRAND,
                         STYLE_COMBO_BOX_TYPE_PART)
from widgets.widget import Widget


class ParametersWidget(Widget):
    """Виджет с параметрами."""

    def __init__(self, widget: QWidget = None) -> None:
        self.widget = QWidget(widget)
        self.widget_edit_database = QWidget(self.widget)
        self.horizontal_layout = QHBoxLayout(self.widget_edit_database)
        self.grid_layout = QGridLayout(self.widget)
        self.label_edit_database = QLabel(self.widget_edit_database)
        self.label_material = QLabel(self.widget)
        self.label_brand = QLabel(self.widget)
        self.label_type_part = QLabel(self.widget)
        self.label_name_part = QLabel(self.widget)
        self.combo_box_material = QComboBox(self.widget)
        self.combo_box_brand = QComboBox(self.widget)
        self.combo_box_type_part = QComboBox(self.widget)
        self.push_button_edit_database = QPushButton(
            self.widget_edit_database
        )
        self.line_edit_name_part = QLineEdit(self.widget)
        self.add_objects_for_widget()

    def add_objects_for_widget(self) -> None:
        """Добавить объекты для виджета."""
        self.add_parameters_for_widget()
        self.add_parameters_for_push_button()
        self.add_parameters_for_line_edit()
        self.add_parameters_for_label()
        self.add_parameters_for_combo_boxes()

    def add_parameters_for_widget(self) -> None:
        """Добавить параметры для виджета."""
        self.name_objets = NAME_PARAMETERS_WIDGET
        self.style_widget = STYLE_PARAMETERS_WIDGET
        self.add_name_for_objects()
        self.add_style()
        self.add_fixed_size_for_widget()
        self.add_grid_layout_for_widgets()
        self.add_horizontal_layout_for_widgets()

    def add_parameters_for_push_button(self) -> None:
        """Добавить параметры для кнопки."""
        self.add_name_objects_for_push_button()
        self.add_style_for_push_button()
        self.add_fixed_size_for_push_button()

    def add_parameters_for_line_edit(self) -> None:
        """Добавить параметры для поля изменения текста."""
        self.add_name_objects_for_line_edit()
        self.add_style_for_line_edit()
        self.add_size_for_line_edit()

    def add_parameters_for_label(self) -> None:
        """Добавить параметры для элементов текста."""
        self.add_name_objects_for_label()
        self.add_style_for_label()
        self.add_text_for_label()

    def add_parameters_for_combo_boxes(self) -> None:
        """Добавить параметры для комбинированных кнопок."""
        self.add_name_objects_for_combo_boxes()
        self.add_style_for_combo_boxes()
        self.add_fixed_size_for_combo_boxes()

    def add_fixed_size_for_widget(self) -> None:
        """Добавить фиксированные размеры для виджета."""
        self.widget.setFixedSize(WIDTH_PARAMETERS_WIDGET,
                                 HEIGHT_PARAMETERS_WIDGET)

    def add_grid_layout_for_widgets(self) -> None:
        """Добавить выравнивание по сетке для виджетов."""
        self.grid_layout.addWidget(self.combo_box_material, 3, 1, 1, 1)
        self.grid_layout.addWidget(self.combo_box_brand, 4, 1, 1, 1)
        self.grid_layout.addWidget(self.combo_box_type_part, 2, 1, 1, 1)
        self.grid_layout.addWidget(self.label_material, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.label_brand, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.label_name_part, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.label_type_part, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.line_edit_name_part, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.widget_edit_database, 5, 0, 1, 2)
        self.grid_layout.setContentsMargins(10, 10, 10, 10)

    def add_horizontal_layout_for_widgets(self) -> None:
        """Добавить горизонтальное выравнивание для виджетов."""
        self.horizontal_layout.addWidget(self.label_edit_database)
        self.horizontal_layout.addWidget(self.push_button_edit_database)
        self.horizontal_layout.setContentsMargins(55, 0, 130, 0)

    def add_name_objects_for_push_button(self) -> None:
        """Добавить название объектов для кнопки."""
        self.push_button_edit_database.setObjectName(
            NAME_PUSH_BUTTON_EDIT_DATABASE
        )

    def add_style_for_push_button(self) -> None:
        """Добавить стиль для кнопки."""
        self.push_button_edit_database.setStyleSheet(
            STYLE_PUSH_BUTTON_EDIT_DATABASE
        )

    def add_fixed_size_for_push_button(self) -> None:
        """Добавить фиксированный размер для кнопки."""
        self.push_button_edit_database.setFixedSize(
            WIDTH_PUSH_BUTTON_EDIT_DATABASE, HEIGHT_PUSH_EDIT_DATABASE
        )

    def add_name_objects_for_line_edit(self) -> None:
        """Добавить название объектов для поля изменения текста."""
        self.line_edit_name_part.setObjectName(NAME_LINE_EDIT_DATABASE_EDIT)

    def add_style_for_line_edit(self) -> None:
        """Добавить стиль для поля изменения текста"""
        self.line_edit_name_part.setStyleSheet(STYLE_LINE_EDIT_DATABASE)

    def add_size_for_line_edit(self) -> None:
        """Добавить размеры для поля изменения текста."""
        self.line_edit_name_part.setFixedSize(230, 30)

    def add_name_objects_for_label(self) -> None:
        """Добавить название объектов для текста."""
        self.label_material.setObjectName(NAME_LABEL_MATERIAL)
        self.label_edit_database.setObjectName(NAME_LABEL_EDIT_DATABASE)
        self.label_brand.setObjectName(NAME_LABEL_BRAND)
        self.label_type_part.setObjectName(NAME_LABEL_TYPE_PART)
        self.label_name_part.setObjectName(NAME_LABEL_NAME_PART)

    def add_style_for_label(self) -> None:
        """Добавить стиль для текста."""
        self.label_material.setStyleSheet(STYLE_LABEL_MATERIAL)
        self.label_edit_database.setStyleSheet(STYLE_LABEL_EDIT_DATABASE)
        self.label_brand.setStyleSheet(STYLE_LABEL_BRAND)
        self.label_type_part.setStyleSheet(STYLE_LABEL_TYPE_PART)
        self.label_name_part.setStyleSheet(STYLE_LABEL_NAME_PART)

    def add_text_for_label(self) -> None:
        """Добавить текст для элемента текста."""
        self.label_material.setText("Материал детали:")
        self.label_edit_database.setText("Редактирование БД:")
        self.label_brand.setText("Марка:")
        self.label_type_part.setText("Класс детали:")
        self.label_name_part.setText("Название детали:")

    def add_name_objects_for_combo_boxes(self) -> None:
        """Добавить название объектов для комбинированных кнопок."""
        self.combo_box_material.setObjectName(NAME_COMBO_BOX_MATERIAL)
        self.combo_box_brand.setObjectName(NAME_COMBO_BOX_BRAND)
        self.combo_box_type_part.setObjectName(NAME_COMBO_BOX_TYPE_PART)

    def add_style_for_combo_boxes(self) -> None:
        """Добавить стиль для комбинированных кнопок."""
        self.combo_box_material.setStyleSheet(STYLE_COMBO_BOX_MATERIAL)
        self.combo_box_brand.setStyleSheet(STYLE_COMBO_BOX_BRAND)
        self.combo_box_type_part.setStyleSheet(STYLE_COMBO_BOX_TYPE_PART)

    def add_fixed_size_for_combo_boxes(self) -> None:
        """Добавить фиксированный размер
        для комбинированных кнопок."""
        self.combo_box_material.setFixedSize(WIDTH_COMBO_BOX_MATERIAL,
                                             HEIGHT_COMBO_BOX_MATERIAL)
        self.combo_box_brand.setFixedSize(WIDTH_COMBO_BOX_BRAND,
                                          HEIGHT_COMBO_BOX_BRAND)
        self.combo_box_type_part.setFixedSize(WIDTH_COMBO_BOX_TYPE_PART,
                                              HEIGHT_COMBO_BOX_TYPE_PART)
