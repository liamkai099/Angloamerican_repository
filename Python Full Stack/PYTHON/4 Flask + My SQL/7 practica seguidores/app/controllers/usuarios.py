from flask import render_template, request, redirect, flash
from app import app
from app.models.usuario import Usuario
from app.models.seguidor import Seguidor

@app.route("/usuarios")
def usuarios():
    # Obtiene todos los usuarios y sus seguidores
    usuarios = Usuario.get_all()
    seguidores = Seguidor.get_all()
    return render_template("usuarios.html", usuarios=usuarios, seguidores=seguidores)

@app.route("/nuevo_usuario", methods=["POST"])
def nuevo_usuario():
    # Procesa la creación de un nuevo usuario
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(data)
    flash("Usuario creado exitosamente")
    return redirect("/usuarios")


