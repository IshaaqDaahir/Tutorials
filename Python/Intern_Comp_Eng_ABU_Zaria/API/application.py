from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# app.app_context().push()

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__ (self):
        return f"{self.name} - {self.description}"


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}

        output.append(drink_data)
    return {'drinks': output}

@app.route('/drinks/<id>', methods=['GET'])
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name, 'description': drink.description}

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {'Error': 'Not found!'}
    db.session.delete(drink)
    db.session.commit()
    return f'"{drink.name}" deleted successfully!'

""" @app.route('/drinks/<id>', methods=['PUT'])
def update_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return f'Error, not found!'
    db.session.update(drink)
    db.session.commit()
    return f'"{drink.name}" updated successfully!' """

if __name__ == '__main__':
    app.run(debug=True)

