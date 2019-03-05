def saludar():
    print("Hola que tal!!")


saludar()


def saludar2(nombre):
    print(f"Buenos días {nombre}")


saludar2("Vir")


def suma(numero1, numero2):
    suma = numero1 + numero2
    print(f"La suma es {suma}")
    return suma


resultado = suma(35, 20)
print(resultado)

colores = ['rojo', 'verde', 'azul']


def incluir_color(color):
    colores.append(color)


incluir_color('amarillo')
print(colores)
