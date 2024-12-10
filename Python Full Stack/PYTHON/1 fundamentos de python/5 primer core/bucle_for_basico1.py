
# PRIMER CORE PYTHON:
#_____________________




# Ejercicio 1: Básico
# Imprime todos los números enteros del 0 al 100.
print("Ejercicio 1: Básico")
for i in range(101):
    print(i)





# Ejercicio 2: Múltiples de 2
# Imprime todos los números múltiplos de 2 entre 2 y 500.
print("\nEjercicio 2: Múltiples de 2")
for i in range(2, 501, 2):   # utilizamos un rango con tres argumentos
    print(i)





# Ejercicio 3: Contando Vanilla Ice
# Imprime los números del 1 al 100. Si es divisible por 5 imprime “ice ice”, y si es divisible por 10, imprime “baby”.
print("\nEjercicio 3: Contando Vanilla Ice")
for i in range(1, 101):  # utilizamos un rango con dos argumrntos
    if i % 10 == 0:    # Si el número i es divisible entre 10 (i % 10 == 0), imprime "baby".
        print("baby")  
    elif i % 5 == 0:     # Si el número i no es divisible entre 10 pero sí entre 5 (i % 5 == 0), imprime "ice ice".
        print("ice ice")
    else:                #Si el número i no cumple ninguna de las condiciones anteriores, simplemente imprime el número i.
        print(i)






# Ejercicio 4: Wow. Número gigante a la vista
# Suma los números pares del 0 al 500,000 e imprime la suma total.
print("\nEjercicio 4: Wow. Número gigante a la vista")
suma_total = sum(i for i in range(0, 500001, 2))
print(suma_total)


# sum(...):

"""sum es una función que suma todos los elementos de una secuencia o generador.
sum(i for i in range(0, 500001, 2)) utiliza una comprensión de generador
(i for i in range(0, 500001, 2)) que produce cada número par de 0 a 500,000 y 
los pasa a la función sum, que calcula la suma total."""





# Ejercicio 5: Regrésame al 3
# Imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
print("\nEjercicio 5: Regrésame al 3")
for i in range(2024, 0, -3):  # utilizamos un range de tres argumentos para iniciar un bucle for que imprime los numeros de forma regresiva del 2024 al 2
    print(i)






# Ejercicio 6: Contador dinámico
# Imprime los números entre numInicial y numFinal que sean múltiplos de multiplo.
numInicial = 3
numFinal = 10
multiplo = 2
print("\nEjercicio 6: Contador dinámico")
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
