from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),unique=True)
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    time = db.Column(db.String(100))
    key = db.Column(db.Boolean,default=True)



