# app/controllers/favoritos.py

from flask import redirect, request
from app import app
from app.models.favorito import Favorito

# Ruta para agregar una canción a los favoritos de un usuario
@app.route('/usuarios/<int:usuario_id>/favorito', methods=['POST'])
def agregar_favorito_usuario(usuario_id):
    data = {
        "usuario_id": usuario_id,
        "cancion_id": request.form['cancion_id']
    }
    # Agregar la canción a los favoritos del usuario
    Favorito.agregar(data)
    return redirect(f'/usuarios/{usuario_id}')

# Ruta para agregar un usuario como favorito de una canción
@app.route('/canciones/<int:cancion_id>/favorito', methods=['POST'])
def agregar_favorito_cancion(cancion_id):
    data = {
        "usuario_id": request.form['usuario_id'],
        "cancion_id": cancion_id
    }
    # Agregar el usuario a los favoritos de la canción
    Favorito.agregar(data)
    return redirect(f'/canciones/{cancion_id}')


