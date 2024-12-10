from flask import Flask, render_template, request, redirect, url_for, session
import random  # Importamos la librería random

app = Flask(__name__)

# Establecemos la clave secreta para usar sesiones
app.secret_key = 'mi_clave_secreta'

@app.route('/')
def index():
    # Muestra el formulario al usuario
    return render_template('juegodestino3.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    # Guardar los datos en la sesión
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    session['profesion'] = request.form['profesion']  # Guardamos la profesión

    # Redirige a la página que mostrará el futuro
    return redirect(url_for('futuro'))

@app.route('/futuro')
def futuro():
    # Obtener los datos de la sesión
    nombre = session.get('nombre')
    lugar = session.get('lugar')
    numero = session.get('numero')
    comida = session.get('comida')
    profesion = session.get('profesion')  # Recuperamos la profesión

    # Elegir aleatoriamente entre los dos mensajes
    mensaje = random.choice([  # Aquí elegimos aleatoriamente entre los dos mensajes
        f"Soy el adivino del Dojo, {nombre} tendrá un viaje muy largo dentro de {numero} años a {lugar} y estará el resto de sus días preparando {comida} para todas las personas que quiere. Cambió de profesión y ahora es {profesion}.",
        f"Soy el adivino del Dojo, {nombre} tendrá {numero} años de mala suerte, nunca conocerá {lugar} y jamás volvió a comer {comida}."
    ])

    # Mostrar la predicción con el mensaje aleatorio
    return render_template('futuro3.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
