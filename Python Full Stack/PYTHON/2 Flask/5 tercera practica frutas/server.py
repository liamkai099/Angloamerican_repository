from flask import Flask, render_template, request
from datetime import datetime  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    # Capturamos los datos del formulario y convertimos las cantidades a enteros
    order_data = {
        'fresa': int(request.form.get('fresa', 0)),
        'moras': int(request.form.get('moras', 0)),
        'frambuesa': int(request.form.get('frambuesa', 0)),
        'manzana': int(request.form.get('manzana', 0)),
        'nombre': request.form.get('nombre', ''),
        'apellido': request.form.get('apellido', ''),
        'email': request.form.get('email', ''),
    }

    # Calcular el total de elementos
    order_data['total'] = (
        order_data['fresa']
        + order_data['moras']
        + order_data['frambuesa']
        + order_data['manzana']
    )

    order_data['fecha'] = datetime.now().strftime('%d de %B %Y')

    return render_template("checkout.html", data=order_data)

@app.route('/frutas')
def fruits():
    return render_template("frutas.html")

if __name__ == "__main__":
    app.run(debug=True)
