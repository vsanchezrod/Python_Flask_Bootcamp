print("------- LOOPS --------")

print("------- IF  ELSE --------")
username = "Admin"
check = "Admin"
permission = True

if username == check:
    print("Access granted!")
else:
    print("Denied!")

print("------- IF ELIF ELSE --------")
username = "Admin"
check = "Admin"

if 1 == 2:
    print("1 Condicion!")
elif 1 == 3:
    print("2 Condicion")
elif 1 == 4:
    print("condicion")
else:
    print("Denied!")

if username == "admin" and permission:
    print("full access")
elif username == "admin" and permission == False:
    print("Admin access only, no full permission")
else:
    print("No access!")

print('\n' * 2)
print("------- FOR --------")
seq = [1, 2, 3, 4, 5, 6]

for item in seq:
    print(item)

# Igual para recorrer caracteres
mystring = "hello"
for char in mystring:
    print(char)

# En un diccionarop - Recorre las claves
salaries = {"John": 20, "Sally": 30, "Sammy": 15}
for key in salaries:
    print(key)

for key in salaries:
    print("Empleado: ", key)
    print(salaries[key])
    print('')

# A menudo las funciones devuelven pares de datos
mypairs = [("a", 1), ("b", 2), ("c", 3)]
print(len(mypairs))

# Se pueden recorrer separando los pares de valores - TUPLE UNPACKING
for item1, item2 in mypairs:
    print("Item1: ", item1)
    print("Item2: ", item2)

print('\n' * 2)
print("------- WHILE --------")

# i = 10
# while 1 < 5:
#     i = i + 1
#     print(f"i es: {i}")

# Bucle for con RANGO desde 0 hasta 5
for x in range(0, 5):
    print(x)

# Bucle for con RANGO desde 0 hasta 5, saltando de 2 en 2
for x in range(0, 5, 2):
    print(x)

# Crear una lista con un rango# Crear una lista con un rango
# result = list(range(0, 11, 2))
# print(result)
result = list(range(0, 11, 2))
print(result)

# Ver si hay una letra en un string
print("s" in "asdasdscfaksjlsxxsxasfda")

# Ver si hay una letra en un string
print("z" in [1, 2, 3])

# Ver si hay una letra en un string
print(1 in [1, 2, 3])