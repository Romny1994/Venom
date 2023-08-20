lista1 = [1, 2, 3, 4, 5]
print(lista1)

# al agregar el * se quitan los []
print(*lista1)

lista2 = [5, 6, 7, 8]

combinada = ["hola", *lista1, "mundo", * lista2]
print(combinada)

# desempaquetar diccionarios con los operadores **, para luego combinarlos en un nuevo diccionario
punto1 = {"x": 12, "y": 23}
punto2 = {"Y": 25}
nuevoPunto = {**punto1, **punto2, "z": "mundo"}
print(nuevoPunto)
