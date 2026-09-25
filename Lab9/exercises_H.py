class Exporter:
    def export(self, data):
        return data

class ConsoleExporter(Exporter):
    def export(self, data):
        print(f"Console: {data}")

    def __str__(self):
        return "ConsoleExporter"

class TextExporter(Exporter):
    def export(self, data):
        print(f"Text format: {data.upper()}")

    def __str__(self):
        return "TextExporter"

class SummaryExporter(Exporter):
    def export(self, data):
        print(f"Summary: {data[:10]}...")

    def __str__(self):
        return "SummaryExporter"

class CustomExporter:
    def export(self, data):
        print(f"Custom export: {len(data)} characters")

    def __str__(self):
        return "CustomExporter"

class Logger:
    def __init__(self, exporter):
        self.exporter = exporter

    def log(self, data):
        self.exporter.export(data)

console = ConsoleExporter()
text = TextExporter()
summary = SummaryExporter()
custom = CustomExporter()

exporters = [console, text, summary, custom]

for e in exporters:
    e.export("Hello world, this is export data")

print(isinstance(console, Exporter))
print(isinstance(custom, Exporter))

logger = Logger(console)
logger.log("Logging through composition")
