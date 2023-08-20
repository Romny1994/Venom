mascotas = ["pelusa", "mascotas", "perros", "gatos"]

# generar una tupla estos son los que se muestran entre(), para que se muestre un listado

for mascota in enumerate(mascotas):
    print(mascota)


mascotas_busqueda = ["pelusa", "mascotas", "perros", "gatos", "pelusa"]

print(mascotas.count("pelusa"))

# se valida si existe el registo en la lista asi no da error el codigo
if "pelusa" in mascotas:
    print(mascotas_busqueda.index("pelusa"))
