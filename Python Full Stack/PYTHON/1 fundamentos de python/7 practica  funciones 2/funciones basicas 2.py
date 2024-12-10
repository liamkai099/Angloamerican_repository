# Archivo: funciones_basicas_2.py

# 1. Función: multiplica_por_2
def multiplica_por_2(num):
    # Crea una lista de números desde 0 hasta `num`, multiplicados por 2
    return [i * 2 for i in range(num + 1)]


# Ejemplo:
print(multiplica_por_2(5))  # Output: [0, 2, 4, 6, 8, 10]


# 2. Función: suma_y_resta
def suma_y_resta(lista):
    if len(lista) != 2:
        print("La lista debe contener exactamente dos números.")
        return None
    
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    print(suma)  # Imprime la suma
    return resta  # Retorna la resta


# Ejemplo:
print(suma_y_resta([5, 4]))  # Output: Imprime 9 y regresa 1


# 3. Función: sumatoria_menos_longitud
def sumatoria_menos_longitud(lista):
    sumatoria = sum(lista)           # Calcula la sumatoria de los números en la lista
    longitud = len(lista)             # Calcula la longitud de la lista
    return sumatoria - longitud       # Retorna la diferencia

# Ejemplo:
print(sumatoria_menos_longitud([1, 2, 3, 4]))  # Output: 6


# 4. Función: valores_multiplicados_segundo
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))             # Imprime la longitud de la lista (que será 1 o menos)
        return []                     # Devuelve una lista vacía
    
    segundo_valor = lista[1]
    nueva_lista = [x * segundo_valor for x in lista]
    print(len(lista))                 # Imprime la longitud de la lista original
    return nueva_lista                # Retorna la lista multiplicada

# Ejemplo:
print(valores_multiplicados_segundo([1, 3, 5, 7]))  # Output: Imprime 4 y devuelve [3, 9, 15, 21]
print(valores_multiplicados_segundo([1]))  # Output: Imprime 1 y devuelve []


# 5. Función: valor_multiplicado_longitud
def valor_multiplicado_longitud(valor, longitud):
    return [valor * longitud] * longitud  # Crea y retorna una lista con `longitud` elementos, todos iguales a `valor * longitud`

# Ejemplo:
print(valor_multiplicado_longitud(5, 2))  # Output: [10, 10]
print(valor_multiplicado_longitud(7, 5))  # Output: [35, 35, 35, 35, 35]
