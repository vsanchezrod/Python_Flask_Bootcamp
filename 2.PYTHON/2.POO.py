print("------------- PERRO---------------")

class Perro():
    # Atributos de clase
    especie = "mamifero"

    # Constructor
    def __init__(self, raza, nombre):
        self.raza = raza
        self.nombre = nombre


# Instancia del objeto
perro1 = Perro("labrador", "Bango")
perro2 = Perro("Caniche", "Lolo")

# Tipo de dato del atributo raza
print(type(perro1.raza))
print(perro1.raza)
print(perro1.nombre)
print(perro1.especie)

print(perro2.raza)
print(perro2.nombre)
print(perro2.especie)

print('\n'*2)
print("------------- CIRCULO---------------")

class Circulo():
    # Atributos
    pi = 3.14

    # Constructor. valor por defecto del radio si no se especifica
    def __init__(self, radio=1):
        self.radio = radio

    # Métodos de clase
    def calcularArea(self):
        return self.radio * self.radio * self.pi

    def calcularCircunferencia(self):
        return 2 * self.pi * self.radio



circulo1 = Circulo(10)
print(circulo1.radio)
print(circulo1.calcularArea())
print(circulo1.calcularCircunferencia())

print('\n'*2)
print("------------- ANIMAL---------------")

class Animal():

    def __init__(self):
        print("Animal created!")

    def report(self):
        print("Animal!")

    def eat(self):
        print("Eating!")


animal = Animal()
animal.eat()
animal.report()
