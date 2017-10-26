from animalpckg.animal import Animal

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
	    return "<h1>woof! woof!... my name is " + self.name + "!... woof! woof!<h1>"

