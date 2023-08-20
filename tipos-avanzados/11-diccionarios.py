# los diccionarios, en las llaves solo acepta strings

punto = {"x": 25, "y": 50}
print(punto)
# se accede mediante un string a la llave que necesitamos el acceso
print(punto["x"])
print(punto["y"])

# agregar llaves al diccionario
punto["z"] = 30

print(punto)

# validar en el diccionario si existe el resultado lala
if "lala" in punto:
    print("encontre lala", punto, punto["lala"])

# validar en el diccionario si existe el resultado lala en el caso de que no existe devuelve el valor none
print(punto.get("lala"))

# eliminar una llave del diccionario
del punto["y"]
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

# al recorrer con items devuelve unas tuplas
for valor in punto.items():
    print(valor)


# al recorrer con items y agregando dos valores de llave y valor se agregan los dos valores del diccionario en cada variable
for llave, valor in punto.items():
    print(llave, valor)

# pasar un diccionario en una lista
usuarios = [{"id": 1, "nombre": "chanchito"},
            {"id": 2, "nombre": "feliz"},
            {"id": 3, "nombre": "pelusa"},
            {"id": 4, "nombre": "calvo"}]

for usuario in usuarios:
    print(usuario["nombre"])
