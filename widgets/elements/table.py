from PySide6.QtWidgets import QTableWidget, QWidget


class TableParameters:
    def __init__(self, widget: QWidget, object_name: str) -> None:
        self.__table = QTableWidget(widget)
        self.__object_name = object_name

    @property
    def table(self) -> QTableWidget:
        self.__set_object_name()
        self.__set_style_sheet()
        return self.__table

    def __set_object_name(self) -> None:
        self.__table.setObjectName(self.__object_name)

    def __set_style_sheet(self) -> None:
        self.__table.setStyleSheet(
            f"""#{self.__object_name}{{
                background-color: white;
                border-radius: 10px;
                font-size: 20px;
                font-family: bold "Times New Roman";
            }}"""
        )
