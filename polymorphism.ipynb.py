
# Base class
class Report:
    def generate(self):
        pass

        # Derived classes
class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report...")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report...")

        # Using polymorphism
reports = [PDFReport(), ExcelReport()]
for r in reports:
    r.generate()

    class OnlineOrder:
    def status(self):
        print("Order is being processed")

class StoreOrder:
    def status(self):
        print("Order is ready for pickup")

def check_status(order):
    order.status()

check_status(OnlineOrder())
check_status(StoreOrder())
