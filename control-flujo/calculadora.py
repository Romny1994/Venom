
print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma,resta,multiplicacion,division")


resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese el primer numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese la operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese el segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print("operacion no valida")
        break
    print("El resultado es :", resultado)
