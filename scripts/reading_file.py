from docx import Document


class DocumentWord:
    def __init__(self, path: str) -> None:
        self.__path = path

    def open_document(self) -> None:
        self.doc = Document(self.__path)

    def get_text(self) -> str:
        text_docx = ""
        for text in self.doc.paragraphs:
            text_docx += text.text
        return text_docx
