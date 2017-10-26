from animalpckg.dog import Dog
from animalpckg.bird import Bird

def create_animal(animal, name):
    if animal == "dog":
        dog1 = Dog(name)
        return dog1.speak()

    if animal == "bird":
        bird1 = Bird(name)
        return bird1.speak()
