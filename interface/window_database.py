import sys

from PySide6.QtWidgets import QApplication

from interface.settings_database_widgets import SettingsDatabaseWidget


class WindowDatabase(SettingsDatabaseWidget):
    def __init__(self):
        super(WindowDatabase, self).__init__()
        self.set_window()

    def set_window(self):
        self.setWindowTitle('DATABASE')
        self.setMinimumSize(800, 600)


def start_window():
    app = QApplication(sys.argv)
    window = WindowDatabase()
    window.show()
    sys.exit(app.exec())
