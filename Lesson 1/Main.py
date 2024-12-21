class Car():
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
        self.speed = 0
    def drive(self):
        print (f"The {self.color} Car with {self.wheels} is starting to drive")

    def accelerate(self, increase):
        self.speed += increase
        print (f"The car is now going at {self.speed}")    

toycar = Car("blue","4")
toycar.drive()
toycar2 = Car("red", "4")
toycar2.drive()
toycar2.accelerate(20)

