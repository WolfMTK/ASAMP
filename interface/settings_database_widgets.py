from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLayout

from interface.widgets.functional_database_widget import FunctionalDatabaseWidget
from interface.widgets.table_database_widget import TableDatabaseWidget


class SettingsDatabaseWidget(FunctionalDatabaseWidget, TableDatabaseWidget):
    def __init__(self):
        super(SettingsDatabaseWidget, self).__init__()
        self.add_settings()

    def add_settings(self):
        self.set_label()
        self.set_push_button()
        self.set_widget()
        self.set_table()
        self.set_grid_layout()
        self.set_horizontal_layout()
        self.set_vertical_layout()

    def set_widget(self):
        self.database_widget.setObjectName('widgetDatabase')
        style_database_widget = '''
        #widgetDatabase{
            background-color: #d9d9d9;
        }
        '''
        self.database_widget.setStyleSheet(style_database_widget)

        self.functional_widget.setObjectName('widgetFunctional')
        self.functional_widget.setFixedSize(200, 250)
        style_functional_widget = '''
            #widgetFunctional{
            background-color: white;
            border-radius: 10px;
        }
        '''
        self.functional_widget.setStyleSheet(style_functional_widget)

        self.table_database_widget.setObjectName('widgetDatabaseTable')
        style_table_database_widget = '''
        #widgetDatabaseTable{
            background-color: white;
            border-radius: 10px;
        }
        '''
        self.table_database_widget.setStyleSheet(style_table_database_widget)

        self.table_widget.setObjectName('widgetTable')
        style_table_widget = '''
        #widgetTable{
            background-color: white;
            border-radius: 10px;
        }
        '''
        self.table_widget.setStyleSheet(style_table_widget)

        self.button_widget.setObjectName('widgetButton')
        style_button_widget = '''
        #widgetButton{
            background-color: white;
            border-radius: 10px;
        }
        '''
        self.button_widget.setStyleSheet(style_button_widget)

    def set_grid_layout(self):
        self.grid_layout_database.addWidget(self.functional_widget, 0, 0, 1, 1)
        self.grid_layout_database.addWidget(self.table_database_widget, 0, 1, 2, 1)

        self.grid_layout_functional.addWidget(self.label_material, 0, 0, 1, 1)
        self.grid_layout_functional.addWidget(self.push_button_material, 0, 1, 1, 1)
        self.grid_layout_functional.addWidget(self.label_type_part, 1, 0, 1, 1)
        self.grid_layout_functional.addWidget(self.push_button_type_part, 1, 1, 1, 1)
        self.grid_layout_functional.addWidget(self.label_settings, 2, 0, 1, 1)
        self.grid_layout_functional.addWidget(self.push_button_settings, 2, 1, 1, 1)
        self.grid_layout_functional.addWidget(self.label_pattern, 3, 0, 1, 1)
        self.grid_layout_functional.addWidget(self.push_button_pattern, 3, 1, 1, 1)
        self.grid_layout_functional.addWidget(self.label_exit, 4, 0, 1, 1)
        self.grid_layout_functional.addWidget(self.push_button_exit, 4, 1, 1, 1)

    def set_label(self):
        self.label_material.setObjectName('labelMaterial')
        self.label_material.setText('Материал:')
        style_label_material = '''
        #labelMaterial{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_material.setStyleSheet(style_label_material)

        self.label_type_part.setObjectName('labelTypePart')
        self.label_type_part.setText('Класс детали:')
        style_label_type_part = '''
        #labelTypePart{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_type_part.setStyleSheet(style_label_type_part)

        self.label_pattern.setObjectName('labelPattern')
        self.label_pattern.setText('Шаблон:')
        style_label_pattern = '''
        #labelPattern{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_pattern.setStyleSheet(style_label_pattern)

        self.label_settings.setObjectName('labelSettings')
        self.label_settings.setText('Параметры:')
        style_label_settings = '''
        #labelSettings{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_settings.setStyleSheet(style_label_settings)

        self.label_exit.setObjectName('labelExit')
        self.label_exit.setText('Выход:')
        style_label_exit = '''
        #labelExit{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_exit.setStyleSheet(style_label_exit)

    def set_push_button(self):
        self.push_button_material.setObjectName('pushButtonMaterial')
        self.push_button_material.setFixedSize(37, 35)
        style_material = '''
        #pushButtonMaterial{
            background-color: rgba(0, 0, 0, 0);
            image: url(./icon/material.png);
            border-radius: 10px;
            font-size: 12px;
            font-family: bold "Times New Roman";
        }

        #pushButtonMaterial::hover{
            background-color: #e3e3e3;
        }

        #pushButtonMaterial::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_material.setStyleSheet(style_material)

        self.push_button_type_part.setObjectName('pushButtonTypePart')
        self.push_button_type_part.setFixedSize(37, 35)
        style_type_part = '''
        #pushButtonTypePart{
            background-color: rgba(0, 0, 0, 0);
            image: url(./icon/part.png);
            border-radius: 10px;
            font-size: 12px;
            font-family: bold "Times New Roman";
        }

        #pushButtonTypePart::hover{
            background-color: #e3e3e3;
        }

        #pushButtonTypePart::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_type_part.setStyleSheet(style_type_part)

        self.push_button_settings.setObjectName('pushButtonSettings')
        self.push_button_settings.setFixedSize(37, 35)
        style_settings = '''
        #pushButtonSettings{
            background-color: rgba(0, 0, 0, 0);
            image: url(./icon/settings.png);
            border-radius: 10px;
            font-size: 12px;
            font-family: bold "Times New Roman";
        }

        #pushButtonSettings::hover{
            background-color: #e3e3e3;
        }

        #pushButtonSettings::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_settings.setStyleSheet(style_settings)

        self.push_button_exit.setObjectName('pushButtonExitTable')
        self.push_button_exit.setFixedSize(37, 35)
        style_exit = '''
        #pushButtonExitTable{
            background-color: rgba(0, 0, 0, 0);
            image: url(./icon/exit.png);
            border-radius: 10px;
            font-size: 12px;
            font-family: bold "Times New Roman";
        }

        #pushButtonExitTable::hover{
            background-color: #e3e3e3;
        }

        #pushButtonExitTable::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_exit.setStyleSheet(style_exit)

        self.push_button_pattern.setObjectName('pushButtonPattern')
        self.push_button_pattern.setFixedSize(37, 35)
        style_pattern = '''
        #pushButtonPattern{
            background-color: rgba(0, 0, 0, 0);
            image: url(./icon/pattern.png);
            border-radius: 10px;
            font-size: 12px;
            font-family: bold "Times New Roman";
        }

        #pushButtonPattern::hover{
            background-color: #e3e3e3;
        }

        #pushButtonPattern::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_pattern.setStyleSheet(style_pattern)

        self.push_button_add.setObjectName('pushButtonAdd')
        self.push_button_add.setFixedSize(35, 30)
        style_add = '''
        #pushButtonAdd{
            background-color: rgba(0, 0, 0, 0);
            image: url(./icon/add.png);
            border-radius: 10px;
            font-size: 12px;
            font-family: bold "Times New Roman";
        }

        #pushButtonAdd::hover{
            background-color: #e3e3e3;
        }

        #pushButtonAdd::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_add.setStyleSheet(style_add)

        self.push_button_clear.setObjectName('pushButtonClear')
        self.push_button_clear.setFixedSize(35, 30)
        style_clear = '''
        #pushButtonClear{
            background-color: rgba(0, 0, 0, 0);
            image: url(./icon/clear.png);
            border-radius: 10px;
            font-size: 12px;
            font-family: bold "Times New Roman";
        }

        #pushButtonClear::hover{
            background-color: #e3e3e3;
        }

        #pushButtonClear::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_clear.setStyleSheet(style_clear)

        self.push_button_save.setObjectName('pushButtonSave')
        self.push_button_save.setFixedSize(35, 30)
        style_save = '''
        #pushButtonSave{
            background-color: rgba(0, 0, 0, 0);
            image: url(./icon/save.png);
            border-radius: 10px;
            font-size: 12px;
            font-family: bold "Times New Roman";
        }

        #pushButtonSave::hover{
            background-color: #e3e3e3;
        }

        #pushButtonSave::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_save.setStyleSheet(style_save)

    def set_table(self):
        self.table_database.setObjectName('tableDatabase')
        style = '''
        #tableDatabase{
            background-color: white;
            border-radius: 10px;
            font-size: 20px;
            font-family: bold "Times New Roman";
        }
        '''
        self.table_database.setStyleSheet(style)

    def set_horizontal_layout(self):
        self.h_layout_table.addWidget(self.table_database)

        self.h_layout_button.addWidget(self.push_button_add, Qt.AlignmentFlag.AlignRight)
        self.h_layout_button.addWidget(self.push_button_clear, Qt.AlignmentFlag.AlignRight)
        self.h_layout_button.addWidget(self.push_button_save, Qt.AlignmentFlag.AlignRight)
        self.h_layout_button.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

    def set_vertical_layout(self):
        self.v_layout_database_table.addWidget(self.table_widget)
        self.v_layout_database_table.addWidget(self.button_widget)
