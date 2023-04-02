from PySide6.QtWidgets import QWidget, QLabel


class LabelParameters:
    def __init__(self, widget: QWidget, object_name: str, text: str) -> None:
        self.__label = QLabel(widget)
        self.__object_name = object_name
        self.__text = text

    @property
    def label(self) -> QLabel:
        self.__set_object_name()
        self.__set_style_sheet()
        self.__set_text()
        return self.__label

    def __set_object_name(self) -> None:
        self.__label.setObjectName(self.__object_name)

    def __set_style_sheet(self) -> None:
        self.__label.setStyleSheet(
            f"""#{self.__object_name}{{
                color: black;
                font-size: 18px;
                font-family: bold "Times New Roman";
            }}"""
        )

    def __set_text(self) -> None:
        self.__label.setText(self.__text)
