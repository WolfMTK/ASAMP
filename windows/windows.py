import logging
import time

from PySide6.QtWidgets import QMainWindow, QGridLayout
from PySide6.QtCore import Qt

from widgets import (
    ActionWidget,
    CentralWidget,
    ParametersWidget,
    ResultWidget,
    DataWidget,
    ControlWidget,
    DatabaseWidget,
)
from threads import MainThreads, GeneratedTemplate
from .elements import WindowParameters
from .settings import (
    WIDTH_WINDOW,
    HEIGHT_WINDOW,
    TITLE_MAIN_WINDOW,
    TITLE_DATABASE,
)


logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__add_widgets()
        self.__add_elements()

        self.__set_parameters_window()
        self.__align_elements()
        self.__set_click_push_buttons()
        self.__start_thread()
        self.__deactivate_text_edit()

    def __add_widgets(self) -> None:
        self.central_widget = CentralWidget(self).widget
        self.action_widget = ActionWidget(self.central_widget)
        self.parameters_widget = ParametersWidget(self.central_widget)
        self.result_widget = ResultWidget(self.central_widget)
        self.data_widget = DataWidget(self.central_widget)

    def __add_elements(self):
        self.push_button_close = self.action_widget.push_button_close
        self.push_button_settings = self.parameters_widget.push_button_settings
        self.push_button_clear = self.action_widget.push_button_clear
        self.push_button_result = self.action_widget.push_button_result
        self.push_button_save = self.action_widget.push_button_save
        self.combo_box_material = self.parameters_widget.combo_box_material
        self.combo_box_brand = self.parameters_widget.combo_box_brand
        self.combo_box_type_part = self.parameters_widget.combo_box_type_part
        self.table_analysis = self.data_widget.table_analysis
        self.line_edit_name_part = self.parameters_widget.line_edit_name_part
        self.text_edit_result = self.result_widget.text_edit_result

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

    def __start_thread(self) -> None:
        self.start_thread = MainThreads(
            self.combo_box_material,
            self.combo_box_brand,
            self.combo_box_type_part,
            self.table_analysis,
        )
        self.start_thread.start()

    def __set_click_push_buttons(self) -> None:
        self.push_button_close.clicked.connect(self.__close_windows)
        self.push_button_settings.clicked.connect(self.__open_database_window)
        self.push_button_clear.clicked.connect(self.__clear_data)
        self.push_button_result.clicked.connect(self.__start_script)
        # self.push_button_save.clicked.connect(...)

    def __close_windows(self) -> None:
        logger.info("Закрытие программы!")
        self.start_thread.close_thread()
        time.sleep(0.1)
        self.close()

    def __open_database_window(self) -> None:
        logger.info("Открытие окна с базой данных!")
        self.database_window = DatabaseWindow()
        self.database_window.setWindowModality(
            Qt.WindowModality.ApplicationModal
        )
        self.database_window.show()

    def __clear_data(self):
        self.combo_box_material.setCurrentIndex(0)
        self.combo_box_type_part.setCurrentIndex(0)
        self.combo_box_brand.setCurrentIndex(0)
        self.text_edit_result.setText("")
        self.__deactivate_text_edit()
        self.line_edit_name_part.setText("")

    def __deactivate_text_edit(self):
        self.text_edit_result.setEnabled(False)

    def __start_script(self):
        self.result = GeneratedTemplate(
            self.combo_box_material,
            self.combo_box_type_part,
            self.combo_box_brand,
            self.table_analysis,
            self.line_edit_name_part,
        )
        self.result.start()


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

    def __set_parameters_window(self) -> None:
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
