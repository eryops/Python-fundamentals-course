class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "Generic document"

class PDFDocument(Document):
    def describe(self):
        return "This is a PDF document."

class TextDocument(Document):
    def describe(self):
        return "This is a plain text document."

docs = [
    PDFDocument("Report Q3"),
    PDFDocument("Invoice 2026-09"),
    TextDocument("Notes from lecture"),
    TextDocument("Todo list")
]

for d in docs:
    print(d.title, "-", d.describe())
