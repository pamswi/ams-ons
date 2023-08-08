from application import app, db
from application.models import Games

@app.route('/add/<new_game>')
def add(new_game):
    new_game = Games(name=new_game)
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete/<name_todelete>')
def delete(name_todelete):
    game_to_delete = Games.query.filter_by(name=name_todelete).first()
    print(game_to_delete)
    db.session.delete(game_to_delete)
    db.session.commit()
    return "You have deleted the entry"


@app.route('/count')
def count():
    games_to_display = Games.query.count()
    return f"the number of games in the database is: {games_to_display}"