#FUNCIONES:
#_________



#1

def cantidad_de_vocales():
    return 5
print(cantidad_de_vocales())




# Definimos la función cantidad_de_vocales
def cantidad_de_vocales():
    # La función retorna el valor 5
    return 5

# Llamamos a la función cantidad_de_vocales y el resultado será 5
print(cantidad_de_vocales())  # Esto imprimirá: 5



# Diagrama T:

# | Línea                             | Acción                                     | Detalles                                |
# |-----------------------------------|--------------------------------------------|-----------------------------------------|
# | def cantidad_de_vocales():        | Define la función cantidad_de_vocales      | No se ejecuta aún, solo se define       |

# | return 5                          | Retorna el valor 5                         | 5 es el valor que devuelve esta función |

# | print(cantidad_de_vocales())      | Llama a la función cantidad_de_vocales     | Ejecuta la función y obtiene el valor 5 |
# |                                   | Imprime el valor retornado 5               | La consola muestra: 5                   |

# Resultado en la Consola:
# 5
















#2

"""

def cantidad_de_glaciares_argentina():

    return 16968

print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())

"""


"""El error ocurre porque en el código intentas llamar a una función que no existe: 
cantidad_de_dias_o_meses_o_semanas_en_anio(). Esta función no está definida en ninguna
parte del código, por lo que Python genera un error de tipo NameError diciendo que no
puede encontrar dicha función.

Soluciones posibles
Definir la función faltante: Si deseas sumar el valor de cantidad_de_glaciares_argentina() 
con otro valor, primero debes definir la función cantidad_de_dias_o_meses_o_semanas_en_anio():"""


def cantidad_de_glaciares_argentina():
    return 16968

# Definir la función faltante
def cantidad_de_dias_o_meses_o_semanas_en_anio():
    return 365  # o cualquier valor que necesites

# Ahora esto funcionará sin error
print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())
"""Usar un valor directo en lugar de la función faltante: Si no necesitas una función 
específica para el valor, puedes simplemente escribir un número:"""


def cantidad_de_glaciares_argentina():
    return 16968

# Usar un valor directo en lugar de la función
print(365 + cantidad_de_glaciares_argentina())  # Usando 365 como ejemplo
"""Cualquiera de las soluciones evitará el error, ya que se está proporcionando un valor válido para realizar la operación."""



















#3

def anio_independencia_chile():

    return 1810

    return 1851

print(anio_independencia_chile())



# Definimos la función anio_independencia_chile
def anio_independencia_chile():
    # La función retorna el valor 1810 y termina aquí
    return 1810
    # Esta línea no se ejecuta, ya que la función termina en el primer return
    return 1851

# Llamamos a la función y la imprimimos en consola
print(anio_independencia_chile())  # Esto imprimirá: 1810


# Diagrama T:

# | Línea                              | Acción                                      | Detalles                                           |
# |------------------------------------|---------------------------------------------|----------------------------------------------------|
# | def anio_independencia_chile():    | Define la función anio_independencia_chile  | No se ejecuta aún, solo se define                  |

# | return 1810                        | Retorna el valor 1810 y termina la función  | 1810 es el valor que la función devuelve           |

# | return 1851                        | No se ejecuta                               | Esta línea es ignorada, ya que la función ya terminó|

# | print(anio_independencia_chile())  | Llama a la función anio_independencia_chile | La función se ejecuta y devuelve 1810              |
# |                                    | Imprime el valor retornado 1810             | La consola muestra: 1810                           |

# Resultado en la Consola:
# 1810



















#4

def cantidad_de_departamentos_colombia():

    return(32)

    print(33)  # al poner este print dentro de la funcion no se ejecuta ya que return finaliza la funcion 

print(cantidad_de_departamentos_colombia())



def cantidad_de_departamentos_colombia():

    return(32)

print(33)  # pero si lo dejamos fuera si se ejecuta

print(cantidad_de_departamentos_colombia())



# Diagrama T:

