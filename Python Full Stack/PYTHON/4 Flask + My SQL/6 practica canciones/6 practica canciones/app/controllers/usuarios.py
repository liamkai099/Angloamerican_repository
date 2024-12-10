# app/controllers/usuarios.py
from flask import render_template, redirect, request, url_for
from app import app
from app.models.usuario import Usuario
from app.models.cancion import Cancion
from app.models.favorito import Favorito

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.get_all()
    return render_template('usuarios/index.html', usuarios=usuarios)

@app.route('/usuarios/nuevo', methods=['POST'])
def crear_usuario():
    Usuario.save(request.form)
    return redirect('/usuarios')

@app.route('/usuarios/<int:id>')
def mostrar_usuario(id):
    usuario = Usuario.get_by_id({'id': id})
    return render_template('usuarios/mostrar_usuarios.html', usuario=usuario, canciones=Cancion.get_all())




