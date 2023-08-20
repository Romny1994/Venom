# las tuplas son listas que no se pueden modificar,agregar o quitar, solo se pueden crear nuevas tuplas en base a existentes

numeros = (0, 1, 2, 3)
numeros = (0, 1, 2, 3) + (4, 5, 6)
print(numeros)

# se convierte una lista a una tupla
punto = tuple([1, 2, 3, 4, 5, 6])
print(punto)


# desempaquetar una tupla
primero, segundo, *otros = punto
print(otros)

# recorre cada valor de la tupla
for n in punto:
    print(n)
