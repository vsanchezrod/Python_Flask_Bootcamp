print("------------SCOPE----------")
print("------------LEGB RULE----------")
# ORDEN EN EL QUE SE BUSCAN LAS VARIABLES: localmente, enclosing, global o built in


print('\n' * 2)
print("----------LOCAL-----------")


# Valor de la variable local
def report():
    # L (local)
    x = "local"
    print(x)


report()

print('\n' * 2)
print("----------ENCLOSING-----------")
x = "THIS IS GLOBAL LEVEL"


# No hay local, coge la enclosing
def enclosing():
    x = "Enclosing level"

    def inside():
        # E (enclosing)
        print(x)

    inside()


print(x)
enclosing()


# No tiene local, no hay enclosing, coge la global
def enclosing2():
    # x = "Enclosing level"

    def inside():
        # G (Global)
        print(x)

    inside()


print(x)
enclosing2()

print("----------GLOBAL-----------")
x = "outside"


def report():
    # Coge la variable global
    global x
    # Reasigna el valor
    x = 'inside'
    return x


print(report())  # inside
print(x)  # inside

print("----------BUILT IT-----------")

def report(x):

    print(x)
    x = 'inside'
    return x


print(report())  # inside
print(x)  # outside