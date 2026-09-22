class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price


# --- Main like section ---
b1 = Book('Dan Brown', 'Davinci koden', 890)
b2= Book('Dan Brown', 'Davinci koden', 890)
print(b1 is b2)
