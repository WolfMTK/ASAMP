from PySide6.QtWidgets import QPushButton, QWidget


class PushButtonParameters:
    def __init__(
        self,
        widget: QWidget,
        object_name: str,
        width: int,
        height: int,
        style: bool = False,
        style_image: bool = False,
        text: str | None = None,
        image_path: str | None = None
    ) -> None:
        self.__push_button = QPushButton(widget)
        self.__object_name = object_name
        self.__width = width
        self.__height = height
        self.__style = style
        self.__style_image = style_image
        self.__text = text
        self.__image_path = image_path

    @property
    def push_button(self):
        self.__set_parameters()
        return self.__push_button

    def __set_parameters(self):
        self.__set_object_name()
        self.__set_style_sheet()
        self.__set_text()
        self.__set_fixed_size()

    def __set_object_name(self) -> None:
        self.__push_button.setObjectName(self.__object_name)

    def __set_style_sheet(self) -> None:
        if self.__style:
            self.__push_button.setStyleSheet(
                f"""#{self.__object_name}{{
                        background-color: rgba(0, 0, 0, 0);
                        color: black;
                        border-radius: 10px;
                        font-size: 20px;
                        font-family: bold "Times New Roman";
                    }}
                    #{self.__object_name}::hover{{
                        background-color: #e3e3e3;
                    }}
                    #{self.__object_name}::pressed{{
                        background-color: #c9f5ff;
                    }}"""
            )
        elif self.__style_image and self.__image_path:
            self.__push_button.setStyleSheet(
                f"""#{self.__object_name}{{
                        background-color: white;
                        border-radius: 5px;
                        image: url({self.__image_path});
                        font-size: 20px;
                        font-family: bold "Times New Roman";
                    }}
                    #{self.__object_name}::hover{{
                        background-color: #f7f7f7;
                    }}
                    #{self.__object_name}::pressed{{
                        background-color: #c9f5ff;
                    }}"""
            )

    def __set_text(self) -> None:
        if self.__text:
            self.__push_button.setText(self.__text)

    def __set_fixed_size(self) -> None:
        self.__push_button.setFixedSize(self.__width, self.__height)
