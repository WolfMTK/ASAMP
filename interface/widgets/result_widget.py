from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout

from interface.widgets.central_widget import CentralWidget


class ResultWidget(CentralWidget):
    """Виджет: результат."""

    def __init__(self):
        super(ResultWidget, self).__init__()
        self.result_widget = QWidget(self.central_widget)

        self.result_widget.setStyleSheet('background-color: red')
        self.text_edit_result = QTextEdit(self.result_widget)
        self.h_layout_result = QHBoxLayout(self.result_widget)
