nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate Python, este curso complenta todo los detalles necesarios para que obtengas tu primer trabajo
"""

tamanio = len(descripcion_curso)  # se obtiene el tamaño de la variable

print(nombre_curso[0])
# es como el substring(0,5) para obtener la palabra que corresponde al espacio 0 hasta el 5
print(nombre_curso[0:5])
# si no se especifica de donde inicia lo toma por defecto en 0, al igual si no se especifica el final lo interpreta como la variable final
print(nombre_curso[9:])
# inicia en el valor 0, luego se salta hasta el valor que le indiquemos
print(nombre_curso[::2])
