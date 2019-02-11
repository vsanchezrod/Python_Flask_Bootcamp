# Se importa la clase User
from user import User

users = [User(1, "Jose", "password1"),
         User(2, "Vir", "password2"),
         User(3, "Marta", "password3")
         ]

# Crear un mapa para acceder de forma rápida a los usuarios

# Por cada usuario en users, se va a coger el username y se va a linkear con el usuario
# Se construye un diccionario basado en el username de cada usuario
username_table = {user.username: user for user in users}
print(username_table)
# De esta forma, se puede acceder al usuario a través del username
print(username_table["Jose"])

# Se construye un diccionario basado en el id de cada usuario
userid_table = {user.id: user for user in users}
print(userid_table)


# AUTENTICACIÓN
def authenticate(username, password):
    # Chequea si el usuario existe y devuelve el usuario. Si no lo encuentra devuelve NONE
    user = username_table.get(username, None)

    if user and password == user.password:
        return user


# POSTMAN PETICIÓN DE AUTENTICACIÓN
# ENDPOINT: http://127.0.0.1:5000/auth
# HEADERS: Content-Type: application/json





# IDENTITY
def identity(payload):
    user_id = payload["identity"]
    return userid_table.get(user_id, None)
