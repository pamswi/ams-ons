# import the module you need
from flask import Flask 
import random

app = Flask(__name__) 

first_names = ["James", "Robert", "John", "Michael", "David", "Pam"]
last_names = ["Wilson", "Davis", "Taylor", "Johnson", "Anderson", "Smith"]

@app.route('/') 
def index(): 
	
    fn = random.randint(0,5)
    ls = random.randint(0,5)
   
    return (first_names[fn] +" " + last_names[ls])

if __name__ == '__main__':
	app.run(debug=True)