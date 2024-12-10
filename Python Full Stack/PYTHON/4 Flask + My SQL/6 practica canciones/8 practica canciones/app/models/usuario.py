# app/models/usuario.py
from app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.contrasena = data['contrasena']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, email, contrasena, created_at, updated_at) VALUES (%(nombre)s, %(email)s, %(contrasena)s, NOW(), NOW())"
        return connectToMySQL('esquema_canciones').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios"
        results = connectToMySQL('esquema_canciones').query_db(query)
        return [cls(user) for user in results]

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('esquema_canciones').query_db(query, data)
        return cls(result[0]) if result else None


