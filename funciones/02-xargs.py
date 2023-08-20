
# al definir las funciones asi, se pueden enviar multiples argumentos, se convierte en una funcion iterable
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(9, 3, 12)
