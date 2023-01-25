from PySide6.QtWidgets import QMainWindow, QGridLayout

from style.size_objects import WIDTH_DATABASE_WINDOW, HEIGHT_DATABASE_WINDOW
from widgets.central_widget import CentralWidget
from widgets.control_widget import ControlWidget
from widgets.database_widget import DatabaseWidget


class DatabaseWindow(QMainWindow):
    """Окно базы данных."""

    def __init__(self):
        super(DatabaseWindow, self).__init__()
        self.central_widget = CentralWidget(self).widget
        self.control_widget = ControlWidget(self)
        self.database_widget = DatabaseWidget(self)
        self.grid_layout = QGridLayout(self.central_widget)
        self.add_functional_for_window()

    def add_functional_for_window(self) -> None:
        """Добавить функционал для окна."""
        self.add_minimum_size_for_window()
        self.add_title_for_window()
        self.set_central_widget()
        self.add_grid_layout_for_widgets()

    def add_minimum_size_for_window(self) -> None:
        """Добавить минимальный размер окна."""
        self.setMinimumSize(WIDTH_DATABASE_WINDOW, HEIGHT_DATABASE_WINDOW)

    def add_title_for_window(self) -> None:
        """Добавить название для приложения."""
        self.setWindowTitle("DATABASE")

    def set_central_widget(self) -> None:
        """Установить центральный виджет для окна."""
        self.setCentralWidget(self.central_widget)

    def add_grid_layout_for_widgets(self) -> None:
        """Добавить выравнивание по сетке для виджетов."""
        self.grid_layout.addWidget(self.control_widget.widget, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.database_widget.widget, 0, 1, 2, 2)
