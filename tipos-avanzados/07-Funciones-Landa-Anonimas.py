

usuarios = [["chanchito", 1], ["pelusa", 3], ["Calvo", 4], ["cal", 6]]


def ordena(elemento):
    return elemento[1]


# esta funcion lambda es una version corta de la funcion elemento
usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
print(usuarios)
