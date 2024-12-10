from app.config.mysqlconnection import connectToMySQL
from app.models.course import Course

class Student:
    db_name = "esquema_estudiante_curso"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.curso_id = data['curso_id']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
            VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_by_course(cls, curso_id):
        query = """
            SELECT * FROM estudiantes
            WHERE curso_id = %(curso_id)s;
        """
        data = {'curso_id': curso_id}
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return [cls(estudiante) for estudiante in results]

