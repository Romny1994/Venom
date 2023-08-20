# range 5 crea una secuencia de numeros para usar en el for, inicia de 0 a 4
for numero in range(5):
    print(numero, numero * "Hola Mundo")

buscar = 3

for numero in range(5):
    print(numero)
    if numero == 3:
        print("encontrado", buscar)
        break
    else:
        print("No encontre el numero buscado")

# recorre cada letra de la cadena
for char in ("Ultimate Python"):
    print(char)
