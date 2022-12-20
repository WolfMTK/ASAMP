from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QLabel

from interface.widgets.central_widget import CentralWidget


class SelectionWidget(CentralWidget):
    """Виджет: установка значений."""

    def __init__(self):
        super(SelectionWidget, self).__init__()
        self.selection_widget = QWidget(self.central_widget)
        self.selection_widget.setStyleSheet('background-color: red')

        self.v_layout_selection = QVBoxLayout(self.selection_widget)
        self.table_analysis = QTableWidget(self.selection_widget)
        self.label_analysis = QLabel(self.selection_widget)
