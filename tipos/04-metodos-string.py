animal = "Chanchito feliz"
print(animal.upper())  # convierte todo el texto a mayuscula
print(animal.lower())  # convierte todo el texto a minuscula
print(animal.capitalize())  # cambia a mayuscula la primera palabra
print(animal.title())  # cambia a mayusculas las palabras iniciales
print(animal.lstrip())  # quita los espacios de la izquierda
print(animal.rstrip())  # quita los espacios de la derecha
print(animal.strip())  # quita espacios de una cadena de caracteres
# retorna el lugar en el que se encuentra la cadena que le estamos pasando, -1 es que no encontro nada
print(animal.find("ch"))
print(animal.replace("ch", "j"))  # intercambia cadena de caracteres
# devuelve un valor booleano si encuentra la cadena de caracteres en la variable
print("nch" in animal)
print("nch" not in animal)  # devuelve un valor booleano al evaluar la negativa


animalEspacio = "  Chanchito feliz"
# concatenar metodos, quita espacios y convierte la primera palabra a mayuscula
print(animalEspacio.strip().capitalize())
