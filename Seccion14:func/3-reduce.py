from functools import reduce

numbers = [10, 20, 30, 40]

# reduce aplica esta función a cada número y conserva el resultado parcial.
#
# En la función:
# - acumulado es la suma que llevamos hasta ahora.
# - numero es el siguiente elemento de la lista.
# - acumulado + numero calcula la nueva suma.
#
# El 0 es el valor inicial del acumulado.
total = reduce(
    lambda acumulado, numero: acumulado + numero,
    numbers,
    0
)

print(total)  # Muestra: 100