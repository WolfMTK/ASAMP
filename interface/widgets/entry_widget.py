from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QComboBox, QLabel,
    QLineEdit, QPushButton, QGridLayout
)

from interface.widgets.central_widget import CentralWidget


class EntryWidget(CentralWidget):
    """Виджет: ввод параметров."""

    def __init__(self):
        super(EntryWidget, self).__init__()
        self.entry_widget = QWidget(self.central_widget)

        self.entry_widget.setStyleSheet('background-color: red')
        self.edit_widget = QWidget(self.entry_widget)
        #
        self.h_layout_edit = QHBoxLayout(self.edit_widget)

        self.combo_box_material = QComboBox(self.entry_widget)
        self.combo_box_brand = QComboBox(self.entry_widget)
        self.combo_box_type_part = QComboBox(self.entry_widget)
        #
        self.label_material = QLabel(self.entry_widget)
        self.label_brand = QLabel(self.entry_widget)
        self.label_type_part = QLabel(self.entry_widget)
        self.label_name_part = QLabel(self.entry_widget)
        self.label_edit = QLabel(self.edit_widget)
        #
        self.line_edit_name_part = QLineEdit(self.entry_widget)
        #
        self.push_button_edit = QPushButton(self.edit_widget)
        #
        self.grid_layout_entry = QGridLayout(self.entry_widget)
