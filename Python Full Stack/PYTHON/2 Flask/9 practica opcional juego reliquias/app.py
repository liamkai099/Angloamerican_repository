from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secret_key_reliquias"

@app.route('/')
def index():
    # Inicializar sesión si es la primera visita
    if 'reliquias' not in session:
        session['reliquias'] = 0
        session['actividades'] = []
    
    return render_template('reliquias.html', reliquias=session['reliquias'], actividades=session['actividades'])

@app.route('/buscar_reliquias', methods=['POST'])
def buscar_reliquias():
    lugar = request.form['lugar']
    reliquias_obtenidas = 0
    mensaje = ""
    
    if lugar == 'templo':
        reliquias_obtenidas = random.randint(10, 20)
        mensaje = f"Se obtuvieron: {reliquias_obtenidas} en: templo"
    elif lugar == 'pirámide':
        reliquias_obtenidas = random.randint(5, 10)
        mensaje = f"Se obtuvieron: {reliquias_obtenidas} en: pirámide"
    elif lugar == 'selva':
        reliquias_obtenidas = random.randint(2, 5)
        mensaje = f"Se obtuvieron: {reliquias_obtenidas} en: selva"
    elif lugar == 'ruinas':
        reliquias_obtenidas = random.randint(-50, 50)
        if reliquias_obtenidas < 0:
            mensaje = f"Se derrumbó la ruina! Perdiste {-reliquias_obtenidas} reliquias en: ruinas"
        else:
            mensaje = f"Se obtuvieron: {reliquias_obtenidas} en: ruinas"
    
    # Actualizar sesión
    session['reliquias'] += reliquias_obtenidas
    session['actividades'].append(mensaje)
    
    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
