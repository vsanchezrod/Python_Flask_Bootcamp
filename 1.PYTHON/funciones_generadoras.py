range

"""
    Una función generadora genera valores sobre la marcha, cada vez que le pedimos uno nos da un valor
    Ej: Un ejemplo de función generadora es la función range
"""

# Genera valores desde 0 a 10 (range(0,11)o range(11) es lo mismo
range(0, 11)
range(11)

for numero in range(0, 11):
    print(numero)

"""
    Se crea una función GENERADORA DE PARES.
    Cada vez que llamemos a la función nos va a dar el siguiente par
"""


def pares(maximo):
    for numero in range(maximo):
        if (numero % 2 == 0):
            yield numero


maximo = 11

for numero in pares(maximo):
    print(numero)

devuelvePares = pares(20)

# Cada vez que llamemos a la función generadora pares, nos va a dar el siguiente valor par
print(next(devuelvePares))
print("Después del primer valor del generador")
print(next(devuelvePares))
print("Después del segundo valor del generador")
print(next(devuelvePares))
print("Después del tercer valor del generador")