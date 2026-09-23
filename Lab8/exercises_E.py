class Device:
    def __init__(self, brand, year):
        self.brand = brand.strip().title()
        self.year = int(year)

class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb

    def __repr__(self):
        return f'Laptop {self.brand}, year {self.year}, ram {self.ram_gb}GB'

class Phone(Device):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def __repr__(self):
        return f'Phone {self.brand}, year {self.year}, model {self.model}'

laptop = Laptop("lenovo", 2018, 16)
phone = Phone("samsung", 2021, "Galaxy S21")

print(laptop)
print(phone)
