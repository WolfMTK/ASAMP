from PySide6.QtWidgets import QWidget, QLineEdit


class LineEditParameters:
    def __init__(
        self, widget: QWidget, object_name: str, width: int, height: int
    ) -> None:
        self.__line_edit = QLineEdit(widget)
        self.__object_name = object_name
        self.__width = width
        self.__height = height

    @property
    def line_edit(self) -> QLineEdit:
        self.__set_object_name()
        self.__set_style_sheet()
        self.__set_fixed_size()
        return self.__line_edit

    def __set_object_name(self) -> None:
        self.__line_edit.setObjectName(self.__object_name)

    def __set_style_sheet(self) -> None:
        self.__line_edit.setStyleSheet(
            f"""#{self.__object_name}{{
                background-color: white;
                color: black;
                font-size: 14px;
                font-family: bold "Times New Roman";
                border: 1px solid #ced4da;
                border-radius: 10px;
                padding-left: 5px;
                padding-right: 5px;
            }}"""
        )

    def __set_fixed_size(self) -> None:
        self.__line_edit.setFixedSize(self.__width, self.__height)
