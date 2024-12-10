from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.route('/')
def index():
    # Inicializa variables de sesión si no existen
    if 'reliquias' not in session:
        session['reliquias'] = 0
    if 'actividades' not in session:
        session['actividades'] = []
    if 'exploraciones' not in session:
        session['exploraciones'] = 0
    if 'ganador' not in session:
        session['ganador'] = False

    return render_template('reliquias3.html', reliquias=session['reliquias'], 
                            actividades=session['actividades'], 
                            ganador=session['ganador'])

@app.route('/buscar_reliquias', methods=['POST'])
def buscar_reliquias():
    lugar = request.form['lugar']
    import random

    if lugar == 'templo':
        reliquias = random.randint(10, 20)
        session['actividades'].append(f"Se obtuvieron {reliquias} en el {lugar}")
    elif lugar == 'piramide':
        reliquias = random.randint(5, 10)
        session['actividades'].append(f"Se obtuvieron {reliquias} en la {lugar}")
    elif lugar == 'selva':
        reliquias = random.randint(2, 5)
        session['actividades'].append(f"Se obtuvieron {reliquias} en la {lugar}")
    elif lugar == 'ruinas':
        reliquias = random.randint(-50, 50)
        if reliquias >= 0:
            session['actividades'].append(f"Se obtuvieron {reliquias} en las {lugar}")
        else:
            session['actividades'].append(f"Se derrumbó la ruina! Perdiste {abs(reliquias)} en las {lugar}")

    # Incrementa exploraciones
    session['exploraciones'] += 1

    # Actualiza las reliquias
    session['reliquias'] += reliquias

    # Verifica condición de victoria
    if session['reliquias'] >= 100 and session['exploraciones'] <= 15:
        session['ganador'] = True

    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    # Reinicia la sesión
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)