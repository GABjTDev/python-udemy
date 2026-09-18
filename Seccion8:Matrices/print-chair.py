n = 10

matriz = [
    [
        '1' if (
            fila == n // 2       # Asiento completo.
            or columna == 0      # Respaldo y pata izquierda.
            or (columna == n - 1 and fila > n // 2)  # Pata derecha.
        ) else 0
        for columna in range(n)
    ]
    for fila in range(n)
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea al terminar cada fila.