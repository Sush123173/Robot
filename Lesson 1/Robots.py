class robot():
    def __init__ (self, arms, top_speed ):
        self.arms = arms
        self.top_speed = top_speed
    def description(self):
        print(f"I have {self.arms} arms and I have a top speed of {self.top_speed} mph.")


robot1 = robot(3, "10")
robot1.description()
robot2 = robot(5, "50")
robot2.description()