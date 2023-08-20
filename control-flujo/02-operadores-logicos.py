# and or y not


gas = True
encendido = True
edad = 17
# en la evaluacion no es necesario poner = true, se sobrenetiende al comparar
if gas and encendido:
    print("Puedes avanzar")


if gas or encendido:
    print("Puedes avanzar")


if not gas and encendido:
    print("No puedes avanzar")


if gas and (encendido or edad > 17):
    print("Puedes avanzar")

# Operadores de Corto circuito(Depende del operador, si es "and" todas deben ser true, si una de la izquierda es falsa las demas no las evalua asi hay un ahorro de computo)
# en caso de "OR" con que una de la izquierda es true no se evalua los de la derecha, si es false si se evaluan los de la derecha

if not gas or encendido or edad > 17:
    print("Puedes avanzar")
