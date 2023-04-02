from PySide6.QtWidgets import QWidget, QComboBox


class ComboBoxParameters:
    def __init__(
        self, widget: QWidget, object_name: str, width: int, height: int
    ) -> None:
        self.__combo_box = QComboBox(widget)
        self.__object_name = object_name
        self.__width = width
        self.__height = height

    @property
    def combo_box(self) -> QComboBox:
        self.__set_object_name()
        self.__set_style_sheet()
        self.__set_fixed_size()
        self.__set_editable()
        return self.__combo_box

    def __set_object_name(self) -> None:
        self.__combo_box.setObjectName(self.__object_name)

    def __set_style_sheet(self) -> None:
        self.__combo_box.setStyleSheet(
            f"""#{self.__object_name}{{
                color: black;
                background-color: white;
                border: 1px solid #ced4da;
                border-radius: 10px;
                padding-left: 5px;
                font-size: 14px;
                font-family: bold "Times New Roman";
            }}
            #{self.__object_name}::drop-down{{
                border: 0px;
            }}
            #{self.__object_name}::down-arrow{{
                image: url(./icons/down_arrow.png);
                width: 20px;
                height: 20px;
                margin-right: 8px;
            }}
            #{self.__object_name}::on{{
                border: 4px solid #e5e5e5;
            }}
            #{self.__object_name} QListView{{
                color: black;
                font-size: 12px;
                border: 1px solid rgba(0, 0, 0, 10%);
                padding: 5px;
                background-color: #fff;
                outline: 0px;
            }}
            #{self.__object_name} QListView::item{{
                padding-left: 10px;
                background-color: #fff;
            }}
            #{self.__object_name} QListView::item:hover{{
                background-color: #1e90ff;
            }}
            #{self.__object_name} QListView::item:selected{{
                background-color: #1e90ff;
            }}"""
        )

    def __set_fixed_size(self) -> None:
        self.__combo_box.setFixedSize(self.__width, self.__height)

    def __set_editable(self) -> None:
        self.__combo_box.setEditable(True)
