# 1. Imprime "Hola, mundo"

print("Hola, mundo" )

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Valeria"

print("Hola mundo",nombre) # con una coma

print("Hola mundo"+nombre) # con un + 
print("Hola mundo "+nombre) # con un + aqui solo con un espacio dentro de las comas podemos separar un espacio en consola


# 3. Imprimir "Hola 156!" con el número en una variable

numero = 156

print("hola",numero,"!") # concatenamos con una coma

# Imprimir "Hola 156!" sin espacio adicional
# aqui con sep='' quitamos los espacios entre los elementos y con un espacio dentro
# de 'Hola ' logramos un espacio por consola
print('Hola ', numero, '!', sep='') 

# Imprimir "Hola 156!" incluyendo las comillas
print('"Hola', numero, '!"')

# con un + -- este debería arrojar un error!, corrígelo con conversión 
# print("hola "+(numero)+"!") da un error
"""El error ocurre porque en la expresión ("hola " + (numero) + "!") estás intentando concatenar
una cadena ("hola ") con un número (numero). En Python, no puedes concatenar directamente 
cadenas y números usando el operador + sin convertir el número a una cadena primero.
con str() convertimos el valor numerico a un valor Strings(o cadena) para corregir el error"""

print("hola "+ str(numero)+"!") 
print("hola "+ str(numero)+" !") # recuerda que con un espacio dentro de las comas obtenemos un espacio en consola



# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "tacos"
comida2 = "arepas"

# Con .format()
#el método .format() inserta los valores de comida1 y comida2 en los lugares {} dentro de la cadena de texto
print("Me encanta comer {} y {}".format(comida1, comida2))

# Con una cadena f
# la f-string permite insertar directamente las variables dentro de la cadena usando {}
print(f"Me encanta comer {comida1} y {comida2}")