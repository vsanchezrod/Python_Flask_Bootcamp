# Se importa módulo para las expresiones regulares
import re

# EXPRESIONES REGULARES (search, findall, split, sub)

'''
    EXP REGULAR: son secuencias de caracteres que forman una búsqueda por patrón
    Se utilizan para ver si una cadena de texto cumple con un patrón
'''

texto = "Hola, mi nombre es Virginia"

print('MÉTODO SEARCH() => PARA BUSCAR UN PATRÓN DENTRO DE UN TEXTO')
print('\n')
'''
    Método search() del módulo re: busca un patrón en una cadena de texto
    :param patrón
    :param cadena de texto
    Resultado: 
    - Si lo encuentra, devuelve un objeto de tipo Match, diciendo que lo ha encontrado
    - Si no lo encuentra, no devuelve nada (None)
'''
resultado = re.search("nombre", texto)
print(resultado)

if (resultado):
    print('Cadena encontrada')
else:
    print('Cadena no encontrada')
print('\n')

resultado2 = re.search("sdadadasdasdasda", texto)
print(resultado2)

if (resultado2):
    print('Cadena encontrada')
else:
    print('Cadena no encontrada')
print('\n')

# USO DE $ => Busca en el final el patrón
print('USO DE $ en el patrón')

# Buscar en la cadena de texto si hay alguna frase que acaba en Virginia
resultado3 = re.search("Virginia$", texto)
print(resultado3)
print('\n')

# USO DE ^ => Busca por en el inicio el patrón
print('USO DE ^ en el patrón')

# Buscar en la cadena de texto si hay alguna frase empieza por Hola
resultado4 = re.search("^Hola", texto)
print(resultado4)
print('\n')

# USO DE . y * => Busca por en el inicio el patrón
print('USO DE . y * en el patrón')
'''
    . => Cualquier caracter
    * => N veces
'''

# Buscar en la cadena de texto si contiene "mi" y despúes "es" independientemente de lo que haya en el medio
resultado5 = re.search("mi.*es", texto)
print(resultado5)
print('\n')

# USO DE FINDALL => Busca todas las ocurrencias en una cada
print('USO DE FINDALL')
print('MÉTODO FINDALL() => PARA BUSCAR TODAS LAS OCURRENCIAS')
print('\n')
'''
    Método findall() del módulo re: busca todas las ocurrencias de un patrón en una cadena de texto
    :param patrón
    :param cadena de texto
    Resultado: 
    - Devuelve una lista con todas las ocurrencias encontradas
'''

texto2 = """
    El coche de Luis es rojo,
    el coche de Antonio es blanco
    y el coche de Vir es rojo
"""

# Buscar en la cadena de texto si contiene "coche" y que acabe en "rojo", independientemente de que haya en medio
resultado5 = re.findall("coche.*rojo", texto2)
print(resultado5)
print('\n')

print('MÉTODO SPLIT() => DIVIDE UNA CADENA A PARTIR DE UN PATRÓN')
print('\n')
'''
    Método split() del módulo re: divide una cadena a partir de un patrón
    :param patrón
    :param cadena de texto
    Resultado: 
    - Devuelve una lista con los elementos divididos de la cadena de texto
'''

texto3 = "La silla es blanca y vale 80"

# Divide la cadena de texto usando el patrón. En este caso se usa "\s" que es un espacio en blanco
resultado6 = re.split("\s", texto3)
print(resultado6)
print('\n')


print('MÉTODO SUB() => SUSTITUTE LAS OCURRENCIAS ENCONTRADAS USANDO UN PATRÓN POR OTRO ELEMENTO')
print('\n')
'''
    Método sub() del módulo re:  Sustituye todas las coincidencias de un patrón por otra cosa en la cadena
    :param patrón
    :param por el valor que se sustituyen las ocurrencias
    :param cadena de texto
    Resultado: 
    - Sustituye por el nuevo elemento si encuentra el patrón, o no sustituye nada si no lo encuentra.
'''

texto3 = "La silla es blanca y vale 80"

# Subtituye las ocurrencias encontradas usando un patrón por otro elemento
resultado7 = re.sub("blanca", "roja", texto3)
print(resultado7)
print('\n')

resultado8 = re.sub("blaasdasdnca", "roja", texto3)
print(resultado8)
print('\n')