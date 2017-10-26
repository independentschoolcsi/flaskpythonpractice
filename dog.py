from animal import Animal

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
	    return "woof! woof!... my name is " + self.name + "!... woof! woof!"

