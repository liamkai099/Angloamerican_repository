# app/__init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "clave_secreta"

# Importa los controladores para registrarlos
from app.controllers import usuarios, canciones, favoritos