# | Línea                                       | Acción                                          | Detalles                                         |
# |---------------------------------------------|-------------------------------------------------|--------------------------------------------------|
# | def cantidad_de_departamentos_colombia():   | Define la función cantidad_de_departamentos_colombia | No se ejecuta aún, solo se define           |

# | return 32                                   | Retorna el valor 32 y termina la función        | 32 es el valor que la función devuelve           |

# | print(33)                                   | No se ejecuta                                   | Esta línea es ignorada, ya que la función terminó |

# | print(cantidad_de_departamentos_colombia()) | Llama a la función cantidad_de_departamentos_colombia | La función se ejecuta y devuelve 32       |

# |                                              | Imprime el valor retornado 32                  | La consola muestra: 32                           |

# Resultado en la Consola:
# 32




















#5

def altura_machu_picchu():

    print(2438)

x = altura_machu_picchu()




print(x)

# Definimos la función altura_machu_picchu
def altura_machu_picchu():
    # La función imprime el valor 2438
    print(2438)

# Llamamos a la función y asignamos su resultado a la variable x
x = altura_machu_picchu()

# Imprimimos el valor de x
print(x)  # Esto imprimirá: None


# Diagrama T:

# | Línea                      | Acción                                              | Detalles                                        |
# |----------------------------|-----------------------------------------------------|-------------------------------------------------|
# | def altura_machu_picchu(): | Define la función altura_machu_picchu                | La función queda definida, pero no ejecutada    |

# | x = altura_machu_picchu()  | Llama a la función altura_machu_picchu              | Ejecuta la función y asigna su resultado a x    |

# | print(2438)                | Imprime el valor 2438 dentro de la función          | La consola muestra: 2438                        |

# | x                          | x recibe el valor None (la función no retorna nada) | x se asigna a None                              |

# | print(x)                   | Imprime el valor de x                               | La consola muestra: None                        |

# Resultado en la Consola:
# 2438
# None




















#6

def suma(a, b):

    print(a+b)

# print(suma(10, 5) + suma(4, 3))



# Definimos la función suma que toma dos parámetros: a y b
def suma(a, b):
    # La función imprime la suma de a y b, pero no retorna ningún valor
    print(a + b)

# Intentamos imprimir el resultado de suma(10, 5) + suma(4, 3)
#print(suma(10, 5) + suma(4, 3))  # Esto provocará un error de TypeError




# Definimos la función suma que toma dos parámetros: a y b
def suma(a, b):
    # La función ahora devuelve la suma de a y b
    return a + b

# Imprimimos la suma de los resultados de suma(10, 5) y suma(4, 3)
print(suma(10, 5) + suma(4, 3))  # Esto imprimirá: 22


# Diagrama T:

# | Línea                      | Acción                                  | Detalles                                                   |
# |----------------------------|-----------------------------------------|------------------------------------------------------------|
# | def suma(a, b):            | Define la función suma                  | La función queda definida, pero no ejecutada               |

# | suma(10, 5)                | Llama a la función suma con a=10, b=5   | Imprime `15` en la consola, pero no devuelve ningún valor  |

# | suma(4, 3)                 | Llama a la función suma con a=4, b=3    | Imprime `7` en la consola, pero no devuelve ningún valor   |

# | suma(10, 5) + suma(4, 3)   | Intenta sumar los resultados de las dos llamadas | Genera un error, ya que ambas funciones devuelven `None` |

# Error en la Consola:
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'






















#7

def concatenar(a, b):

    return str(b) + str(a)

print(concatenar(7, 15))


# Definimos la función concatenar que toma dos parámetros: a y b
def concatenar(a, b):
    # Convierte b y a a cadenas, y las concatena en el orden b + a
    return str(b) + str(a)

# Llamamos a la función concatenar con a=7 y b=15, e imprimimos el resultado
print(concatenar(7, 15))  # Esto imprimirá: "157"

# Diagrama T:

# | Línea                      | Acción                                      | Detalles                                            |
# |----------------------------|---------------------------------------------|-----------------------------------------------------|
# | def concatenar(a, b):      | Define la función concatenar                | La función queda definida, pero no ejecutada        |

