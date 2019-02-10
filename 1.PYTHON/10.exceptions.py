def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Captura excepción dividir por 0
    try:
        return num1 / num2

    except ZeroDivisionError:
        print("No se puede dividor entre 0")
        return "Operación errónea"


# Captura excepción introducir valores incorrectos

while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))

        op2 = (int(input("Introduce el segundo número: ")))

        break

    except ValueError:
        print("Los valores introducidos no son correctos. Inténtalo de nuevo")

operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecúción del programa ")




