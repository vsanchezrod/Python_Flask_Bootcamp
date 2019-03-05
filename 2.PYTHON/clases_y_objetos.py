class Silla():
    color = "blanco"
    precio = 100


silla1 = Silla()
print(silla1.color)
print(silla1.precio)

silla1.color = "roja"
print(silla1.color)

silla2 = Silla()
silla2.color = "verde"
silla2.precio = 120


class Persona():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self):
        print(f" Hola {self.nombre}")


persona = Persona("Jorge", 30)
persona.saluda()
