'''
    La función FILTER es una función para filtrar resultados a partir de una lista y de una función condicional
    El RESULTADO será otra lista con los elementos que cumplen la condición.
'''


# FUNCIÓN CONDICIONAL
def es_positivo(numero):
    if numero > 0:
        return True
    else:
        return False


print(es_positivo(5))
print(es_positivo(-3))

# LISTA DE NÚMEROS
lista_numeros = [4, -2, 8, -3, -5, -7, 1, 9]


# CREAR UN FILTRO
'''
    Se crea un filtro con filter(), que recibe dos parámetros
    :param función condicional
    :param lista de numeros
'''
filtro = filter(es_positivo, lista_numeros)
# FILTER
print(filtro)

# Para poder ver el RESULTADO, CONVERTIMOS el FILTRO en una LISTA
resultado = list(filtro)
print(resultado)

# ABREVIADO EN UNA LINEA
lista_numeros = list(filter(es_positivo, lista_numeros))
print(lista_numeros)