from interface.settings_database_widgets import SettingsDatabaseWidget


class Functional(SettingsDatabaseWidget):
    """Функционал для виждетов."""

    def __init__(self):
        super(Functional, self).__init__()
        self.row: int = None
        self.col: int = None
        self.key: bool = False
        self.add_functional()

    def add_functional(self):
        """Добавление функционала."""
        self.add_functional_button()
        self.show_table_material()

    def add_functional_button(self):
        """Добавление функционала для кнопок."""
        self.push_button_exit.clicked.connect(self.close)
        # self.push_button_add
        # self.push_button_clear
        self.push_button_material.clicked.connect(self.active_key_material)
        # self.push_button_pattern
        # self.push_button_save
        # self.push_button_settings
        # self.push_button_type_part

    def active_key_material(self) -> None:
        """Активация ключи для материала."""
        self.key = True
        return self.show_table_material()

    def active_table_material(self):
        """Активация таблицы для материла."""
        ...

    def functional_table_material(self):
        """Функционал таблицы с материалом."""
        ...

    def show_table_material(self):
        """Показ таблицы с материалом."""
        self.button_widget.hide()
        self.table_widget.hide()
        if self.key:
            self.button_widget.show()
            self.table_widget.show()
            self.key = False



