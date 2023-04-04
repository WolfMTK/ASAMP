import re
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QFileDialog,
    QMessageBox,
)

from widgets.elements.widget import WidgetParameters
from widgets.elements.line_edit import LineEditParameters
from widgets.elements.push_button import PushButtonParameters
from widgets.settings import NAME_WIDGET, NAME_LINE_EDIT, NAME_PUSH_BUTTON
from .elements.window import WindowParameters


class SettingsPattern(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__add_widget()
        self.__add_line_edit()
        self.__add_push_buttons()
        self.__set_parameters_window()
        self.__align_elements()
        self.__click_push_buttons()

    def __add_widget(self) -> None:
        self.widget = WidgetParameters(self, NAME_WIDGET, style=True).widget

    def __add_line_edit(self) -> None:
        self.line_edit = LineEditParameters(
            self.widget, NAME_LINE_EDIT, width=200, height=35
        ).line_edit

    def __add_push_buttons(self) -> None:
        self.push_button_open_path = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            width=250,
            height=35,
            style=True,
            text="ПУТЬ ДО ШАБЛОНА",
        ).push_button
        self.push_button_save = PushButtonParameters(
            self.widget,
            NAME_PUSH_BUTTON,
            width=150,
            height=35,
            style=True,
            text="СОХРАНИТЬ",
        ).push_button

    def __set_parameters_window(self) -> None:
        WindowParameters(
            self,
            self.widget,
            "Параметры",
        ).set_parameters()
        self.setFixedSize(500, 100)

    def __align_elements(self) -> None:
        horizontal_layout = QGridLayout(self.widget)
        horizontal_layout.addWidget(self.line_edit, 0, 1, 1, 1)
        horizontal_layout.addWidget(self.push_button_open_path, 0, 0, 1, 1)
        horizontal_layout.addWidget(
            self.push_button_save, 3, 0, 1, 0, Qt.AlignCenter
        )

    def __click_push_buttons(self) -> None:
        self.push_button_open_path.clicked.connect(self.__add_path)
        self.push_button_save.clicked.connect(self.__save_path)

    def __add_path(self) -> None:
        path = QFileDialog.getOpenFileName(self, "Путь к шаблону", "")
        self.line_edit.setText(path[0])

    def __save_path(self) -> None:
        path = self.line_edit.text()
        if all([
            path,
            Path(path).exists(),
            re.search(r".docx", path),
        ]):
            with open("path_template.txt", "w") as file:
                file.write(path)
                file.close()
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка!", "Неверный шаблон!")
