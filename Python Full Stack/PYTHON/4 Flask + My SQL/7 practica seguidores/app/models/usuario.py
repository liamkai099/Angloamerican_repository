from app.config.mysqlconnection import connectToMySQL

class Usuario:
    db_name = "esquema_seguidores"

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.db_name).query_db(query)
        return [cls(user) for user in results]

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL(cls.db_name).query_db(query, data)



