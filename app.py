import sys
import logging

from PySide6.QtWidgets import QApplication

from windows import MainWindow
from database import Database


def main() -> None:
    Database("sql/create_table.sql").create_table()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    logging.basicConfig(
        filename="logs_app.log",
        level=logging.INFO,
        format="%(asctime)s, %(levelname)s, %(message)s, %(name)s",
    )
    logging.getLogger(__name__).info("Запуск программы!")
    main()
