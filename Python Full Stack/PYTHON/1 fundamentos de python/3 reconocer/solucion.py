# declaración de variable
numero1 = 70  # Numerales
numero2 = 3.14  # decimal
booleano = False  # Boolean
cadena = 'Hola Mundo'  # Strings (Cadenas)

# Listas 
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate']

# Diccionarios 
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False}

# Tuplas 
frutas = ('guayaba', 'fresa', 'papaya')

# revisión de tipo
print(type(frutas))

# Listas - accesar valor
print(ingredientes_pastel[2])

# Listas - agregar valor
ingredientes_pastel.append('Mantequilla')

# Diccionarios - accesar valor
print(persona['nombre'])

# Diccionarios - cambiar valor
persona['nombre'] = 'Kevin'

# Diccionarios - agregar valor
persona['color_ojos'] = 'cafe'

# Tuplas - accesar valor
print(frutas[2])

# condicional - if
if numero1 > 45:
    print("Numero mayor")

# condicional - else
else:
    print("Numero menor")

# revisión de tamaño
if len(cadena) < 5:
    print("Cadena corta")

# condicional - else if
elif len(cadena) > 15:
    print("Cadena larga")

# condicional - else
else:
    print("Cadena perfecta")

# bucle for - inicio
for x in range(8):
    print(x)
# bucle for - inicio con rango específico
for x in range(2,8):
    print(x)

# bucle for - inicio con rango e incremento
for x in range(2,8,2):
    print(x)

# bucle while - inicio
x = 0
while(x < 8):
    print(x)

    # bucle while - incremento
    x += 1

# Listas - borrar valor (último elemento)
ingredientes_pastel.pop()

# Listas - borrar valor (elemento específico)
ingredientes_pastel.pop(1)

# Diccionarios - mostrar diccionario completo
print(persona)

# Diccionarios - borrar valor
persona.pop('color_ojos')

# bucle for - inicio
for ingrediente in ingredientes_pastel:
    # bucle for - continue
    if ingrediente == 'Harina':
        continue

    print('Después de la primera sentencia')

    # bucle for - break
    if ingrediente == 'Chocolate':
        break

# función - declaración
def imprime_hola_10_veces():
    # bucle for - inicio
    for numero in range(10):
        print('Hola')

# función - llamada
imprime_hola_10_veces()

# función - declaración con parámetro
def imprime_hola_n_veces(n):
    # bucle for - inicio
    for numero in range(n):
        print('Hola')

# función - llamada con argumento
imprime_hola_n_veces(5)

# función - declaración con parámetro y valor predeterminado
def imprime_hola_n_o_diez_veces(n = 10):
    # bucle for - inicio
    for numero in range(n):
        print('Hola')

# función - llamada sin argumento (usa el valor predeterminado)
imprime_hola_n_o_diez_veces()

# función - llamada con argumento
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# imprime el valor de la variable numero3
print(numero3)

# se define la variable numero3 y se le asigna el valor 86
numero3 = 86

#se modifica el primer elemento (índice 0) de la lista llamada frutas
frutas[0] = 'naranja'

#  accede a un diccionario llamado persona  y luego imprime el valor asociado con la clave 'hobbies'.
print(persona['hobbies'])

# accede a la posición 11 de una lista llamada ingredientes_pastel y luego imprimir el valor en esa posición
print(ingredientes_pastel[11])

# imprime el valor de una variable llamada booleano
print(booleano)

# la función append() se utiliza para agregar el valor 'manzana'
frutas.append('manzana')

#  La función pop() elimina el elemento en el índice especificado de la lista
frutas.pop(1)