# | concatenar(7, 15)          | Llama a la función con a=7 y b=15           | Ejecuta el cuerpo de la función                     |

# | str(b)                     | Convierte b (15) a cadena "15"              |                                                     |

# | str(a)                     | Convierte a (7) a cadena "7"                |                                                     |

# | str(b) + str(a)            | Concatena "15" y "7", resultando en "157"   |                                                     |

# | return "157"               | Retorna "157"                               | La función devuelve "157"                           |

# | print(concatenar(7, 15))   | Imprime el valor retornado ("157")          | La consola muestra: 157                             |

# Resultado en la Consola:
# 157



















#8

def paises_latinoamerica_o_lenguas_indigenas():  # Definimos una función llamada 'paises_latinoamerica_o_lenguas_indigenas'
    
    a = 560  # Asignamos el valor 560 a la variable 'a'

    print(a)  # Imprimimos el valor de 'a', que es 560

    if a < 180:  # Comprobamos si 'a' es menor que 180
        return 33  # Si 'a' es menor que 180, la función retorna 33 (esto no se ejecutará porque 'a' es 560)

    else:  # Si 'a' no es menor que 180 (en este caso, 560), se ejecuta este bloque
        return 46  # Retornamos el valor 46 porque 'a' no cumple la condición del if

    return 21  # Este 'return' nunca se ejecutará, porque ya hemos retornado un valor en el bloque 'else'
    
# Llamamos a la función y mostramos el valor retornado
print(paises_latinoamerica_o_lenguas_indigenas())  # Esto imprimirá 46, ya que es el valor retornado por la función





















#9

def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):  # Se define una función llamada 'cantidad_de_dias_o_meses_o_semanas_en_anio' que recibe dos parámetros 'a' y 'b'.
    
    if a < b:  # Se verifica si el valor de 'a' es menor que el valor de 'b'.
        return 365  # Si la condición 'a < b' es verdadera, la función retorna 365 (lo que representa un año con 365 días).
    
    else:  # Si la condición 'a < b' es falsa (es decir, si 'a' no es menor que 'b'), se ejecuta este bloque.
        return 12  # La función retorna 12, lo que representa el número de meses en un año.
    
    return 52  # Este 'return' nunca se ejecutará porque la función ya retornó un valor en el bloque 'else'. Es innecesario.

# Llamadas a la función con diferentes valores de 'a' y 'b'

print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))  # Se imprime el valor retornado al llamar la función con 'a=1' y 'b=3'.

print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))  # Se imprime el valor retornado al llamar la función con 'a=7' y 'b=4'.

print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))  # Se imprimen los resultados de sumar las dos llamadas a la función.






















#10

def sumatoria(a, b):  # Se define una función llamada 'sumatoria' que recibe dos parámetros, 'a' y 'b'.
    
    return a + b  # La función retorna la suma de los valores 'a' y 'b'. Este valor se devolverá inmediatamente cuando la función se ejecute.
    
    return 157  # Esta línea de código es innecesaria y nunca se ejecutará, ya que la función ya ha retornado un valor en la línea anterior.

print(sumatoria(3, 4))  # Llamamos a la función 'sumatoria' pasando los valores 3 y 4 como argumentos, e imprimimos el resultado.





















#11

a = 150

print(a)

def funcion():

    a = 350

    print(a)

print(a)

funcion()

print(a)




# Declaramos la variable global a y le asignamos el valor 150
a = 150

# Imprimimos el valor de la variable global a
print(a)  # Esto imprimirá: 150

# Definimos la función funcion
def funcion():
    # Declaramos una variable local a dentro de la función y le asignamos el valor 350
    a = 350
    # Imprimimos el valor de la variable local a dentro de la función
    print(a)  # Esto imprimirá: 350 SOLO CUANDO SE LLAMA A LA FUNCION 

# Imprimimos nuevamente el valor de la variable global a
print(a)  # Esto imprimirá: 150

# Llamamos a la función funcion
funcion()

# Imprimimos nuevamente el valor de la variable global a después de la función
print(a)  # Esto imprimirá: 150



