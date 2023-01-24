from PySide6.QtWidgets import QMainWindow, QWidget

from name_objects.name_objects import NAME_CENTRAL_WIDGET
from style.style import STYLE_CENTRAL_WIDGET
from widgets.widget import Widget


class CentralWidget(Widget):
    """Центральные виджет для главного окна."""

    def __init__(self, window: QMainWindow) -> None:
        self.widget = QWidget(window)
        self.add_parameters_for_widget()

    def add_parameters_for_widget(self) -> None:
        """Добавить параметры для виджета."""
        self.name_objets = NAME_CENTRAL_WIDGET
        self.style_widget = STYLE_CENTRAL_WIDGET
        self.add_name_for_objects()
        self.add_style()
