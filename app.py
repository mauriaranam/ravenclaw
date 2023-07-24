from flask import Flask, render_template, request, redirect, url_for
from models import db, Docente, Cv
from datetime import datetime




app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializamos la base de datos
db.init_app(app)

@app.route("/home")
def home():
    docentes = Docente.query.all()
    return render_template("home.html", docentes=docentes)

#nueva ruta de registro
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form ['username']
        email = request.form ['email']
        password = request.form ['password']
        #Instanciamos un objeto para agg a la db
        usuario = Docente(username=username, email=email, password=password)
        #Agregar a la DB
        db.session.add(usuario)
        #Confirmo con el commit
        db.session.commit()
        global current_user
        current_user = usuario.id 
        return redirect(url_for('cv'))
    return render_template('register.html')


#ruta para login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form ['email']
        password = request.form ['password']
        usuario_db = Docente.query.filter_by(email=email).first()
        if usuario_db is not None:
            if usuario_db.password == password:
                global current_user 
                current_user = usuario_db.id
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
        elif usuario_db is None:
            return redirect(url_for('login'))  
    return render_template('login.html')

#ruta para crear CV
@app.route("/cv", methods=['POST','GET'])
def cv():
    if request.method == 'POST':
        nombre = request.form ['nombre']
        apellido = request.form ['apellido']
        materia = request.form ['materia']
        fecha_str = request.form["fecha"]
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()        
        telefono = request.form ['telefono']
        nivel = request.form ['nivel']
        docente_db = Cv(nombre=nombre, apellido=apellido, materia=materia, fecha_nac=fecha,telefono=telefono,nivel=nivel, docente_id=current_user)
        db.session.add(docente_db)
        db.session.commit()
        return redirect (url_for('home'))
    return render_template("new_cv.html")


if __name__ == "__main__":
    app.run (debug=True)    