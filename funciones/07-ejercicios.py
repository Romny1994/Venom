# funcion para quitar espacios en blanco
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

# funcion para dar vuelta al texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)  # funcion para quitar espacios en blanco
    texto_al_reves = reverse(texto)  # funcion para dar vuelta al texto
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("amo la paloma"))
