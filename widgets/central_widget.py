from PySide6.QtWidgets import QMainWindow

from .elements import WidgetParameters
from .settings import NAME_WIDGET


class CentralWidget:
    def __init__(self, window: QMainWindow) -> None:
        self.widget = WidgetParameters(
            window, NAME_WIDGET, style_central_widget=True
        ).widget
