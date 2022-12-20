import sys

from PySide6.QtWidgets import QApplication

from interface.functional_database_widget import Functional


class WindowDatabase(Functional):
    """Окно базы данных."""
    def __init__(self):
        super(WindowDatabase, self).__init__()
        self.set_window()

    def set_window(self):
        """Настройки окна."""
        self.setWindowTitle('DATABASE')
        self.setMinimumSize(800, 600)


def start_window():
    app = QApplication(sys.argv)
    window = WindowDatabase()
    window.show()
    sys.exit(app.exec())
