print("------- TUPLES --------")
# Son como listas, pero con paréntisis y que un elemento dentro de una tupla NO puede ser reasignado
tuple = (1, 2, 3)
print(tuple)
lista = [1, 2, 3]
print(lista)
lista[0] = "NEW"
print(lista)
# tuple[0] = "NEW" ==> ERROR

# Accceder a un valor de la tupla
print(tuple[0])
print('\n'*2)


print("------- SETS --------")
# Elementos únicos. Es similar a un diccionar pero si pares de clave, valor
x = set()
print(x)
print("AÑADIR ELEMENTO AL SET")
x.add(1)
x.add(2)
x.add(3)
x.add(3) # => NO se añade porque ya está representado en el SET
print(x)

print("PASAR UNA LISTA A SET")
lista = [1, 1, 3, 5, 5, 1, 6, 7, 10, 9, 9]
print(set(lista))
print('\n'*2)


print("------- BOOLENAS --------")
# True or False
a = True
b = False
# Special Keyword
c = None
print(a)
print(1 > 2)