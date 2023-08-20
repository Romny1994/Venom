print(1 < 2)
print(1 > 2)
print(1 <= 2)  # true
print(2 != 2)
print(2 != "2")  # false


edad = 22
if edad > 54:
    print("Puede ver la pelicula")
elif edad > 17:
    print("No puedes entrar")
else:
    print("No puedes entrar")
print("Listo")


# operadores ternarios

mensaje = "Es mayor" if edad > 22 else "Es menor"

print(mensaje)
