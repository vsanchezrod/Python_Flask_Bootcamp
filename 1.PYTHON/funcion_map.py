'''
    La función MAP sirve para aplicar una función a cada uno de los elementos de una lista
    El RESULTADO será otra lista con los elementos resultantes de aplicarles la función
'''


# FUNCIÓN
def multiplicar(numero):
    return numero * 2


print(multiplicar(2))

# LISTA DE NÚMEROS
lista_numeros = [2, 4, 6]

# APLICAR FUNCIÓN MAP
'''
    Se utiliza la función map(), que recibe dos parámetros
    :param función a aplicar
    :param lista de elementos
'''
mapeo = map(multiplicar, lista_numeros)
# MAPA
print(mapeo)

# Para poder ver el RESULTADO, CONVERTIMOS el MAPEO en una LISTA
resultado = list(mapeo)
print(resultado)

# ABREVIADO EN UNA LINEA
lista_numeros = list(map(multiplicar, lista_numeros))
print(lista_numeros)


# A VECES NO SE DEFINE LA FUNCIÓN Y SE UTILIZA LA FUNCIÓN LAMBDA
lista_numeros2 = list(map(lambda numero: numero*2, lista_numeros))
print(lista_numeros2)