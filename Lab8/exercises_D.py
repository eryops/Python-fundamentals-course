class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f'Employee: {self.name}'

class Developer(Employee):
    def write_code(self):
        return f'{self.name} is writing Python code'

class Designer(Employee):
    def create_designs(self):
        return f'{self.name} designs stuff'

developer = Developer("Johanna")
designer = Designer("Alex")

print(developer.get_information())   
print(designer.get_information())   

print(developer.write_code())       
print(designer.create_designs())     

employee = Employee('Berit')
# print(employee.write_code()) 

# parents can´t inherit from their children, like in nature 