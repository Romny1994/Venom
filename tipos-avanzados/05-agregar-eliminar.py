mascotas = ["Pelusa", "Mascotas", "perros", "gatos"]

# insertar datos a las listas existentes
mascotas.insert(1, "pato")
# insertar datos a las listas existentes en el ultimo registro
mascotas.append("Chanchito")

print(mascotas)

# elimina el registro indicado, en caso de estar mas de un regitro solo elimina el primero
mascotas.remove("pato")
print(mascotas)

# elimina el registro que indiquemos en caso de estar mas de uno
mascotas.pop(1)
print(mascotas)

# elimar un regitro indicando el indice
del mascotas[0]
