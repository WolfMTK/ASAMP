import sys

from PySide6.QtWidgets import QApplication

from interface.functional_widget import Functional


class Window(Functional):
    def __init__(self):
        super(Window, self).__init__()
        self.set_window()

    def set_window(self):
        self.setWindowTitle('ASAMP')
        self.setMinimumSize(850, 600)


def start_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
