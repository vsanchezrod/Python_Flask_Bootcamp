print("------- LISTAS --------")
# LIST: Objectos que obtienen por posicion
#
miLista = [1, 2, 3]
print("Lista: ", miLista)

# Longitud de la lista
print("Longitud: ", len(miLista))

# Las listas puedes tener distintos tipos de datos
listaVariada = ["hello", "world", 3, 4.5]
print("Lista variada: ", listaVariada)

# Acceder a una posición de la lista
print(listaVariada[2])

# Acceder a varios elementos de la lista (Start:end:step)
listaLetras = ["a", "b", "c", "d", "e", "f"]
print(listaLetras[1:4])

print('\n'*2)
print("------- LISTAS METHODS --------")
print("- APPEND -")
# Agregar un elemento al final de la lista APPEND
listaLetras.append("z")
print("Append: ", listaLetras)

print("- INSERT -")
# Agregar un elemento en una posición de la lista INSERT
# Método insert(index, varibla a insertar
listaLetras.insert(1, "X")
print("Insert: ", listaLetras)

print("- POP -")
# Eliminar un elemento en una posición de la lista POP
# Método pop(index)
listaLetras.pop(1)
print("Pop: ", listaLetras)

# Se puede guardar el elemento se quiere en una variable
popItem = listaLetras.pop(0)
print("popItem: ", popItem)
print("lista: ", listaLetras)

# Si no se especifica un index, se eliminar el último de la lista
popItem2 = listaLetras.pop()
print("popItem2: ", popItem2)
print("lista: ", listaLetras)

print("- MEGA LISTA -")
# Obtener una lista de listas
list1 = [0, 1, 2]
list2 = [3, 4, 5]
list3 = [6, 7, 8]

megaList = [list1, list2, list3]
print("Megalist: ", megaList)
print("Leng Megalist: ", len(megaList))

# Acceder a un elemento de una de las lista de la megaLista
print(megaList[2][1])

# Crear una lista con numeros desde 0 a 11 saltando de 2 en 2
result = list(range(0, 11, 2))
print(result)

# Buscar con IN en una lista un valor
# Ver si hay una letra en un string
print("z" in [1, 2, 3])

# Ver si hay una letra en un string
print(1 in [1, 2, 3])