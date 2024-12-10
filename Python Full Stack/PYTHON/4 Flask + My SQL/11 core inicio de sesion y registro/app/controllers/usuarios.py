from flask import render_template, request, redirect, session, flash 
from app import app
from app.models.usuario import Usuario

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    # Validar datos del formulario
    if not Usuario.validar_usuario(request.form):
        return redirect("/")
    
    # Crear nuevo usuario
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirmpassword": request.form["confirmpassword"]  # Modificado para que coincida con el formulario
    }
    id_usuario = Usuario.registrar(data)
    session["id_usuario"] = id_usuario  # Guardar usuario en sesión
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    # Validar credenciales
    usuario = Usuario.validar_login(request.form)
    if not usuario:
        return redirect("/")
    
    session["id_usuario"] = usuario["id_usuario"]  # Guardar usuario en sesión
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "id_usuario" not in session:
        return redirect("/")
    
    usuario = Usuario.obtener_por_id(session["id_usuario"])
    return render_template("dashboard.html", usuario=usuario)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
