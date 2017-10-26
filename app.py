from flask import Flask, render_template
import animalpckg.createanimal as create

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<animal>/<name>')
def users_animal(animal, name):

    animal_greeting = create.create_animal(animal, name)
    return render_template('animal.html', htmlgreeting = animal_greeting)

if __name__ == '__main__':
    app.run(debug=True)
