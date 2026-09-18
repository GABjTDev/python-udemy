import numpy as np

identity = np.identity(5, dtype=int)
print('Matriz identidad: \n', identity)

random = np.random.rand(5, 5)
print('Matriz de números aleatorios: \n', random)

random_matrix = np.random.random((5, 5))
print('Matriz de números aleatorios (5x5): \n', random_matrix)

random_int = np.random.randint(1, 10, size=(5, 5))
print('Matriz de números enteros aleatorios (5x5): \n', random_int)

print('Transpuesta de la matriz identidad: \n', random_int.T)
print('Transpuesta de la matriz de números aleatorios: \n', np.transpose(random_int))


empty = np.zeros((3, 3), dtype=str)
print('Matriz vacía (3x3): \n', empty)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Matriz definida: \n', matrix)
print(matrix[1, 1])
print('Sumar toda la matriz: \n', matrix.sum())
print('Sumar toda la fila 0: \n', matrix[0].sum())
print('Sumar toda la columna 1: \n', matrix[:, 1].sum())