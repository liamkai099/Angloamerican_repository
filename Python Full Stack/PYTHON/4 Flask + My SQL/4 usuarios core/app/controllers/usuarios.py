from flask import render_template, request, redirect
from app import app
from app.models.usuario import Usuario

# Ruta principal: muestra todos los usuarios
@app.route("/")
def index():
    usuarios = Usuario.get_all()  # Obtiene todos los usuarios
    return render_template("index.html", usuarios=usuarios)

# Ruta para mostrar el formulario de creación de usuario
@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("nuevo usuario.html")

# Ruta para procesar el formulario de creación de usuario
@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    datos = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
    }
    Usuario.save(datos)  # Guarda el nuevo usuario en la base de datos
    return redirect("/")

# Ruta para mostrar un usuario específico
@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    usuario = Usuario.get_one({"id": id})  # Obtiene un solo usuario por ID
    return render_template("ver usuario.html", usuario=usuario)

# Ruta para mostrar el formulario de edición de un usuario
@app.route("/usuarios/editar/<int:id>")
def editar_usuario(id):
    usuario = Usuario.get_one({"id": id})  # Obtiene el usuario por ID
    return render_template("editar.html", usuario=usuario)

# Ruta para procesar la edición de un usuario
@app.route("/usuarios/actualizar/<int:id>", methods=["POST"])
def actualizar_usuario(id):
    datos = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
    }
    Usuario.update(datos)  # Actualiza el usuario en la base de datos
    return redirect("/")

# Ruta para eliminar un usuario
@app.route("/usuarios/borrar/<int:id>")
def borrar_usuario(id):
    Usuario.delete({"id": id})  # Elimina el usuario de la base de datos
    return redirect("/")


