def hello(name="Lolo"):
    print("the hello() func has benn run")

    def greet():
        return "     This is inside the greet()"

    def welcome():
        return "     This is inside welcome()"

    if name == "Lolo":
        return greet
    else:
        return welcome


# Se está devolviendo una función
x = hello()
# x = greet
print(x())

# x = welcome
x = hello("Vir")
print(x())

print('\n' * 2)
print("------------ PASAR UNA FUNCION COOMO PARAMETRO --------------")


def hello2():
    return "Hola!"


def other(func):
    print("Some other code")
    # Lo que recibe se asume que es una función (parametro)
    print(func())


# A la función se le pasa la función saludo
other(hello2)

print('\n' * 2)
print("------------ PASAR UNA FUNCION COOMO PARAMETRO --------------")


def new_decorator(func):
    def wrap_func():
        print("Some code before executing func")
        func()
        print("Code here, after executing func()")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("Please decorate me!!")


func_needs_decorator = new_decorator(func_needs_decorator())
func_needs_decorator()