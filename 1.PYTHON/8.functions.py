print("------- DEFINICION DE FUNCIONES --------")


def suma(num1, num2):
    print(num1 + num2)


suma(3, 5)


def report_person(name):
    print("Reporting person: " + name)

report_person("John")

# n parámetros
def report_person_con_n_parametros(*names):

    for name in names:
        print("Reporting person: " + name)


report_person_con_n_parametros("John", "Virginia", "Pedro")

# Se puede definir una valor por defecto para el parámetro por si no lo recibe
def report_person2(name="Sin Nombre"):
    print("Reporting person: " + name)


# ERROR => report_person()
report_person2()

print("------- FUNCTIONS  --------")
print('\n' * 2)
print("------- MAX y MIN --------")
print(max(2, 3))
print(max([12, 3, 100, 212]))

print(min(1, 9))
print(min([12, 3, 100, 212]))

print('\n' * 2)
print("------- SUM --------")
print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print('\n' * 2)
print("------- ABS --------")
print(abs(10-20))


print('\n' * 2)
print("------- ENUMERATE --------")
myList = ["a", "b", "c"]
index = 0

for letter in myList:
    print(letter)
    print('is at index: {}'.format(index))
    index = index + 1
    print('')

# Se puede hacer lo mismo pero con enumerate y devuelve pares de valores.
for item in enumerate(myList):
    print(item)

# Se puede desempaquetar los pares de valores (ver en 5.tuples)
for index, item in enumerate(myList):
    print(item)
    print(index)
    print('{} is at index: {}'.format(item, index))
    print('')

print('\n' * 2)
print("------- JOIN --------")
# Une los elementos de la lista
lista = ["a", "b", "c", "d"]
print("".join(lista))
# Se le puede pasar una cadena para que la use para unir los elementos
print("--".join(lista))

print('\n' * 2)
print("------- EJERCICIOS --------")
print("------- PROBLEMA 1 --------")


# Funciónj que devuelva un boleano indicando si "secret" está en un string

def secret_check(cadena):
    if "secret" in cadena:
        return True
    else:
        return False


# Mejor versión
def secret_check2(cadena):
    return "secret" in cadena.lower()


print(secret_check("simple"))
print(secret_check("secret is a secret"))
print(secret_check("SECRET"))
print(secret_check2("simple"))
print(secret_check2("secret"))
print(secret_check2("SECRET"))

print("------- PROBLEMA 2 --------")


# Funcion que coge un string y cambia las vocales por una x
def cambiarVocales(cadena):
    # Crear una lista con el string
    listaLetras = list(cadena)
    print(listaLetras)

    for index, letra in enumerate(cadena):
        for vocal in "aeiou":
            if letra.lower() == vocal:
                # Si la letra es una vocal, cambia el item de la lista por una x
                listaLetras[index] = "x"

    print("".join(listaLetras))


print(cambiarVocales("sammy"))
