from flask_sqlalchemy import SQLAlchemy

#Se instancia la DB
db = SQLAlchemy()

class Docente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String(20))
    email = db.Column(db.String)
    password = db.Column (db.String(20))


