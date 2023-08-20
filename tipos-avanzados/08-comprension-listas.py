animales = [["chancito", 1], ["calvo", 2], ["Val", 3], ["Pelusa", 4]]

nombres = []
for animal in animales:
    nombres.append(animal[0])
print(nombres)

# nombres = [expresion for item in items], esta es una version reducida del for en arreglos
# se utiliza el indice 0, ya que en el caso ["chancito",1]=> el parametro chanchito es el indice 0 y el 1 corresponde al indice 1 por posiciones, a este metodo es map
nombres = [animal[0] for animal in animales]
print(nombres)

# se filtra que los resultado que se guarda en el arreglo de animal sea mayor a 2, esto para el indice 1, a este metodo se le llama filter
nombres = [animal for animal in animales if animal[1] > 2]
print(nombres)

# listado utilizando la funcion de map
nombres = list(map(lambda animal: animal[0], animales))
print(nombres)

# listado utilizando las listas de comprension filter
menosAnimales = list(filter(lambda animal: animal[1] > 2, animales))
print(menosAnimales)
