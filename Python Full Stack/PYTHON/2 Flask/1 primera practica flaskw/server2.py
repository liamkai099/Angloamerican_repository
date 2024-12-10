from flask import Flask, render_template  # Importamos render_template

app = Flask(__name__)

@app.route('/bienvenido')

def bienvenido():

    #En vez de regresar una cadena, regresamos el resultado del método render_template

    #enviando el nombre del archivo de HTML que queremos renderizar

    return render_template('clase1_3formulario.html')

if __name__=="__main__":   

    app.run(debug=True)