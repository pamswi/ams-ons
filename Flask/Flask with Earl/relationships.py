from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

db = SQLAlchemy(app)

# set up a table in a db using python syntax
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products = db.relationship('prodOrder', backref='order')
    
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), nullable=False)
    orders = db.relationship('prodOrder', backref='product')

class prodOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('products.id'))





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)