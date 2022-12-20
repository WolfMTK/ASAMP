from typing import List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCompleter

from database.material import Material
from database.part import Part
from interface.settings_widgets import SettingsWidgets
from interface.window_database import WindowDatabase


class Functional(SettingsWidgets):
    def __init__(self):
        super(Functional, self).__init__()
        self.list_part: List[str] = sorted(Part().get_part)
        self.list_material: List[str] = sorted(Material().get_material)
        self.list_brand: List[str | int] = None
        self.flag: bool = False
        self.window_database = WindowDatabase()
        self.add_functional()

    def add_functional(self) -> None:
        self.add_functional_push_button()
        self.add_functional_combo_box()

    def add_functional_push_button(self) -> None:
        # self.push_button_clear.clicked.connect()

        self.push_button_edit.clicked.connect(self.open_window_database)

        self.push_button_exit.clicked.connect(self.close)

        # self.push_button_result.clicked.connect()

        # self.push_button_save.clicked.connect()

    def add_functional_combo_box(self):
        self.combo_box_type_part.setEditable(True)
        copy_part = self.list_part.copy()
        copy_part.insert(0, '')
        self.combo_box_type_part.addItems(copy_part)
        self.combo_box_type_part.setCompleter(QCompleter(self.list_part))

        copy_material = self.list_material.copy()
        copy_material.insert(0, '')
        self.combo_box_material.setEditable(True)
        self.combo_box_material.addItems(copy_material)
        self.combo_box_material.setCompleter(QCompleter(self.list_material))
        self.combo_box_material.currentTextChanged.connect(self.change_flag)

    def make_active_combo_box(self) -> None:
        """Сделать активным комбинированную кнопку."""
        self.combo_box_brand.setEnabled(self.flag)
        self.combo_box_brand.clear()
        material = self.combo_box_material.currentText()
        if self.flag:
            self.list_brand = Material(material).get_brand()
            copy_brand = self.list_brand.copy()
            copy_brand.insert(0, '')
            self.combo_box_brand.setEditable(self.flag)
            self.combo_box_brand.addItems(copy_brand)
            self.combo_box_brand.setCompleter(QCompleter(self.list_brand))
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

    def change_flag(self):
        """Изменить ключ-флаг."""
        if self.combo_box_material.currentText() in self.list_material:
            self.flag = True
            return self.make_active_combo_box()
        self.flag = False
        return self.make_active_combo_box()

    def open_window_database(self):
        self.window_database.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.window_database.show()
