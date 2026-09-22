class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

    def __repr__(self):
        return f'Product (name={self.name}, price={self.price})'

product1 = Product("Laptop", 15000)
product2 = Product("Headphones", 1200)
product3 = Product("Mouse", 400)

print(product1.price_with_tax())
print(product2.price_with_tax())
print(product3.price_with_tax())

Product.tax_rate = 0.1
print(product1.price_with_tax())
print(product2.price_with_tax())
print(product3.price_with_tax())
product1.tax_rate = 0.50
print(product1.price_with_tax())