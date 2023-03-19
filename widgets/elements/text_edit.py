from PySide6.QtWidgets import QWidget, QTextEdit


class TextEditParameters:
    def __init__(self, widget: QWidget, object_name: str) -> None:
        self.__text_edit = QTextEdit(widget)
        self.__object_name = object_name

    @property
    def text_edit(self):
        self.__set_object_name()
        self.__set_style_sheet()
        return self.__text_edit

    def __set_object_name(self) -> None:
        self.__text_edit.setObjectName(self.__object_name)

    def __set_style_sheet(self) -> None:
        self.__text_edit.setStyleSheet(
            f"""#{self.__object_name}{{
                background-color: white;
                border-radius: 10px;
                font-size: 20px;
                font-family: bold "Times New Roman";
            }}"""
        )
