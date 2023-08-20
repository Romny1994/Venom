mascotas = ["wolfgang", "pelusa", "copito", "pulga"]
print(mascotas[0])

mascotas[0] = "Bicho"
print(mascotas)
print(mascotas[0:3])  # toma desde el valor 0 en el arreglo hasta el 3
# en caso de poner valores negativos inicia del final de la lista
print(mascotas[-1])
# al poner doble :: toma el primer valor luego salta el siguiente hasta el numero que le indicamos
print(mascotas[::3])

# muestra los numeros impares, ya que incia desde el valor 1 y se salta 2 que es el valor que le estamos indicando
numeros = list(range(21))
print(numeros[1::2])


# realizamos los mismo pero en el rango al iniciar con 1 no es necesario agregar 2 partametros en el print
numeros = list(range(1, 21))
print(numeros[::2])
