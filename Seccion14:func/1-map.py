# Creamos una lista de números enteros.
numbers = [1, 2, 3, 4, 5, 6, 7]

# lambda x: ... crea una función pequeña y sin nombre.
# Recibe un número (x), lo multiplica por 2 y convierte el resultado en texto con str().
#
# map(...) aplica esa función a cada elemento de numbers.
# map devuelve un iterador, y list(...) lo convierte en una lista.
numbers_x2 = list(map(lambda x: str(x * 2), numbers))
print(numbers_x2)  # Muestra: ['2', '4', '6', '8', '10', '12', '14']

# Esta comprensión de listas hace lo mismo que la línea anterior:
# recorre cada número x, lo multiplica por 2 y convierte el resultado en texto.
pairs_numbers = [str(x * 2) for x in numbers]
print(pairs_numbers)  # Muestra la misma lista que numbers_x2.

# Creamos una lista de nombres y apellidos.
names = ['Andres Guzman', 'Maria Perez', 'John Doe', 'Josefa Mena']

# Aplicamos una función a cada nombre:
# 1. name.split() separa el texto por los espacios.
#    Por ejemplo: 'Andres Guzman' se convierte en ['Andres', 'Guzman'].
# 2. [1] toma el elemento en la posición 1, es decir, el apellido.
# map(...) aplica esa operación a cada nombre y list(...) guarda los resultados en una lista.
# Esto supone que cada nombre tiene al menos dos palabras.
lastnames = list(map(lambda name: name.split()[1], names))
print(lastnames)  # Muestra: ['Guzman', 'Perez', 'Doe', 'Mena']

# Los índices empiezan en 0: [1] accede al segundo elemento, 'Perez'.
print(lastnames[1])

# Mostramos las listas originales; map y split no las modificaron.
print(numbers)
print(names)