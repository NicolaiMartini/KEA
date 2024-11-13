class Person():
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country
    def description(self):
        print(f"My name is {self.name}, I am {self.age} years of age and I come from {self.country}.")