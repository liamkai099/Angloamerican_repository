from flask import Flask, session, redirect, url_for, render_template, request


app = Flask(__name__)

# Clave secreta para la sesión (necesaria para habilitar sesiones)
app.secret_key = "clave_secreta_super_segura"

@app.route('/')
def index():
    # Verifica si existe la clave 'visitas' en la sesión
    if 'visitas' not in session:
        session['visitas'] = 0  # Inicializa el contador en 0 si no existe
    if 'reinicios' not in session:
        session['reinicios'] = 0  # Inicializa el contador de reinicios en 0 si no existe
    session['visitas'] += 1  # Incrementa el contador de visitas solo en la ruta principal
    return render_template('index2.html', visitas=session['visitas'], reinicios=session['reinicios'])

@app.route('/aumentar_dos')
def aumentar_dos():
    # Incrementa las visitas en 2 sobre el valor actual
    if 'visitas' not in session:
        session['visitas'] = 2  # Si no hay visitas registradas, inicializa con 2
    else:
        session['visitas'] += 2  # Suma 2 al valor actual
    return render_template('index2.html', visitas=session['visitas'], reinicios=session['reinicios'])

@app.route('/reiniciar')
def reiniciar_visitas():
    # Incrementa el contador de reinicios y reinicia el contador de visitas a 0
    if 'reinicios' not in session:
        session['reinicios'] = 0  # Inicializa el contador de reinicios si no existe
    session['reinicios'] += 1  # Incrementa el contador de reinicios
    session['visitas'] = 0  # Reinicia las visitas
    return redirect(url_for('index'))

@app.route('/aumentar_personalizado', methods=['POST'])
def aumentar_personalizado():
    # Obtiene el valor del formulario
    incremento = int(request.form.get('cantidad', 0))
    session['visitas'] = session.get('visitas', 0) + incremento
    return redirect(url_for('index'))

@app.route('/destruir_sesion')
def destruir_sesion():
    # Elimina toda la información de la sesión
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
