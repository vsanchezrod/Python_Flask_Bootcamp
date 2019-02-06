print("------- STRINGS --------")
# STRINGS
cadena = "Hello world"
print("cadena: ", cadena)
print(type(cadena))

# Acceder a un caracter
letra = cadena[0]
print("letra: ", letra)

# Se puede acceder también por el final
letra2 = cadena[-1]
print("letra2: ", letra2)

# LONGITUD de la candena LENGTH
print("Longitud: ", len(cadena))

# Cortar una cadena - Slice [start:end:step]
# La posición del start está incluída y la de end no
cadenaTexto = "abcdefghijk"

# Ejemplo con start:end
cadenaNueva = cadenaTexto[0:3]
print("cadenaTexto: ", cadenaNueva)

# Ejemplo con start:end:step
# Va desde el start hasta el end, saltando de dos en dos los caracteres
cadenaNueva2 = cadenaTexto[0:7:2]
print("cadenaTexto2: ", cadenaNueva2)

# Ejemplo desde el inicio hasta el 3 (no incluido)
cadenaNueva3 = cadenaTexto[:3]
print("cadenaTexto3: ", cadenaNueva3)

# Ejemplo desde el 3 hasta el final
cadenaNueva4 = cadenaTexto[3:]
print("cadenaTexto4: ", cadenaNueva4)

# Ejemplo desde el inicio hasta el end, saltando de dos en dos los caracteres
cadenaNueva5 = cadenaTexto[::2]
print("cadenaTexto5: ", cadenaNueva5)

# Obtener la cadena al revés
cadenaNueva6 = cadenaTexto[::-1]
print("cadenaTexto6: ", cadenaNueva6)

print('\n'*2)
print("------- STRINGS METHODS --------")
# No se puede asignar a un caracter de una cadena otro caracter
cadenaTexto2 = "Hello World"

# Concatenar strings
print(cadenaTexto2 + cadenaTexto2)

# Pasar a mayúsculas
print(cadenaTexto2.upper())

# Pasar a minúsculas
print(cadenaTexto2.lower())

# Partir una cadena en una lista SPLIT (Se incluye el caracter que cortará la cadena). Si no se pone nada es un espacio
print(cadenaTexto2.split())
print(cadenaTexto2.split('o'))


print('\n'*2)
print("------- SUSTITUIR VARIABLES EN STRINGS --------")
username = "Vir"
color = "red"
print("The username favorite is color")

# Reemplazar con variables mediante tres métodos
# 1. format()
print("The {} favorite is {}".format(username, color))

# 2. %s(strings), %d(decimals)
print("The %s favorite is %s" % (username, color))

# 3. f" - f string literals!!
print(f"The {username} chose {color}")


# Ver si hay una letra en un string
print("s" in "asdasdscfaksjlsxxsxasfda")