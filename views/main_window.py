import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout

from widgets.action_widget import ActionWidget
from widgets.central_widget import CentralWidget
from widgets.parameters_widget import ParametersWidget


class MainWindow(QMainWindow):
    """Главное окно программы."""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.central_widget = CentralWidget(self).widget
        self.action_widget = ActionWidget(self.central_widget)
        self.parameters_widget = ParametersWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.set_central_widget()
        self.add_grid_layout_for_widgets()

    def set_central_widget(self):
        """Установить центральный виджет для окна."""
        self.setCentralWidget(self.central_widget)

    def add_grid_layout_for_widgets(self):
        """Добавить выравнивание по сетке для виджетов."""
        self.grid_layout.addWidget(self.action_widget.widget, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.parameters_widget.widget, 0, 0, 1, 1)


def run_main_window():
    """Запуск главного окна."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
