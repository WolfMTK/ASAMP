import logging

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QComboBox, QTableWidget

from .brand import Brand
from .type_part import TypePart
from .material import Material
from .parameters import AnalysisParameters


logger = logging.getLogger(__name__)


class MainThreads(QThread):
    def __init__(
        self,
        combo_box_material: QComboBox,
        combo_box_brand: QComboBox,
        combo_box_type_part: QComboBox,
        table_analysis: QTableWidget,
    ) -> None:
        super().__init__()
        self.combo_box_material = combo_box_material
        self.combo_box_brand = combo_box_brand
        self.combo_box_type_part = combo_box_type_part
        self.table_analysis = table_analysis

    def run(self) -> None:
        self.__start_thread_material()
        self.__start_thread_brand()
        self.__start_thread_type_part()
        self.__start_thread_analysis_parameters()

    def close_thread(self) -> None:
        self.material.close_thread()
        self.brand.close_thread()
        self.type_part.close_thread()
        self.analysis_parameters.close_thread()

    def __start_thread_material(self) -> None:
        self.material = Material(self.combo_box_material)
        self.material.start()

    def __start_thread_brand(self) -> None:
        self.brand = Brand(self.combo_box_brand, self.combo_box_material)
        self.brand.start()

    def __start_thread_type_part(self) -> None:
        self.type_part = TypePart(self.combo_box_type_part)
        self.type_part.start()

    def __start_thread_analysis_parameters(self) -> None:
        self.analysis_parameters = AnalysisParameters(
            self.table_analysis, self.combo_box_type_part
        )
        self.analysis_parameters.start()
