# Cuando en el código hay una llamada a una función Generador.
# Se devuelven los valores de uno a uno dentro de un objeto iterable


# sintaxis
#
# def generarNumeros():
#     yield numeros

# EJEMPLO - Sin generador

# Crear un programa que genere una lista de números pares

def generarNumeros(limite):
    num = 1
    listaPares = []

    while num < limite:
        listaPares.append(num * 2)
        num += 1

    return listaPares


print(generarNumeros(10))


# EJEMPLO - Con generador

# Crear un programa que genere una lista de números pares

def generarNumerosPar(cantidadNumeros):
    num = 1

    while num <= cantidadNumeros:
        # Construye un objeto iterable con los valores de la lista en su interior
        # Los va almacenando de uno en uno
        yield num * 2
        num += 1

def kk():
    num = 1
    while True:
        yield num * 2
        num += 1




# Crear un objeto donde almacenamos el objeto iterable que devuelve la función
devuelvePares = generarNumerosPar(10)
# Si solo queremos los 3 primeros elementos
# Con el método next conseguimos que solo nos devuelva el primer valor que tiene almacenado en su interior el objeto generador

print(next(devuelvePares))
print("Después del primer valor del generador")
print(next(devuelvePares))
print("Después del segundo valor del generador")
print(next(devuelvePares))
print("Después del tercer valor del generador")
