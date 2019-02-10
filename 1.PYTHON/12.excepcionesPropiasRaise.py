# EXCEPCIONES PROPIAS - RAISE

def evaluaEdad(edad):
    if edad < 0:
        print("Lala")
        # Lanzamos el tipo de error que queramos con un mensaje personalizado
        # raise MiPropioError("No se permiten edades negativas")

    elif edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate..."


print(evaluaEdad(10))

# Es necesario definir una clase nueva, para lanzar las excepciones personalizadas


# CALCULAR LA RAIZ CUADRADA DE UN NÚMERO

import math


# Calcular la raíz cuadrada : math.sqrt()

def calculaRaiz(numero):
    if numero < 0:
        # Lanzamos un error
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(numero)


op1 = int(input("Introduce un número:"))

try:
    print(calculaRaiz(op1))

# Capturar el mismo tipo de error que se ha lanzado. Se puede poner un alias al error
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)

print("Programa terminado")