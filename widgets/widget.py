from dataclasses import dataclass

from PySide6.QtWidgets import QWidget


@dataclass
class Widget:
    """Виджет с базовым функционалом."""

    widget: QWidget
    name_objets: str
    style_widget: str

    def add_name_for_objects(self) -> None:
        """Добавить имя для объектов."""
        self.widget.setObjectName(self.name_objets)

    def add_style(self) -> None:
        """Добавить стиль для виджета."""
        self.widget.setStyleSheet(self.style_widget)
