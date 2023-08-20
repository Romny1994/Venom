numeros = [1, 2, 3, 4, 5, 6, 7]

# ordenar los elementos de una lista
numeros.sort(reverse=True)
print(numeros)

# es una funcion para ordenar iterables
numeros2 = sorted(numeros)
print(numeros2)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)


usuarios = [[4, "chancito"], [1, "gato"], [2, "pepe"]]
usuarios2 = [["chancito", 4], ["gato", 1], ["pepe", 2]]


def ordena(elemento):
    return elemento[1]


# se llama la funcion ordena, para ordenar los elementos de la lista, en este caso no es necesario mandarle parametros a la funcion ya que la funcion sort lo realiza
usuarios2.sort(key=ordena)
print(usuarios2)

# ordenar en reversa
usuarios2.sort(key=ordena, reverse=True)
print(usuarios2)
