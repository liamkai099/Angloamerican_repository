# 1. Actualizar valores en diccionarios y listas


print("EJERCICIO 1 Cambia el valor de 3 en matriz por 6")
matriz = [[10, 15, 20], [3, 7, 14]]
# METODO 1 Cambiar el valor 3 por 6
matriz[1][0] = 6
# Imprimir la matriz para verificar el cambio
print(matriz)




# METODO 2 Eliminar el valor en la posición específica y agregar el nuevo valor
matriz[1].pop(0)     # Esto elimina el valor en la primera posición de la segunda fila (el 3)
matriz[1].insert(0, 6)  # Luego insertamos el 6 en la misma posición
"""Nota: Aquí usamos insert(0, 6) en lugar de append(6) porque append agrega el elemento al final 
de la sublista, mientras que insert permite especificar una posición."""
# Imprimir la matriz para verificar el cambio
print(matriz)












print("\nEJERCICIO 2: Cambia el nombre")
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
# METODO 1 Cambiar el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"
# Imprimir la lista de cantantes para verificar el cambio
print(cantantes)



#metodo 2: Usar update()
#El método update() de los diccionarios permite actualizar múltiples claves al mismo tiempo. Podemos usarlo para actualizar "nombre".

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
# Usar update para cambiar el nombre
cantantes[0].update({"nombre": "Enrique Martin Morales"})
print(cantantes)









# metodo 1 aceder directamente al elemento cancun y asignarle un nuevo valor 
print("\nEJERCICIO 3: En ciudades, cambia “Cancún” por “Monterrey")
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

ciudades["México"][2] = "Monterrey" 
print(ciudades)









# metodo 1 aceder directamente al elemento latitud y cambiar su valor
print("\nEJERCICIO 4: En las coordenadas, cambia el valor de “latitud” por 9.9355431")
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}]
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

















# 2. Iterar a través de una lista de diccionarios


def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}")

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)





def iterarDiccionario(lista):
    for diccionario in lista:
        # Crear una lista de pares 'llave - valor' como cadenas
        output = ", ".join([f"{llave} - {valor}" for llave, valor in diccionario.items()])
        print(output)

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)









def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        # Verificar si la clave está en el diccionario y luego imprimir el valor
        if llave in diccionario:
            print(diccionario[llave])

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamada a la función con la clave "nombre"
iterarDiccionario2("nombre", cantantes)






# 3 Crea la función iterarDiccionario2(llave, lista)


def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        # Verificar si la llave existe en el diccionario y obtener su valor
        if llave in diccionario:
            print(diccionario[llave])
        else:
            print(f"La llave '{llave}' no está presente en el diccionario.")

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamada a la función para obtener los valores asociados a la llave "nombre"
iterarDiccionario2("nombre", cantantes)










def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        # Verificar si la clave está en el diccionario
        if llave in diccionario:
            print(diccionario[llave])

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamada a la función con la clave "pais"
iterarDiccionario2("pais", cantantes)










# 4 Crea la función imprimirInformacion(diccionario)

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        # Imprimir el nombre de la clave y el tamaño de la lista
        print(f"{clave}: {len(lista)} elementos")
        
        # Imprimir los valores de la lista
        for item in lista:
            print(f"  - {item}")

# Ejemplo de uso
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)

