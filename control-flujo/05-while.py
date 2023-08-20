numero = 1

while numero < 100:
    print(numero)
    numero *= 2

comando = ""
# se usa el atributo lower para setear siempre a minuscula aunque el usuario ingrese el texto en mayusculas
while comando.lower() != "salir":
    comando = input("$ ")  # presenta el $ al usuario para ingresar caracteres
    print(comando)
    if comando.lower() == "Salir":
        break
