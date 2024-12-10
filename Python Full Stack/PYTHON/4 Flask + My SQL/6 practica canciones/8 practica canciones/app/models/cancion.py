# app/models/cancion.py
from app.config.mysqlconnection import connectToMySQL
from app.models.favorito import Favorito  # Importamos el modelo de Favorito para la relación con usuarios

class Cancion:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.artista = data['artista']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuarios = []  # Lista de usuarios que marcaron esta canción como favorita

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO canciones (titulo, artista, created_at, updated_at)
            VALUES (%(titulo)s, %(artista)s, NOW(), NOW());
        """
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
        if result:
            cancion = cls(result[0])
            # Obtenemos los usuarios que marcaron esta canción como favorita
            cancion.usuarios = Favorito.obtener_usuarios_por_cancion({'cancion_id': cancion.id})
            return cancion
        return None


