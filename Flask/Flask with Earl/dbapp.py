from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

# set up a table in a db using python syntax
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), default="John")
    last_name = db.Column(db.String(30), unique=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)