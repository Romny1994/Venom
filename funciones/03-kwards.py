# keyword arguments es decir empaquetar los parametros, se ponen 2 asteriscos al inicio

def get_product(**datos):
    print(datos["id"], datos["name"])  # obtener el id,nombre de la lista


# en los keyword arguments se debe definir el nombre del parametro que se va enviar, al ejecutar la funcion devuelve un diccionario
get_product(id="id", name="cellphone", model="samsung")
