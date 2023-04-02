from docxtpl import DocxTemplate


class TemplateWord:
    def __init__(self, context) -> None:
        self.__context = context

    def open_doc(self, name: str) -> None:
        self.doc = DocxTemplate(name)

    def render_doc(self) -> None:
        self.doc.render(self.__context)

    def save_doc(self, path: str) -> None:
        self.doc.save(path)
