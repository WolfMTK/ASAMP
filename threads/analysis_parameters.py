import logging
from typing import List, Any
from itertools import count

from PySide6.QtWidgets import QTableWidget, QComboBox, QTableWidgetItem
from PySide6.QtCore import QThread, Qt

from database import Database


CLEAR_INDEX = 0

logger = logging.getLogger(__name__)


class AnalysisParameters(QThread):
    def __init__(
        self, table_analysis: QTableWidget, combo_box_type_part: QComboBox
    ) -> None:
        super().__init__()
        self.table_analysis = table_analysis
        self.combo_box_type_part = combo_box_type_part
        self.status: bool = True
        self.parameters: None | List[str] = None

    def run(self) -> None:
        for _ in count(1):
            data = self.__get_data()
            self.__add_data_in_table(data)
            if not self.status:
                break
            self.msleep(10)

    def close_thread(self) -> None:
        self.status = False

    def __get_data(self) -> List[Any]:
        type_part = self.combo_box_type_part.currentText()
        data = []
        if all([type_part]):
            for part in Database("sql/parameter.sql").get_data(
                part=type_part
            ):
                data.append(part[0])
        else:
            self.parameters = None
        return data

    def __add_data_in_table(self, data):
        self.table_analysis.resizeColumnsToContents()
        self.table_analysis.horizontalHeader().setMinimumSectionSize(100)
        if data and data != self.parameters:
            self.parameters = data
            self.table_analysis.setRowCount(len(data))
            self.table_analysis.setColumnCount(2)
            self.table_analysis.horizontalHeader().setVisible(False)
            self.table_analysis.verticalHeader().setVisible(False)
            for index, parameter in enumerate(self.parameters):
                self.table_analysis.setItem(
                    index, 0, QTableWidgetItem(parameter)
                )
                self.table_analysis.item(index, 0).setFlags(Qt.ItemIsEnabled)
        elif self.parameters != data:
            self.parameters = None
            self.table_analysis.setColumnCount(CLEAR_INDEX)
            self.table_analysis.setRowCount(CLEAR_INDEX)
