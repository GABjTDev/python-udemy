# Lista de números enteros.
nums = [1, 2, 3, 4, 5, 6]

# lambda y: y % 2 == 0 es una función breve:
# recibe un número y devuelve True si es par, o False si es impar.
# El operador % calcula el resto de una división: los pares dejan resto 0 al dividirse por 2.
#
# filter(...) conserva solo los elementos para los que la función devuelve True.
# list(...) convierte el resultado de filter en una lista.
pairs = list(filter(lambda y: y % 2 == 0, nums))
print(pairs)  # Muestra: [2, 4, 6]

# Esta comprensión de listas hace lo mismo:
# recorre nums y agrega a la lista solo los números que cumplen la condición.
pairs2 = [y for y in nums if y % 2 == 0]
print(pairs2)  # Muestra: [2, 4, 6]

# Lista de nombres completos.
names = [
    'Andres Guzman',
    'Pepe Doe',
    'Mariela Gonzalez',
    'Claudio Roe',
    'James Gosling',
    'Bruce Doe'
]

# Para cada nombre:
# 1. split() separa el nombre y el apellido usando el espacio.
#    Por ejemplo: 'Pepe Doe' se convierte en ['Pepe', 'Doe'].
# 2. [1] obtiene la segunda parte, que aquí es el apellido.
# 3. La comparación == 'Doe' devuelve True si el apellido es 'Doe'.
#
# filter(...) conserva los nombres cuya condición devuelve True.
filter_names = list(filter(lambda name: name.split()[1] == 'Doe', names))

# Otra forma de aplicar el mismo filtro, usando una comprensión de listas.
filter_names2 = [name for name in names if name.split()[1] == 'Doe']

print(filter_names2)  # Muestra: ['Pepe Doe', 'Bruce Doe']
print(filter_names)   # Muestra el mismo resultado.

# filter conserva los números para los que x != 3 es True.
# != significa “distinto de”. En este caso, se excluye el número 3.
new_nums = list(filter(lambda x: x != 3, nums))
print(new_nums)  # Muestra: [1, 2, 4, 5, 6]