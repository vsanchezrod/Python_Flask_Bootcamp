# JSON: Formato para intercambiar datos

# Importar módulo json
import json

print("CONVERTIR DICCIONARIO EN JSON")

# Crear diccionario
producto1 = {"nombre": "silla", "color": "blanco", "precio": 40}

# Crear JSON a través de un diccionario => json.dumps()
estructura_json = json.dumps(producto1)
print(estructura_json)
print('\n')

# No se puede acceder a los atriburos de un JSON como si fuera un diccionario
# print(estructura_json["nombre"]) => Da error porque no es un diccionario


print("CONVERTIR JSON A DICCIONARIO")
# Crear DICCIONARIO a través de un JSON => json.loads()
producto2 = json.loads(estructura_json)
print(producto2)
print('\n')

print(producto2['nombre'])
print(producto2['precio'])