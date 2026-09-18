import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

y = np.random.randint(1, 10, size=(3, 3))

print('Matriz x: \n', x)
print('Matriz y: \n', y)

print('Suma de las matrices: \n',  np.add(x, y))
print('Resta de las matrices: \n', np.subtract(x, y))
print('Producto de las matrices: \n', np.multiply(x, y))
print('División de las matrices: \n', np.divide(x, y))

print('Eliminar filas: \n', np.delete(x, 1, axis=0))
print('Eliminar columnas: \n', np.delete(x, 1, axis=1))