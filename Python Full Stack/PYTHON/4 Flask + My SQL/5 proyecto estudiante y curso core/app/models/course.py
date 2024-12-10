from app.config.mysqlconnection import connectToMySQL

class Course:
    db_name = "esquema_estudiante_curso"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        results = connectToMySQL(cls.db_name).query_db(query)
        return [cls(curso) for curso in results]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM cursos WHERE id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(result[0]) if result else None

