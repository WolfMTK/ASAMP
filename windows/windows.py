from PySide6.QtWidgets import QMainWindow, QGridLayout
from PySide6.QtCore import Qt

from widgets import (
    ActionWidget,
    CentralWidget,
    ParametersWidget,
    ResultWidget,
    DataWidget,
    ControlWidget,
    DatabaseWidget
)
from .elements import WindowParameters
from .settings import (
    WIDTH_WINDOW,
    HEIGHT_WINDOW,
    TITLE_MAIN_WINDOW,
    TITLE_DATABASE,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__add_widgets()
        self.__set_parameters_window()
        self.__align_elements()
        self.__set_click_push_buttons()

    def __add_widgets(self) -> None:
        self.central_widget = CentralWidget(self).widget
        self.action_widget = ActionWidget(self.central_widget)
        self.parameters_widget = ParametersWidget(self.central_widget)
        self.result_widget = ResultWidget(self.central_widget)
        self.data_widget = DataWidget(self.central_widget)

    def __set_parameters_window(self):
        WindowParameters(
            self,
            self.central_widget,
            TITLE_MAIN_WINDOW,
            min_width=WIDTH_WINDOW,
            min_height=HEIGHT_WINDOW,
        ).set_parameters()

    def __align_elements(self) -> None:
        grid_layout = QGridLayout(self.central_widget)
        grid_layout.addWidget(self.action_widget.widget, 2, 0, 1, 1)
        grid_layout.addWidget(self.parameters_widget.widget, 0, 0, 1, 1)
        grid_layout.addWidget(self.data_widget.widget, 0, 1, 3, 1)
        grid_layout.addWidget(self.result_widget.widget, 1, 0, 1, 1)

    def __set_click_push_buttons(self) -> None:
        self.action_widget.push_button_close.clicked.connect(self.close)
        self.parameters_widget.push_button_settings.clicked.connect(self.__open_database_window)
        # TODO: добавить функционал для кнопок
        # self.action_widget.push_button_clear.clicked.connect(...)
        # self.action_widget.push_button_result.clicked.connect(...)
        # self.action_widget.push_button_save.clicked.connect(...)
    
    def __open_database_window(self) -> None:
        self.database_window = DatabaseWindow()
        self.database_window.setWindowModality(
            Qt.WindowModality.ApplicationModal
        )
        self.database_window.show()


class DatabaseWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__add_widgets()
        self.__set_parameters_window()
        self.__align_elements()

    def __add_widgets(self) -> None:
        self.central_widget = CentralWidget(self).widget
        self.control_widget = ControlWidget(self)
        self.database_widget = DatabaseWidget(self)

    def __set_parameters_window(self):
        WindowParameters(
            self,
            self.central_widget,
            TITLE_DATABASE,
            min_width=WIDTH_WINDOW,
            min_height=HEIGHT_WINDOW,
        ).set_parameters()
    
    def __align_elements(self) -> None:
        grid_layout = QGridLayout(self.central_widget)
        grid_layout.addWidget(self.control_widget.widget, 0, 0, 1, 1)
        grid_layout.addWidget(self.database_widget.widget, 0, 1, 2, 2)
