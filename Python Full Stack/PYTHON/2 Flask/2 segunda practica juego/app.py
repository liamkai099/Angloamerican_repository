from flask import Flask, render_template

app = Flask(__name__)

# Nivel 1: Ruta que muestra 3 pelotas rojas por defecto
@app.route('/juego')
def juego():
    return render_template('juego.html', cantidad=3, color='red')

# Nivel 2: Ruta que muestra 'x' pelotas rojas
@app.route('/juego/<int:x>')
def juego_con_cantidad(x):
    return render_template('juego.html', cantidad=x, color='red')

# Nivel 3: Ruta que muestra 'x' pelotas del color indicado
@app.route('/juego/<int:x>/<color>')
def juego_con_cantidad_y_color(x, color):
    return render_template('juego.html', cantidad=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)
