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
    favoritos = Favorito.obtener_favoritos_por_usuario({'usuario_id': id})  # Actualiza favoritos
    canciones = Cancion.get_all()  # Canciones disponibles
    return render_template('usuarios/mostrar_usuarios.html', usuario=usuario, favoritos=favoritos, canciones=canciones)

@app.route('/usuarios/<int:usuario_id>/favorito', methods=['POST'])
def agregar_favorito(usuario_id):
    cancion_id = request.form.get('cancion_id')
    # Verificar si el favorito ya existe
    if not Favorito.existe_favorito({'usuario_id': usuario_id, 'cancion_id': cancion_id}):
        Favorito.agregar({'usuario_id': usuario_id, 'cancion_id': cancion_id})
    # Redirige nuevamente a mostrar_usuario para asegurarte de que los datos se actualicen
    return redirect(url_for('mostrar_usuario', id=usuario_id))


