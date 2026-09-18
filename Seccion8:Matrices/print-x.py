x = 8

matriz = [
    ['x' if fila == columna or fila + columna == x - 1 else 0
        for columna in range(x)]
    for fila in range(x)
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()