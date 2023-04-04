from PySide6.QtWidgets import QMainWindow, QWidget


class WindowParameters:
    def __init__(
        self,
        window: QMainWindow,
        central_widget: QWidget,
        title: str,
        min_width: int | None = None,
        min_height: int | None = None,
    ) -> None:
        self.__window = window
        self.__central_widget = central_widget
        self.__title = title
        self.__min_width = min_width
        self.__min_height = min_height

    def set_parameters(self) -> None:
        self.__set_central_widget()
        self.__set_window_title()
        self.__set_minimum_size()

    def __set_central_widget(self) -> None:
        self.__window.setCentralWidget(self.__central_widget)

    def __set_window_title(self) -> None:
        self.__window.setWindowTitle(self.__title)

    def __set_minimum_size(self) -> None:
        if self.__min_width and self.__min_height:
            self.__window.setMinimumSize(self.__min_width, self.__min_height)
