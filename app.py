import sys
import logging
import shutil
from pathlib import Path

from PySide6.QtWidgets import QApplication

from windows import MainWindow
from database import Database


def main() -> None:
    path = Path('./cash')
    path.mkdir(parents=True, exist_ok=True)
    Database("sql/create_table.sql").create_table()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    shutil.rmtree(path)
    sys.exit()


if __name__ == "__main__":
    logging.basicConfig(
        filename="logs_app.log",
        level=logging.INFO,
        format="%(asctime)s, %(levelname)s, %(message)s, %(name)s",
    )
    logging.getLogger(__name__).info("Запуск программы!")
    main()
