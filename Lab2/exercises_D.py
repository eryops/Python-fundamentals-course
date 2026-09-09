laptop = {
    "brand": "Dell",
    "model": "XPS 13",
    "RAM": "16GB",
    "storage": "512GB SSD",
    "price": 12000
}

print(f"The {laptop['brand']} {laptop['model']} has {laptop['RAM']} of RAM and {laptop['storage']} of storage. It costs {laptop['price']}sek.")

laptop["price"] = 11000
laptop["operating_system"] = "Windows 11"
laptop.pop("model")

print(laptop)
print(laptop.get("model"))
print(laptop.get("price"))

print(laptop.values())
print(laptop.items())
print(laptop.values())

study_hours = {
    "python basic": 33,
    "sql": 12,
    "web development": 23,
    "python 3": 22,
    "Java":1
}

print("total study hours", sum(study_hours.values()))