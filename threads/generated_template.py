import logging

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QComboBox, QTableWidget, QLineEdit
from docx.opc.exceptions import PackageNotFoundError

from database import Database
from scripts.generate_template import TemplateWord


logger = logging.getLogger(__name__)


class GeneratedTemplate(QThread):
    def __init__(
        self,
        combo_box_material: QComboBox,
        combo_box_type_part: QComboBox,
        combo_box_brand: QComboBox,
        table_analysis: QTableWidget,
        line_edit_name_part: QLineEdit,
        save_name: str,
    ) -> None:
        super().__init__()
        self.__combo_box_material = combo_box_material
        self.__combo_box_type_part = combo_box_type_part
        self.__combo_box_brand = combo_box_brand
        self.__table_analysis = table_analysis
        self.__line_edit_name_part = line_edit_name_part
        self.__save_name = save_name

    def run(self) -> None:
        data = self.__get_data()
        if data:
            self.__generate_doc(data | self.__get_data_with_table())
            self.msleep(1)

    def __get_data(self) -> dict[str, str]:
        type_part = self.__combo_box_type_part.currentText()
        material = self.__combo_box_material.currentText()
        brand = self.__combo_box_brand.currentText()
        name_part = self.__line_edit_name_part.text()
        data = {}
        if all([material, brand, name_part, type_part]):
            data["материал_детали"] = material.lower()
            data["марка_материала"] = brand
            data["название_детали"] = name_part.lower()
            data["описание_материала"] = Database(
                "sql/description.sql"
            ).get_data(material_part=material, brand_part=brand)[0][0]
        return data

    def __get_data_with_table(self) -> dict[str, str]:
        col_count = self.__table_analysis.columnCount()
        row_count = self.__table_analysis.rowCount()
        data = {}
        for index in range(row_count):
            try:
                parameter = Database("sql/tag_parameter.sql").get_data(
                    part=self.__combo_box_type_part.currentText(),
                    parameter=self.__table_analysis.item(
                        index, col_count - 2
                    ).text(),
                )[0][0]
                data[parameter] = self.__table_analysis.item(
                    index, col_count - 1
                ).text()
            except Exception as error:  # noqa
                logger.warning(
                    f"""Ошибка: {error}! Ячейка {
                        self.__table_analysis.item(index, col_count - 2).text()
                    }"""
                )
        return data

    def __generate_doc(self, data) -> None:
        template = TemplateWord(data)
        with open("path_template.txt") as file:
            try:
                template.open_doc(file.read())
                template.render_doc()
                template.save_doc(self.__save_name)
            except PackageNotFoundError:
                pass
            file.close()
