print("------- DICCIONARIOS --------")
# Son pares de valores {clave: valor}
# DICCIONARIO: Objetos que se obtienen por clave

diccionario = {"key1": "valor1", "key2": "valor2"}
print(diccionario)

print("------- BUSCAR VALOR POR CLAVE --------")
# Buscar el valor de una clave del diccionario
print(diccionario["key1"])
salaries = {"John": 20, "Sally": 30, "Sammy": 15}
print(salaries["Sally"])

print("------- AÑADIR DATOS AL DICCIONAR --------")
salaries["Cindy"] = 100
print(salaries)

print("------- CAMBIAR VALOR PARA UNA CLAVE --------")
salaries["John"] = salaries["John"] + 40
print(salaries["John"])

print("------- KEY CON LISTA COMO VALOR, Y ACCEDER A LOS VALORES --------")
people = {"John": [1, 2, 3], "Sally": [40, 10, 30]}
print(people["John"])
print(people["John"][1])

print("------- KEY CON DICCIONARIO COMO VALOR, Y ACCEDER A LOS VALORES --------")
people2 = {"John": {"salary": 10, "age": 20}}
print(people2["John"]["age"])
print(people2["John"]["salary"])


print("------- DICCIONARIO METHODS --------")
d = {"k1": 10, "k2": 20, "k3": 30}

print("OBTENER LAS KEYS")
print(d.keys())

print("OBTENER LOS VALORES")
print(d.values())

print("OBTENER LOS ITEMS")
print(d.items())