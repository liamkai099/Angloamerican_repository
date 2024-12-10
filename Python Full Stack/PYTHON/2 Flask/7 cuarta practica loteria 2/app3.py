from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Arreglo con las cartas

@app.route("/")
def index():
    if "numero_aleatorio" not in session:
        session["numero_aleatorio"] = random.randint(1, 54)  # Generar número aleatorio entre 1 y 54
    return render_template(
        "loteria4.html",
        mensaje="¡Intenta adivinar el número!",
        color="warning",
        mostrar_formulario=True
    )

@app.route("/adivinar", methods=["POST"])
def adivinar():
    # Verificar si el contador de intentos está en la sesión, si no, iniciarlo
    if "intentos" not in session:
        session["intentos"] = 0  # Inicializar contador de intentos

    numero_usuario = int(request.form["numero"])
    numero_aleatorio = session["numero_aleatorio"]
    
    # Incrementar el contador de intentos
    session["intentos"] += 1

    if numero_usuario > numero_aleatorio:
        mensaje = "Tu número es mayor al de la carta"
        color = "danger"
        mostrar_formulario = True
    elif numero_usuario < numero_aleatorio:
        mensaje = "Tu número es menor al de la carta"
        color = "danger"
        mostrar_formulario = True
    else:
        # Mostrar el número de intentos cuando adivinen correctamente
        mensaje = f"¡Lotería! El número es {numero_aleatorio} y su carta es: {cartas[numero_aleatorio]}. Te tomó {session['intentos']} intentos."
        color = "success"
        mostrar_formulario = False
        session.pop("numero_aleatorio", None)  # Reinicia para un nuevo juego
        session.pop("intentos", None)  # Reinicia el contador de intentos para un nuevo juego

    return render_template(
        "loteria4.html",
        mensaje=mensaje,
        color=color,
        mostrar_formulario=mostrar_formulario
    )


cartas = [
    "0 - Carta no válida",
    "1 El Gallo", "2 El Diablito", "3 La Dama", "4 El Catrín", "5 El Paraguas",
    "6 La Sirena", "7 La Escalera", "8 La Botella", "9 El Barril", "10 El Árbol",
    "11 El Melón", "12 El Valiente", "13 El Gorrito", "14 La Muerte", "15 La Pera",
    "16 La Bandera", "17 El Bandolón", "18 El Violoncello", "19 La Garza", "20 El Pájaro",
    "21 La Mano", "22 La Bota", "23 La Luna", "24 El Cotorro", "25 El Borracho",
    "26 El Negrito", "27 El Corazón", "28 La Sandía", "29 El Tambor", "30 El Camarón",
    "31 Las Jaras", "32 El Músico", "33 La Araña", "34 El Soldado", "35 La Estrella",
    "36 El Cazo", "37 El Mundo", "38 El Apache", "39 El Nopal", "40 El Alacrán",
    "41 La Rosa", "42 La Calavera", "43 La Campana", "44 El Cantarito", "45 El Venado",
    "46 El Sol", "47 La Corona", "48 La Chalupa", "49 El Pino", "50 El Pescado",
    "51 La Palma", "52 La Maceta", "53 El Arpa", "54 La Rana"
]


if __name__ == "__main__":
    app.run(debug=True)