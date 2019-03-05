'''
    LAMBDA son funciones pequeñas y anónimas

    Ejemplo: función lambda que recibe un parámetro y que devuelve ese parámetro sumando 30

'''

# Un parámetro
resultado = lambda numero: numero + 30
print(resultado(10))


# Varios parámetros
resultado2 = lambda numero1, numero2: numero1 + numero2
print(resultado2(10, 32))


