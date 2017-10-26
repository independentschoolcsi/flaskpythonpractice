from flask import Flask
from dog import Dog
from bird import Bird
app = Flask(__name__)

@app.route('/<animal>/<name>')
def users_animal(animal, name):

    if animal == "dog":
        dog1 = Dog(name)
        return dog1.speak()

    if animal == "bird":
        bird1 = Bird(name)
        return bird1.speak()

if __name__ == '__main__':
    app.run(debug=True)
