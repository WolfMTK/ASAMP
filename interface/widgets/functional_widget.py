from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton

from interface.widgets.central_widget import CentralWidget


class FunctionalWidget(CentralWidget):
    """Виджет: функционал."""

    def __init__(self):
        super(FunctionalWidget, self).__init__()
        self.functional_widget = QWidget(self.central_widget)

        self.functional_widget.setStyleSheet('background-color: red')
        self.grid_layout_functional = QGridLayout(self.functional_widget)
        self.push_button_clear = QPushButton(self.functional_widget)
        self.push_button_exit = QPushButton(self.functional_widget)
        self.push_button_result = QPushButton(self.functional_widget)
        self.push_button_save = QPushButton(self.functional_widget)
