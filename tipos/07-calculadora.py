# input es para obtener un valor por parte del usuario en pantalla
n1 = input("Ingresa el primer numero")
n2 = input("Ingresa el segundo numero")

n1 = int(n1)  # Se castea a int para poder realizar las operaciones
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""Para los numeros{n1} y {n2},
          el resultado de la suma es {suma},
          el resultado de la resta es {resta},
          el resultado de la multiplicacion es {multiplicacion},
          el resultado de la division es {division}"""


print(mensaje)
