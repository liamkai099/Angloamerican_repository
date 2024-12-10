# app/controllers/canciones.py
from flask import render_template, redirect, request, url_for  # Importar url_for para redirección
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
    # Obtener la canción por ID
    cancion = Cancion.get_by_id({'id': id})
    # Renderizar la página con todos los usuarios y la canción obtenida
    return render_template('canciones/mostrar_cancion.html', cancion=cancion, usuarios=Usuario.get_all())

@app.route('/canciones/<int:id>/favorito', methods=['POST'])
def agregar_favorito_a_cancion(id):
    """
    Agregar la relación de favorito entre la canción y un usuario
    """
    data = {
        'usuario_id': request.form['usuario_id'],
        'cancion_id': id
    }
    # Verificar si el favorito ya existe para evitar duplicados
    if not Favorito.existe_favorito(data):
        Favorito.agregar(data)  # Agregar el favorito

    # Redirigir a la página de mostrar canción
    return redirect(url_for('mostrar_cancion', id=id))
