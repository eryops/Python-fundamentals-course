class CPU:
    def __init__(self, model):
        self.model = model

class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu

cpu1 = CPU("Intel Core i7-12700K")
computer1 = Computer("Lenovo", cpu1)

print(computer1.brand)
print(computer1.cpu.model)

# Car / Engine        -> HAS-A
# Manager / Employee  -> IS-A
# Course / Teacher    -> HAS-A
# Phone / Device      -> IS-A
