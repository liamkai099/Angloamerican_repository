import pymysql.cursors  # Utilizamos un cursor para interactuar con la BD

class MySQLConnection:  # Clase que permite generar instancia de conexión con la BD
    def __init__(self, db):
        connection = pymysql.connect(
            host='localhost',
            user='root',  # Cambia el usuario y contraseña
            password='oracle099',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection  # Establecemos conexión con la BD

    # El método que se encarga de la consulta
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                # Generamos la consulta con los datos
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                # Ejecutamos la consulta
                cursor.execute(query, data)

                if query.lower().find("insert") >= 0:
                    # La consulta INSERT regresa el id del nuevo registro
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # La consulta SELECT regresa una LISTA DE DICCIONARIOS con los datos
                    result = cursor.fetchall()
                    return result if result else []  # Regresa lista vacía si no hay resultados
                else:
                    # UPDATE y DELETE no regresan datos
                    self.connection.commit()
                    return None
            except Exception as e:
                # En caso de alguna falla, regresa una lista vacía para evitar errores
                print("Something went wrong:", e)
                return []  # Cambiamos False por una lista vacía
            finally:
                # Cerramos conexión
                self.connection.close()

# connectToMySQL recibe el nombre de la base de datos y genera una instancia de MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
