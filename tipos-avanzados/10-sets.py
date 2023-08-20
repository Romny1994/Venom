# set significa grupo o conjunto de registros no repetidos, si hay registros repetidos los omite al llamar a pantalla, no se pueden acceder a los indices solo filtar en un if
# if 5 in primero
primero = {1, 1, 2, 2, 3, 3, 4, 4}
print(primero)
primero.add(5)
primero.remove(1)
print(primero)

segundo = [3, 4, 5]
# set es un valor iterable
segundo = set(segundo)
print(segundo)

# el caracter | es para unir set, relaizando los filtros de no repetidos
print(primero | segundo)

# el caracter & solo devuelve los valor que se encuentren en ambos set
print(primero & segundo)

# el caracter - solo devuelve los que estan en un set y no en el otro
print(primero - segundo)

# el caracter ^ solo devuelve los valores que no se repiten en ambos set
print(primero ^ segundo)
