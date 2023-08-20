

# se ejecuta de arriba hacia abajo, luego que llega abajo vuelve hacia arriba, por eso el primer valor es j = 0 y k = 0, luego sube y k = 0 y j = 1
# cuando termino los 2 ciclos vuelve a iniciar y J = 1 y k = 0, sube nuevamente y K = 1 y j = 1
# luego vuelve a iniciar y j = 2 y k = 0, sube nuevamente y k = 1 y j = 2
for j in range(3):
    for k in range(2):
        print(f"{j},{k}")
