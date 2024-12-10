from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
from app import app

# Inicialización de bcrypt para manejar contraseñas hash
bcrypt = Bcrypt(app)

# Nombre de la base de datos
DATABASE = "esquema_registro"  # Asegúrate de que este sea el nombre correcto de tu base de datos

# Expresiones regulares para validación
NOMBRE_REGEX = re.compile(r"^[a-zA-ZÀ-ÿ\s]+$")  # Nombres con letras y espacios
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")  # Formato básico de email

class Usuario:
    def __init__(self, data):
        self.id_usuario = data["id_usuario"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]

    @classmethod
    def registrar(cls, data):
        # Hashing de la contraseña antes de guardarla
        hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
        data["password"] = hashed_password

        query = """
            INSERT INTO usuarios (nombre, apellido, email, password, fecha_creacion, fecha_actualizacion)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());
        """
        # Retorna el ID del nuevo usuario
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def validar_login(cls, data):
        # Verificar si el email existe en la base de datos
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if not result:
            flash("Email o contraseña incorrectos.", "danger")
            return False

        usuario = result[0]
        # Verificar la contraseña usando bcrypt
        if not bcrypt.check_password_hash(usuario["password"], data["password"]):
            flash("Email o contraseña incorrectos.", "danger")
            return False

        return usuario

    @classmethod
    def obtener_por_id(cls, id_usuario):
        query = "SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s;"
        data = {"id_usuario": id_usuario}
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result[0] if result else None

    @staticmethod
    def validar_usuario(usuario):
        is_valid = True

        # VALIDACIÓN NOMBRE
        if len(usuario['nombre']) <= 0:
            flash("El nombre no puede estar vacío.", "danger")
            is_valid = False
        elif len(usuario['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "danger")
            is_valid = False
        elif not NOMBRE_REGEX.match(usuario['nombre']):
            flash("El nombre solo puede contener letras y espacios.", "danger")
            is_valid = False

        # VALIDACIÓN APELLIDO
        if len(usuario['apellido']) <= 0:
            flash("El apellido no puede estar vacío.", "danger")
            is_valid = False
        elif len(usuario['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "danger")
            is_valid = False

        # VALIDACIÓN EMAIL
        if len(usuario['email']) <= 0:
            flash("El email no puede estar vacío.", "danger")
            is_valid = False
        elif not EMAIL_REGEX.match(usuario['email']):
            flash("El email no tiene un formato válido.", "danger")
            is_valid = False
        else:
            # Comprobamos si el email ya existe en la base de datos
            query = "SELECT * FROM usuarios WHERE email = %(email)s;"
            data = {'email': usuario['email']}
            resultado = connectToMySQL(DATABASE).query_db(query, data)
            if len(resultado) > 0:
                flash("El email ya está registrado.", "danger")
                is_valid = False

        # VALIDACIÓN PASSWORD
        if len(usuario['password']) <= 0:
            flash("La contraseña no puede estar vacía.", "danger")
            is_valid = False
        elif len(usuario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "danger")
            is_valid = False

        # VALIDACIÓN CONFIRMACIÓN PASSWORD
        if len(usuario['confirmpassword']) <= 0:
            flash("La confirmación de la contraseña no puede estar vacía.", "danger")
            is_valid = False
        if (usuario['password'] != usuario['confirmpassword']):
            flash("Las contraseñas no coinciden.", "danger")
            is_valid = False

        return is_valid
