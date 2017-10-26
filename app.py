from flask import Flask
import animalpckg.createanimal as create

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<animal>/<name>')
def users_animal(animal, name):

    return create.create_animal(animal, name)

if __name__ == '__main__':
    app.run(debug=True)
