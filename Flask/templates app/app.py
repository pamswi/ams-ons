from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
     return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/names/<letter>')
def names(letter):
     names = ["ben", "harry", "bob", "jay", "matt", "bill"]
     return render_template ('index.html', names=names, letter=letter)



if __name__ == "__main__":
     app.run(debug=True, host='0.0.0.0')