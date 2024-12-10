from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        """Obtiene todos los registros de la tabla usuarios"""
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('usuario_practica').query_db(query)
        usuarios = []
        for row in results:
            usuarios.append(cls(row))  # Crea instancias de Usuario por cada registro
        return usuarios

    @classmethod
    def get_one(cls, data):
        """Obtiene un solo usuario basado en el ID"""
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('usuario_practica').query_db(query, data)
        if result:  # Verifica que la consulta devuelva un resultado
            return cls(result[0])  # Retorna la primera fila como una instancia de Usuario
        return None

    @classmethod
    def save(cls, data):
        """Inserta un nuevo registro en la tabla usuarios"""
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) 
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL('usuario_practica').query_db(query, data)

    @classmethod
    def update(cls, data):
        """Actualiza un registro existente basado en el ID"""
        query = """
            UPDATE usuarios 
            SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL('usuario_practica').query_db(query, data)

    @classmethod
    def delete(cls, data):
        """Elimina un registro basado en el ID"""
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('usuario_practica').query_db(query, data)

