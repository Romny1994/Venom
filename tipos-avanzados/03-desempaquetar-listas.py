numeros = [1, 2, 3]

# al agregar el * se agregan los demas valores a excepcion del primero que si esta definido
primero, *otros = numeros

print(primero)

mas_numeros = [1, 2, 3, 4, 5, 6, 7]

primero, segundo, *otros, penultimo, ultimo = mas_numeros
print(primero, segundo, penultimo, ultimo, otros)
