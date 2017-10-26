from flask import Flask, render_template, request
import animalpckg.createanimal as create

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    animal_greeting = None

    if request.method == 'POST':
        name = request.form['name']
        animal = request.form['animal']
        animal_greeting = create.create_animal(animal, name)


    return render_template('index.html', htmlgreeting = animal_greeting)

# @app.route('/<animal>/<name>')
# def users_animal(animal, name):
#
#     animal_greeting = create.create_animal(animal, name)
#     return render_template('animal.html', htmlgreeting = animal_greeting)

if __name__ == '__main__':
    app.run(debug=True)
