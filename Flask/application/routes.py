from application import app
import random

first_names = ["James", "Robert", "John", "Michael", "David", "Pam"]
last_names = ["Wilson", "Davis", "Taylor", "Johnson", "Anderson", "Smith"]


@app.route('/') 
def index(): 
	
    fn = random.randint(0,5)
    ls = random.randint(0,5)
   
    return (first_names[fn] +" " + last_names[ls])
