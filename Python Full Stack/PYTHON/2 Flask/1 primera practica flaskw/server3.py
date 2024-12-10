
from flask import Flask, render_template  # Importamos render_template

app = Flask(__name__)

@app.route('/bienvenido')

def bienvenido():

    #Enviamos 2 nuevos argumentos

    return render_template('index3.html', cancion="dale a tu cuerpo alegría macarena", repite=5)


if __name__=="__main__":   

    app.run(debug=True)