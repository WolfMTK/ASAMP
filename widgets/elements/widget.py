from PySide6.QtWidgets import QWidget, QMainWindow


class WidgetParameters:
    def __init__(
        self,
        widget: QWidget | QMainWindow,
        object_name: str,
        width: int | None = None,
        height: int | None = None,
        style: bool = False,
        style_central_widget: bool = False,
    ) -> None:
        self.__widget = QWidget(widget)
        self.__object_name = object_name
        self.__style = style
        self.__style_central_widget = style_central_widget
        self.__width = width
        self.__height = height

    @property
    def widget(self) -> None:
        self.__set_object_name()
        self.__set_style_sheet()
        self.__set_fixed_size()
        return self.__widget

    def __set_object_name(self) -> None:
        self.__widget.setObjectName(self.__object_name)

    def __set_style_sheet(self) -> None:
        if self.__style:
            self.__widget.setStyleSheet(
                f"""#{self.__object_name}{{
                    background-color: white;
                    border-radius: 10px;
                }}"""
            )
        elif self.__style_central_widget:
            self.__widget.setStyleSheet(
                f"""#{self.__object_name}{{
                    background-color: #d9d9d9;
                }}"""
            )

    def __set_fixed_size(self):
        if self.__width and self.__height:
            self.__widget.setFixedSize(self.__width, self.__height)
        elif self.__width and self.__height is None:
            self.__widget.setFixedWidth(self.__width)
        elif self.__height and self.__width is None:
            self.__widget.setFixedHeight(self.__height)
