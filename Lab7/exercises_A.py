class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"


class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

    def __repr__(self):
        return f"Laptop(brand='{self.brand}', model='{self.model}', ram={self.ram_gb}gb), price={self.ram_gb})"


# --- Main like section ---
b1 = Book('Dan Brown', 'Davinci koden', 890)
b2 = Book('Dan Brown', 'Davinci koden', 890)
print(b1 is b2)
print(b1.is_long()) 
print(b1)

laptop1 = Laptop('Dell', 'XJ345', 32, 12344)
print(laptop1)