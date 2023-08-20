# se agrega un modulo para trabajar con mas funciones de numeros
import math

numero = 2  # entero -> integer
decimal = 1.2  # float
imaginario = 2 + 2j  # 2 +2i, es decir la suma de 2 + 2 entre la raiz cuadrada de -1, j equivale a -1 es decir un numero imaginario
numero = numero + 2  # se le suma 2 a la variable de numero
numero += 2  # se le suma 2 a la variable de numero en version reducida
numero *= 2
numero -= 2


print(1+3)
print(1-3)
print(1*3)
print(1/3)
print(1//3)  # al usar doble // no se muestran decimales
print(1 % 3)  # se obtiene el sobrante de la division
print(2**3)  # es decir se eleva 2 a la 3


# devuelve el numero al que se devuelve mas cerca, es decir 5 o mayor suma 1
print(round(1.3))
print(abs(-77))  # valor absoluto de la ecuacion, siempre es positivo

print(math.ceil(1.1))  # devuelve el valor mas cercano hacia arriba
print(math.floor(1.9999))  # devuelve el valor mas cercano hacia abajo
print(math.isnan(5))  # devuelve si el valor no es un numero
print(math.pow(10.3))  # elevar 10 a la 3
print(math.sqrt(9))  # sacar la raiz cuadrada
