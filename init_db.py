from models import db, Docente, Cv
from flask import Flask

app = Flask("app")

# configurar la base de datos SQLite

# Indicamos la conexion a la base de datos

# Para desactivar el seguimiento de modificaciones en la base de datos con SQLALCHEMY. 
#Esto puede mejorar el rendimiento y evitar problemas de uso excesivo de memoria al no realizar un 
# seguimiento detallado de los cambios en los objetos de la base de datos.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)


# Crear base de datoos
with app.app_context():
    db.create_all()

