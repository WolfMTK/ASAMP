from interface.widgets.entry_widget import EntryWidget
from interface.widgets.functional_widget import FunctionalWidget
from interface.widgets.result_widget import ResultWidget
from interface.widgets.selection_widget import SelectionWidget


class SettingsWidgets(FunctionalWidget,
                      ResultWidget,
                      EntryWidget,
                      SelectionWidget):
    def __init__(self) -> None:
        super(SettingsWidgets, self).__init__()
        self.add_settings()

    def add_settings(self) -> None:
        self.set_grid_layouts()
        self.set_widgets()
        self.set_push_buttons()
        self.set_text_edit()
        self.set_horizontal_layout()
        self.set_table()
        self.set_labels()
        self.set_vertical_layout()
        self.set_combo_box()
        self.set_line_edit()

    def set_grid_layouts(self):
        """Настройка выравнивания по сетке."""
        self.grid_layout_central.addWidget(self.functional_widget, 2, 0, 1, 1)
        self.grid_layout_central.addWidget(self.result_widget, 0, 1, 3, 1)
        self.grid_layout_central.addWidget(self.selection_widget, 1, 0, 1, 1)
        self.grid_layout_central.addWidget(self.entry_widget, 0, 0, 1, 1)

        self.grid_layout_functional.addWidget(
            self.push_button_save, 0, 1, 1, 1
        )
        self.grid_layout_functional.addWidget(
            self.push_button_exit, 1, 1, 1, 1
        )
        self.grid_layout_functional.addWidget(
            self.push_button_clear, 1, 0, 1, 1
        )
        self.grid_layout_functional.addWidget(
            self.push_button_result, 0, 0, 1, 1
        )

        self.grid_layout_entry.addWidget(
            self.combo_box_material, 3, 1, 1, 1
        )
        self.grid_layout_entry.addWidget(
            self.combo_box_brand, 4, 1, 1, 1
        )
        self.grid_layout_entry.addWidget(self.combo_box_type_part, 2, 1, 1, 1)
        self.grid_layout_entry.addWidget(self.label_material, 3, 0, 1, 1)
        self.grid_layout_entry.addWidget(self.label_brand, 4, 0, 1, 1)
        self.grid_layout_entry.addWidget(self.label_name_part, 0, 0, 1, 1)
        self.grid_layout_entry.addWidget(self.label_type_part, 2, 0, 1, 1)
        self.grid_layout_entry.addWidget(self.line_edit_name_part, 0, 1, 1, 1)
        self.grid_layout_entry.setContentsMargins(10, 10, 10, 10)
        self.grid_layout_entry.addWidget(self.edit_widget, 5, 0, 1, 2)

    def set_widgets(self):
        """Настройка виджетов."""
        self.central_widget.setObjectName('centralWidget')
        style_central_widget = '''
        #centralWidget{
            background-color: #d9d9d9;
        }
        '''
        self.central_widget.setStyleSheet(style_central_widget)

        self.functional_widget.setObjectName('functionalWidget')
        self.functional_widget.setFixedSize(400, 90)
        style_functional_widget = '''
        #functionalWidget{
            background-color: white;
            border-radius: 10px;
        }
        '''
        self.functional_widget.setStyleSheet(style_functional_widget)

        self.result_widget.setObjectName('widgetResult')
        style_result_widget = '''
        #widgetResult{
            background-color: white;
            border-radius: 10px;
        }
        '''
        self.result_widget.setStyleSheet(style_result_widget)

        self.selection_widget.setObjectName('widgetSelection')
        self.selection_widget.setFixedWidth(400)
        style_selection_widget = '''
        #widgetSelection{
            background-color: white;
            border-radius: 10px;
        }
        '''
        self.selection_widget.setStyleSheet(style_selection_widget)

        self.entry_widget.setObjectName('widgetEntry')
        self.entry_widget.setFixedSize(400, 220)
        style_entry_widget = '''
        #widgetEntry{
            background-color: white;
            border-radius: 10px;
        }
        '''
        self.entry_widget.setStyleSheet(style_entry_widget)

    def set_push_buttons(self):
        """Настройка кнопок."""
        self.push_button_clear.setObjectName('pushButtonClear')
        self.push_button_clear.setFixedSize(150, 30)
        self.push_button_clear.setText('Сбросить')
        style_clear = '''
        #pushButtonClear{
            background-color: rgba(0, 0, 0, 0);
            border-radius: 10px;
            font-size: 20px;
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

        self.push_button_result.setObjectName('pushButtonResult')
        self.push_button_result.setFixedSize(150, 30)
        self.push_button_result.setText('Результат')
        style_result = '''
        #pushButtonResult{
            background-color: rgba(0, 0, 0, 0);
            border-radius: 10px;
            font-size: 20px;
            font-family: bold "Times New Roman";
        }

        #pushButtonResult::hover{
            background-color: #e3e3e3;
        }

        #pushButtonResult::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_result.setStyleSheet(style_result)

        self.push_button_save.setObjectName('pushButtonSave')
        self.push_button_save.setFixedSize(150, 30)
        self.push_button_save.setText('Сохранить')
        style_save = '''
        #pushButtonSave{
            background-color: rgba(0, 0, 0, 0);
            border-radius: 10px;
            font-size: 20px;
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

        self.push_button_exit.setObjectName('pushButtonExit')
        self.push_button_exit.setFixedSize(150, 30)
        self.push_button_exit.setText('Выход')
        style_exit = '''
        #pushButtonExit{
            background-color: rgba(0, 0, 0, 0);
            border-radius: 10px;
            font-size: 20px;
            font-family: bold "Times New Roman";
        }

        #pushButtonExit::hover{
            background-color: #e3e3e3;
        }

        #pushButtonExit::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_exit.setStyleSheet(style_exit)

        self.push_button_edit.setObjectName('pushButtonEdit')
        self.push_button_edit.setFixedSize(40, 30)
        style_edit = '''
        #pushButtonEdit{
            background-color: rgba(0, 0, 0, 0);
            border-radius: 5px;
            image: url(./icon/edit.png);
            font-size: 20px;
            font-family: bold "Times New Roman";
        }

        #pushButtonEdit::hover{
            background-color: #f7f7f7;;
        }

        #pushButtonEdit::pressed{
            background-color: #c9f5ff;
        }
        '''
        self.push_button_edit.setStyleSheet(style_edit)

    def set_text_edit(self):
        """Настройка изменяемого текста."""
        self.text_edit_result.setObjectName('textEditResult')
        self.text_edit_result.setEnabled(False)
        style_text_edit = '''
        #textEditResult{
            background-color: white;
            border-radius: 10px;
            font-size: 20px;
            font-family: bold "Times New Roman";
        }
        '''
        self.text_edit_result.setStyleSheet(style_text_edit)

    def set_horizontal_layout(self):
        """Настройка горизонтального выравнивания."""
        self.h_layout_result.addWidget(self.text_edit_result)
        self.h_layout_result.setContentsMargins(10, 10, 10, 10)

        self.h_layout_edit.addWidget(
            self.label_edit
        )
        self.h_layout_edit.addWidget(
            self.push_button_edit
        )
        self.h_layout_edit.setContentsMargins(55, 0, 130, 0)

    def set_table(self):
        """Настройка таблицы."""
        self.table_analysis.setObjectName('tableAnalysis')
        style_analysis = '''
        #tableAnalysis{
            background-color: white;
            border-radius: 10px;
            font-size: 20px;
            font-family: bold "Times New Roman";
        }
        '''
        self.table_analysis.setStyleSheet(style_analysis)

    def set_labels(self):
        """Настрока текста."""
        self.label_analysis.setObjectName('labelAnalysis')
        self.label_analysis.setText('Анализ технологичности детали')
        style_label_analysis = '''
        #labelAnalysis{
            font-size: 20px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_analysis.setStyleSheet(style_label_analysis)

        self.label_material.setObjectName('labelMaterial')
        self.label_material.setText('Материал детали:')
        style_label_material = '''
        #labelMaterial{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_material.setStyleSheet(style_label_material)

        self.label_brand.setObjectName('labelBrand')
        self.label_brand.setText('Марка:')
        style_label_brand = '''
        #labelBrand{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_brand.setStyleSheet(style_label_brand)

        self.label_name_part.setObjectName('labelNamePart')
        self.label_name_part.setText('Название детали:')
        style_name_part = '''
        #labelNamePart{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_name_part.setStyleSheet(style_name_part)

        self.label_type_part.setObjectName('labelTypePart')
        self.label_type_part.setText('Класс детали:')
        style_type_part = '''
        #labelTypePart{
            font-size: 15px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_type_part.setStyleSheet(style_type_part)

        self.label_edit.setObjectName('labelEdit')
        self.label_edit.setText('Редактирование БД:')
        style_label_edit = '''
        #labelEdit{
            font-size: 16px;
            font-family: bold "Times New Roman";
        }
        '''
        self.label_edit.setStyleSheet(style_label_edit)

    def set_vertical_layout(self):
        """Настройка вертикального выравнивания."""
        self.v_layout_selection.addWidget(self.label_analysis)
        self.v_layout_selection.addWidget(self.table_analysis)

    def set_combo_box(self):
        """Настройка комбинированной кнопки."""
        self.combo_box_material.setObjectName('comboBoxMaterial')
        self.combo_box_material.setFixedSize(230, 30)
        style_material = '''
        #comboBoxMaterial{
            border: 1px solid #ced4da;
            border-radius: 10px;
            padding-left: 5px;
            font-size: 14px;
            font-family: bold "Times New Roman";
        }

        #comboBoxMaterial::drop-down{
            border: 0px;
        }

        #comboBoxMaterial::down-arrow{
            image: url(./icon/down_arrow.png);
            width: 20px;
            height: 20px;
            margin-right: 8px;
        }

        #comboBoxMaterial:on{
            border: 4px solid #e5e5e5;
        }

        #comboBoxMaterial QListView{
            font-size: 12px;
            border: 1px solid rgba(0, 0, 0, 10%);
            padding: 5px;
            background-color: #fff;
            outline: 0px;
        }

        #comboBoxMaterial QListView::item{
            padding-left: 10px;
            background-color: #fff;
        }

        #comboBoxMaterial QListView::item:hover{
            background-color: #1e90ff;
        }

        #comboBoxMaterial QListView::item:selected{
            background-color: #1e90ff;
        }
        '''
        self.combo_box_material.setStyleSheet(style_material)

        self.combo_box_brand.setObjectName('comboBoxBrand')
        self.combo_box_brand.setFixedSize(230, 30)
        style_brand = '''
        #comboBoxBrand{
            border: 1px solid #ced4da;
            border-radius: 10px;
            padding-left: 5px;
            font-size: 14px;
            font-family: bold "Times New Roman";
        }

        #comboBoxBrand::drop-down{
            border: 0px;
        }

        #comboBoxBrand::down-arrow{
            image: url(./icon/down_arrow.png);
            width: 20px;
            height: 20px;
            margin-right: 8px;
        }

        #comboBoxBrand:on{
            border: 4px solid #e5e5e5;
        }

        #comboBoxBrand QListView{
            font-size: 12px;
            border: 1px solid rgba(0, 0, 0, 10%);
            padding: 5px;
            background-color: #fff;
            outline: 0px;
        }

        #comboBoxBrand QListView::item{
            padding-left: 10px;
            background-color: #fff;
        }

        #comboBoxBrand QListView::item:hover{
            background-color: #1e90ff;
        }

        #comboBoxBrand QListView::item:selected{
            background-color: #1e90ff;
        }
        '''
        self.combo_box_brand.setStyleSheet(style_brand)

        self.combo_box_type_part.setObjectName('comboBoxTypePart')
        self.combo_box_type_part.setFixedSize(230, 30)
        style_type_part = '''
        #comboBoxTypePart{
            border: 1px solid #ced4da;
            border-radius: 10px;
            padding-left: 5px;
            font-size: 14px;
            font-family: bold "Times New Roman";
        }

        #comboBoxTypePart::drop-down{
            border: 0px;
        }

        #comboBoxTypePart::down-arrow{
            image: url(./icon/down_arrow.png);
            width: 20px;
            height: 20px;
            margin-right: 8px;
        }

        #comboBoxTypePart:on{
            border: 4px solid #e5e5e5;
        }

        #comboBoxTypePart QListView{
            font-size: 12px;
            border: 1px solid rgba(0, 0, 0, 10%);
            padding: 5px;
            background-color: #fff;
            outline: 0px;
        }

        #comboBoxTypePart QListView::item{
            padding-left: 10px;
            background-color: #fff;
        }

        #comboBoxTypePart QListView::item:hover{
            background-color: #1e90ff;
        }

        #comboBoxTypePart QListView::item:selected{
            background-color: #1e90ff;
        }
        '''
        self.combo_box_type_part.setStyleSheet(style_type_part)

    def set_line_edit(self):
        """Настройка изменяемого поля текста."""
        self.line_edit_name_part.setObjectName('lineEditNamePart')
        self.line_edit_name_part.setFixedSize(230, 30)
        style = '''
        #lineEditNamePart{
            font-size: 14px;
            font-family: bold "Times New Roman";
            border: 1px solid #ced4da;
            border-radius: 10px;
            padding-left: 5px;
            padding-right: 5px;
        }
        '''
        self.line_edit_name_part.setStyleSheet(style)
