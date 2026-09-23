class Report:
    def get_summary(self):
        return f'Report'

class SalesReport(Report):
    def get_summary(self):
        return super().get_summary() + f' Sales'

salesReport = SalesReport()
print(salesReport.get_summary())