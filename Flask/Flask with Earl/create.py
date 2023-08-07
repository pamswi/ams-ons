# import the app and the db from app.py
from dbapp import db, app, User, Person


with app.app_context():
    db.drop_all()
    db.create_all()

    testuser = User(username="pampam")
    db.session.add(testuser)
    db.session.commit()

    testperson=Person(first_name="Pam", last_name="Swi")
    db.session.add(testperson)
    db.session.commit()
