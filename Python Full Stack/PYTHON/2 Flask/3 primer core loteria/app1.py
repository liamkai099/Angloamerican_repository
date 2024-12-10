from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de colores y cartas
COLORS = ['pink', '#1E90FF', 'yellow']
CARDS = [
    "1  El Gallo", "2  El Diablito", "3  La Dama", "4  El catrín", "5  El paraguas",
    "6  La sirena", "7  La escalera", "8  La botella", "9  El barril", "10 El árbol",
    "11 El melón", "12 El valiente", "13 El gorrito", "14 La muerte", "15 La pera",
    "16 La bandera", "17 El bandolón", "18 El violoncello", "19 La garza", "20 El pájaro",
    "21 La mano", "22 La bota", "23 La luna", "24 El cotorro", "25 El borracho",
    "26 El negrito", "27 El corazón", "28 La sandía", "29 El tambor", "30 El camarón",
    "31 Las jaras", "32 El músico", "33 La araña", "34 El soldado", "35 La estrella",
    "36 El cazo", "37 El mundo", "38 El apache", "39 El nopal", "40 El alacrán",
    "41 La rosa", "42 La calavera", "43 La campana", "44 El cantarito", "45 El venado",
    "46 El sol", "47 La corona", "48 La chalupa", "49 El pino", "50 El pescado",
    "51 La palma", "52 La maceta", "53 El arpa", "54 La rana"
]

@app.route('/')
def index():
    return "Bienvenido a la Lotería. Visita /loteria para ver el tablero."

# Ruta para un tablero de 4x4
@app.route('/loteria')
def loteria_default():
    grid = []
    for i in range(4):
        row = []
        for j in range(4):
            color_index = (i + j) % len(COLORS)  # Seleccionar color alternado
            cell = {'color': COLORS[color_index]}  # Solo se define el color
            row.append(cell)
        grid.append(row)
    return render_template('loteriaapp1.html', grid=grid, rows=4, cols=4)



# Ruta con número de filas especificado
@app.route('/loteria/<int:rows>')
def loteria_con_filas(rows):
    return generar_tablero(rows, 4)

# Ruta con filas y columnas especificadas
@app.route('/loteria/<int:rows>/<int:cols>')
def loteria_con_filas_y_columnas(rows, cols):
    return generar_tablero(rows, cols)

# Función que genera el tablero
def generar_tablero(rows, cols):
    # Generar un patrón de colores y cartas aleatorias para cada celda
    grid = []
    available_cards = CARDS.copy()  # Copia de las cartas para no repetir
    for i in range(rows):
        row = []
        for j in range(cols):
            color_index = (i + j) % len(COLORS)  # Seleccionar color alternado
            card = random.choice(available_cards)  # Carta aleatoria
            available_cards.remove(card)  # Remover carta para evitar repeticiones
            # Diccionario con información de la celda
            cell = {
                'color': COLORS[color_index],
                'card': card,
                'number': card.split()[0],  # Número de la carta
                'name': ' '.join(card.split()[1:])  # Nombre de la carta
            }
            row.append(cell)
        grid.append(row)
    return render_template('loteriaapp1.html', grid=grid, rows=rows, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)

