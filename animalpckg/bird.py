from animalpckg.animal import Animal

class Bird(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
	    return "<h1>chirp chirp chirp!... my name is " + self.name + "!... chirp chirp chirp!<h1>"

