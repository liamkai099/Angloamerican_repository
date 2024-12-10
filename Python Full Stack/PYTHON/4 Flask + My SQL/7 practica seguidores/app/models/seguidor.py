from app.config.mysqlconnection import connectToMySQL

class Seguidor:
    db_name = "esquema_seguidores"

    def __init__(self, data):
        self.id = data["id"]
        self.usuario_id = data["usuario_id"]
        self.seguidor_id = data["seguidor_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO seguidores (usuario_id, seguidor_id, created_at, updated_at)
            VALUES (%(usuario_id)s, %(seguidor_id)s, NOW(), NOW());
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
            SELECT usuarios.nombre AS usuario, u2.nombre AS seguidor
            FROM seguidores
            JOIN usuarios ON seguidores.usuario_id = usuarios.id
            JOIN usuarios AS u2 ON seguidores.seguidor_id = u2.id;
        """
        return connectToMySQL(cls.db_name).query_db(query)

    @classmethod
    def is_duplicate(cls, data):
        # Verifica si el usuario intenta seguirse a sí mismo
        if data["usuario_id"] == data["seguidor_id"]:
            return True

        query = """
            SELECT * FROM seguidores
            WHERE usuario_id = %(usuario_id)s AND seguidor_id = %(seguidor_id)s;
        """
        result = connectToMySQL(cls.db_name).query_db(query, data)
        return len(result) > 0

