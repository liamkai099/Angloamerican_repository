from flask import Flask

app = Flask(__name__)

# Ruta raíz que responde con "¡Hola desde Flask!"
@app.route('/')
def hello():
    return "¡Hola desde Flask!"

# Ruta "/ruta" que responde con "¿Qué ruta estás buscando?"
@app.route('/ruta')
def ruta():
    return "¿Qué ruta estás buscando?"

# Ruta para "bienvenido/nombre" que muestra un saludo personalizado
@app.route('/bienvenido/<nombre>')
def bienvenida(nombre):
    # Verificar si el nombre es una cadena (Bonus de Plata)
    if isinstance(nombre, str):
        return f"Bienvenid@ a esta ruta {nombre.capitalize()}"
    else:
        return "¡Sobrecarga de rutas! No encontramos a donde quieres ir, inténtalo de nuevo."

# Ruta para repetir una palabra especificada un número de veces
@app.route('/repite/<int:num>/<palabra>')
def repite(num, palabra):
    # Verificar si el número es un entero y la palabra es una cadena (Bonus de Plata)
    if isinstance(num, int) and isinstance(palabra, str):
        return f"Repite después de mi: {' '.join([palabra] * num)}"
    else:
        return "¡Sobrecarga de rutas! No encontramos a donde quieres ir, inténtalo de nuevo."

# Manejo de rutas no especificadas (Bonus de Oro)
@app.errorhandler(404)
def page_not_found(error):
    return "¡Sobrecarga de rutas! No encontramos a donde quieres ir, inténtalo de nuevo."

if __name__ == '__main__':
    app.run(debug=True)
