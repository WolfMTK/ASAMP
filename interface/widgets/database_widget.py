from PySide6.QtWidgets import QWidget, QGridLayout

from interface.core import Core


class DatabaseWidget(Core):
    def __init__(self, *args, **kwargs):
        super(DatabaseWidget, self).__init__(*args, **kwargs)
        self.database_widget = QWidget(self)
        self.grid_layout_database = QGridLayout(self.database_widget)
        self.setCentralWidget(self.database_widget)
