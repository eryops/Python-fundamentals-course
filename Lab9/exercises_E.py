class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} kr"

p1 = Product("Laptop", 15000)
p2 = Product("Headphones", 1200)
p3 = Product("Mouse", 400)

print(p1)
print(p2)
print(p3)

text = str(p1)
print(text)
print(type(text))
