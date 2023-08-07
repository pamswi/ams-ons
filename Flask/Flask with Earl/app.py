# install flask with pip, then import all the necessary modules
from flask import Flask, request, redirect, url_for
import os 
from flask_sqlalchemy import SQLAlchemy

# create a flask object (app) "the executable"
app = Flask(__name__)

# db config using sqlite for develpoment environement (built-in database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# set up a db object (the object will have its own methods)
db = SQLAlchemy(app)

# db config using db-URI (cloud in production)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:3501@localhost:3306/mydatabase'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
# terminal command to set up environement variable: DATABASE_URI='mysql+pymysql://root:3501@localhost:3306/mydatabase'
# can then be used as a variable  {os.getenv('DATABASE_URI')}


@app.route('/')   # /route for all routes (get byu default)
def home():
    return "hello internet"

@app.route('/about')
def about():
    return "this is the about page"

# route with specifying request methods of get and post
@app.route('/postoption', methods=["GET", "POST"])
def posto():
    print(request.method)
    # if request.method == "POST":
    return f"method is {request.method}"


# route with url parameters
@app.route('/name/<word>')  # <int:word> for integets rather than strings
def name(word):
    return f"{word} <br>"*5



# redirect function
@app.route('/google')
def gotogoogle():
    return redirect('https://www.google.com')

# url_for() function for finding url of another function in flask
@app.route('/gotohome')
def gotohome():
    return redirect (url_for("home"))  # url_for is looking for a function name rather than the route
    

 # route exercise
@app.route('/<int:number>')
def square(number):
    square = number **2
    return f"{square}"





# the run statement; only run the app if the file is the main file
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

    # debug=True; more info in the terminal; when working in the develpoment environement rather than production
    # host is the local machine
    # port is 5000 by default unless specified otherwise