from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_restless
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
CORS(app)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    name = db.Column(db.String(255), unique=True)
    captured = db.Column(db.Boolean)
    description = db.Column(db.String(255))
    type = db.Column(db.String(255))
    attacks = db.Column(db.String(255))


db.create_all()

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Pokemon, methods=['GET', 'POST', 'DELETE'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
