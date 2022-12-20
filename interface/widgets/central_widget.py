from PySide6.QtWidgets import QWidget, QGridLayout

from interface.core import Core


class CentralWidget(Core):
    def __init__(self, *args, **kwargs):
        super(CentralWidget, self).__init__(*args, **kwargs)
        self.central_widget = QWidget(self)
        self.grid_layout_central = QGridLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)
