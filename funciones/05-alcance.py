
# al estar fuera de las funciones es una variable global, independiente de las funciones
saludo = "Hola Global"


def saludar():
    global saludo  # si se quiere usar una variable global, se debe poner la palabra global antes de la variable
    saludo = "Hola Mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


saludar()
saludaChanchito()
saludar()
print(saludo)
