from flask_sqlalchemy import SQLAlchemy
from datetime import date


#Se instancia la DB
db = SQLAlchemy()

class Docente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String(20),nullable=False, unique=True)
    email = db.Column(db.String,nullable=False,unique=True)
    password = db.Column (db.String(20),nullable=False)


class Cv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    docente_id = db.Column(db.Integer, db.ForeignKey('docente.id'), nullable=False) # Creador de la receta
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    materia = db.Column(db.String)
    fecha_nac = db.Column(db.Date)
    telefono = db.Column(db.Integer)
    nivel = db.Column(db.String)





