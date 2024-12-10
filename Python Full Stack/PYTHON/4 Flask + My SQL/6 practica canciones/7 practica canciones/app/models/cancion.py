# app/models/cancion.py
from app.config.mysqlconnection import connectToMySQL

class Cancion:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.artista = data['artista']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO canciones (titulo, artista, created_at, updated_at) VALUES (%(titulo)s, %(artista)s, NOW(), NOW())"
        return connectToMySQL('esquema_canciones').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM canciones"
        results = connectToMySQL('esquema_canciones').query_db(query)
        return [cls(song) for song in results]

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM canciones WHERE id = %(id)s"
        result = connectToMySQL('esquema_canciones').query_db(query, data)
        return cls(result[0]) if result else None


