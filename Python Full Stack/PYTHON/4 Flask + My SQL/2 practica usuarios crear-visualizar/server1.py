from flask import Flask, render_template, request, redirect
from usuarios import Usuario  # Importa la clase Usuario

app = Flask(__name__)

@app.route("/usuarios")
def index():
    usuarios = Usuario.get_all()  # Obtiene todos los usuarios
    return render_template("index.html", todos_usuarios=usuarios)

@app.route("/usuarios/nuevo", methods=['GET'])
def nuevo_usuario():
    return render_template("nuevo usuario.html")

@app.route("/usuarios/crear", methods=['POST'])
def crear_usuario():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.save(datos)  # Guarda el nuevo usuario
    return redirect('/usuarios')  # Redirige a la lista de usuarios

if __name__ == "__main__":
    app.run(debug=True)


