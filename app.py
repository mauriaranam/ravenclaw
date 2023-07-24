from flask import Flask, render_template, request, redirect, url_for
from models import db, Docente




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
        return redirect(url_for('home'))
    return render_template('register.html')

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



if __name__ == "__main__":
    app.run (debug=True)    