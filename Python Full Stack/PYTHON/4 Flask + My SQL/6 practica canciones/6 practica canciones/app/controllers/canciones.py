# app/controllers/canciones.py
from flask import render_template, redirect, request
from app import app
from app.models.cancion import Cancion
from app.models.usuario import Usuario
from app.models.favorito import Favorito

@app.route('/canciones')
def canciones():
    canciones = Cancion.get_all()
    return render_template('canciones/index.html', canciones=canciones)

@app.route('/canciones/nueva', methods=['POST'])
def crear_cancion():
    Cancion.save(request.form)
    return redirect('/canciones')

@app.route('/canciones/<int:id>')
def mostrar_cancion(id):
    cancion = Cancion.get_by_id({'id': id})
    return render_template('canciones/mostrar_cancion.html', cancion=cancion, usuarios=Usuario.get_all())
