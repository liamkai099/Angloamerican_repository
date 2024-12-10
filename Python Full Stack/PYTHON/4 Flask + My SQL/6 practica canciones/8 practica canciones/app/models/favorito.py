# app/models/favorito.py

from app.config.mysqlconnection import connectToMySQL

class Favorito:
    def __init__(self, id, usuario_id, cancion_id, created_at, updated_at):
        self.id = id
        self.usuario_id = usuario_id
        self.cancion_id = cancion_id
        self.created_at = created_at
        self.updated_at = updated_at

    # Método para agregar un favorito
    @staticmethod
    def agregar(data):
        query = """
            INSERT INTO favoritos (usuario_id, cancion_id, created_at, updated_at)
            VALUES (%(usuario_id)s, %(cancion_id)s, NOW(), NOW());
        """
        return connectToMySQL('esquema_canciones').query_db(query, data)

    # Método para verificar si un favorito ya existe
    @staticmethod
    def existe_favorito(data):
        query = """
            SELECT * FROM favoritos
            WHERE usuario_id = %(usuario_id)s AND cancion_id = %(cancion_id)s;
        """
        result = connectToMySQL('esquema_canciones').query_db(query, data)
        return len(result) > 0  # Devuelve True si existe

    # Método para obtener todos los favoritos de un usuario
    @staticmethod
    def obtener_favoritos_por_usuario(data):
        query = """
            SELECT canciones.* FROM favoritos
            JOIN canciones ON favoritos.cancion_id = canciones.id
            WHERE favoritos.usuario_id = %(usuario_id)s;
        """
        results = connectToMySQL('esquema_canciones').query_db(query, data)
        return results

    # Método para obtener todos los usuarios que marcaron una canción como favorita
    @staticmethod
    def obtener_usuarios_por_cancion(data):
        query = """
            SELECT usuarios.* FROM favoritos
            JOIN usuarios ON favoritos.usuario_id = usuarios.id
            WHERE favoritos.cancion_id = %(cancion_id)s;
        """
        results = connectToMySQL('esquema_canciones').query_db(query, data)
        return [usuario for usuario in results]  # Convertir resultados a una lista de usuarios

    # Método para obtener todas las canciones marcadas como favoritas (opcional)
    @staticmethod
    def obtener_todos_favoritos():
        query = """
            SELECT favoritos.*, usuarios.nombre AS usuario_nombre, canciones.titulo AS cancion_titulo
            FROM favoritos
            JOIN usuarios ON favoritos.usuario_id = usuarios.id
            JOIN canciones ON favoritos.cancion_id = canciones.id;
        """
        results = connectToMySQL('esquema_canciones').query_db(query)
        return results
