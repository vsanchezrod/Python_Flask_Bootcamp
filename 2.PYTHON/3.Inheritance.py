print("------------- ANIMAL---------------")


class Animal():

    def __init__(self):
        print("Animal created!")

    def report(self):
        print("Animal!")

    def eat(self):
        print("Eating!")


print('\n' * 2)
print("------------- PERRO CON HERENCIA---------------")


# A la clase Perro se le pasa Animal para decirle que hereda de esa clase
class Dog(Animal):

    def __init__(self):
        # Se ejecuta el constructor de la clase padre
        Animal.__init__(self)
        print("Dog created!")

    # Sobreescribir un método de la clase padre
    def report(self):
        print("I am a dog")


# Se crea una instancia de perro
perro = Dog()

# La instancia de perro hereda los atributos y métodos de la clase padre
perro.eat()
perro.report()


print('\n' * 2)
print("------------- ANIMAL2 ATRIBUTO EN EL CONSTRUCTOR---------------")
# Si la clase padre tiene un constructor con parámetros

class Animal2():

    def __init__(self, fur):
        self.fur = fur

    def report(self):
        print("Animal!")

    def eat(self):
        print("Eating!")


print('\n' * 2)
print("------------- PERRO2 CON HERENCIA---------------")


# A la clase Perro se le pasa Animal para decirle que hereda de esa clase
class Dog2(Animal2):

    # El constructor de la clase hija recibe el parámetro que necesita el padre
    def __init__(self, fur):
        # Se ejecuta el constructor de la clase padre con el paráemtro
        Animal2.__init__(self, fur)
        print("Dog created!")

    # Sobreescribir un método de la clase padre
    def report(self):
        print("I am a dog")


# Se crea una instancia de perro con el atributo requerido
perro2 = Dog2("Fuzzy")

# La instancia de perro hereda los atributos y métodos de la clase padre
perro2.eat()
perro2.report()
print(perro2.fur)
