from flask import Flask, render_template, request, redirect, session

import random

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

# Diccionario para definir las reglas de reliquias por lugar
REGLAS = {
    'templo': lambda: random.randint(10, 20),
    'pirámide': lambda: random.randint(5, 10),
    'selva': lambda: random.randint(2, 5),
    'ruinas': lambda: random.choice([random.randint(-50, -1), random.randint(1, 50)]),  # Ganar o perder
}


@app.route('/')
def index():
    # Inicializa la sesión si es la primera vez que se carga
    session.setdefault('reliquias', 0)
    session.setdefault('actividades', [])
    session.setdefault('exploraciones', 0)
    session.setdefault('ganador', False)

    # Verifica si el usuario ha ganado
    if session['reliquias'] >= 100 and session['exploraciones'] <= 15:
        session['ganador'] = True

    return render_template(
        'reliquias4.html',
        reliquias=session['reliquias'],
        actividades=reversed(session['actividades']),  # Mostrar las actividades en orden descendente
        ganador=session['ganador']
    )


@app.route('/buscar_reliquias', methods=['POST'])
def buscar_reliquias():
    # Obtén el lugar enviado desde el formulario
    lugar = request.form.get('lugar')

    # Calcula las reliquias según el lugar (evitando condicionales)
    reliquias_obtenidas = REGLAS.get(lugar, lambda: 0)()  # Si no hay lugar, devuelve 0 por defecto
    session['reliquias'] += reliquias_obtenidas

    # Determina el color de la actividad según la ganancia o pérdida
    color_clase = "text-success" if reliquias_obtenidas > 0 else "text-danger"

    # Actualiza actividades
    actividad = {
        "mensaje": (
            f"Se obtuvo {reliquias_obtenidas} reliquias en el {lugar}" 
            if reliquias_obtenidas >= 0 
            else f"Se derrumbó la {lugar}! Perdiste {-reliquias_obtenidas} reliquias"
        ),
        "clase": color_clase,
    }
    session['actividades'].append(actividad)
    
    # Incrementa el contador de exploraciones
    session['exploraciones'] += 1

    return redirect('/')



@app.route('/reiniciar')
def reiniciar():
    # Reinicia la sesión para empezar de nuevo
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)