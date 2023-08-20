
# definicion de funciones
def hola():
    print("Hello world")
    print("Ultimate Python")
    print("Update Git")


hola()

# se agrega un valor por defecto en algun parametro, en caso de si enviar un valor toma el otro


def hola2(nombre, apellido="Shurman"):
    print(f"Bienvenido : {nombre} {apellido}")


hola2("Nicolas", "Blaz")

# se llama la funcion sin importar el orden de los argumentos, pero definiendo a que corresponde cada uno
hola2(apellido="Shurman", nombre="Nicolas")
