class Person():
    def __init__ (self, age, name ):
        self.age = age
        self.name = name
    def greet(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old.")


Person1 = Person(15, "Sushant")
Person1.greet()
