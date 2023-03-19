import sys

from PySide6.QtWidgets import QApplication

# from windows import MainWindow
from windows.main_window import run_main_window


# def main() -> None:
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


if __name__ == "__main__":
    run_main_window()