# Diagrama T:

# | Línea              | Acción                                       | Detalles                           |
# |--------------------|----------------------------------------------|------------------------------------|
# | a = 150            | Declara la variable global `a` y asigna 150  | a (global) = 150                   |

# | print(a)           | Imprime el valor de la variable global `a`   | Consola muestra: 150               |

# | def funcion()      | Define la función `funcion`                  | La función queda definida          |

# | print(a)           | Imprime nuevamente el valor de `a`           | Consola muestra: 150               |

# | funcion()          | Llama a la función `funcion`                 | Inicia ejecución de la función     |

# | a = 350 (en funcion)| Declara variable local `a` y asigna 350     | a (local en funcion) = 350         |

# | print(a) (en funcion)| Imprime el valor de `a` dentro de `funcion`| Consola muestra: 350               |

# | print(a)           | Imprime el valor de la variable global `a`   | Consola muestra: 150               |

# Resultado en la Consola:
# 150
# 150
# 350
# 150
















#12
a = 150  # Asignamos el valor 150 a la variable global 'a'

print(a)  # Imprimimos el valor de la variable global 'a', que es 150

def funcion():  # Definimos una función llamada 'funcion' que no recibe parámetros.
    
    a = 350  # Dentro de la función, asignamos el valor 350 a una variable local 'a'.
    
    print(a)  # Imprimimos el valor de la variable local 'a', que es 350 (dentro de la función).
    
    return a  # La función retorna el valor de la variable local 'a', que es 350.

print(a)  # Imprimimos el valor de la variable global 'a' fuera de la función. Sigue siendo 150.

print(a)  # Volvemos a imprimir el valor de la variable global 'a'. Sigue siendo 150.


























#13

a = 150  # Asignamos el valor 150 a la variable global 'a'.

print(a)  # Imprimimos el valor de la variable global 'a'. El valor es 150.

def funcion():  # Definimos una función llamada 'funcion' que no recibe parámetros.
    
    a = 350  # Dentro de la función, asignamos el valor 350 a la variable local 'a'.
    
    print(a)  # Imprimimos el valor de la variable local 'a'. La variable local 'a' tiene el valor 350.

    return a  # La función retorna el valor de la variable local 'a', que es 350.

print(a)  # Imprimimos el valor de la variable global 'a'. Este sigue siendo 150, ya que no ha sido modificada por la función.

a = funcion()  # Llamamos a la función 'funcion', la cual retorna 350. El valor retornado se asigna a la variable global 'a'.

print(a)  # Imprimimos el valor de la variable global 'a'. Ahora, 'a' tiene el valor 350 debido al retorno de la función.























#14

def funcion1():

    print(3)

    funcion2()

    print(2)

def funcion2():

    print(1)

funcion1()



def funcion1():
    print(3)           # Paso 1: Imprime 3
    funcion2()         # Paso 2: Llama a funcion2
    print(2)           # Paso 4: Imprime 2 (después de que funcion2 termine)

def funcion2():
    print(1)           # Paso 3: Imprime 1

# Ejecución del programa:
funcion1()             # Inicia la ejecución llamando a funcion1

# Resultado esperado en consola:
# 3
# 1
# 2























#15

def funcion1():  # Definimos la función 'funcion1', que no toma parámetros.
    
    print(3)  # Imprime el número 3 en la consola.
    
    a = funcion2()  # Llama a la función 'funcion2', y asigna el valor retornado a la variable 'a'.

    print(a)  # Imprime el valor de la variable 'a', que es el valor retornado por 'funcion2'.
    
    return 4  # La función 'funcion1' retorna el valor 4.

def funcion2():  # Definimos la función 'funcion2', que no toma parámetros.
    
    print(1)  # Imprime el número 1 en la consola.
    
    return 0  # La función 'funcion2' retorna el valor 0.

b = funcion1()  # Llama a la función 'funcion1', y asigna el valor retornado por la función a la variable 'b'.

print(b)  # Imprime el valor de la variable 'b', que es el valor retornado por 'funcion1', es decir, 4.
