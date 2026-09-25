# locale permite usar reglas regionales, por ejemplo, para ordenar texto
# teniendo en cuenta las reglas de un idioma.
import locale

# reduce aplica una función varias veces para combinar elementos y obtener un único resultado.
from functools import reduce

# numpy es una biblioteca para trabajar con arreglos y cálculos numéricos.
import numpy as np

# statistics incluye funciones estadísticas, como el promedio.
import statistics


# Lista de números enteros.
numbers = [10, 20, 30, 40]

# sum suma todos los elementos de la lista.
total = sum(numbers)
print(total)  # Muestra: 100

# np.array(numbers) convierte la lista en un arreglo de NumPy.
# .sum() suma los valores de ese arreglo.
total2 = np.array(numbers).sum()
print(total2)  # Muestra: 100


# Tupla de calificaciones.
scores = (80, 90, 100)

# statistics.mean calcula el promedio de los valores.
average = statistics.mean(scores)
print(average)  # Muestra: 90


# Lista de palabras.
words = ['apple', 'banana', 'pear', 'grape']

# min busca el elemento menor.
# key=len indica que debe comparar las palabras por su longitud,
# en vez de compararlas alfabéticamente.
shortest = min(words, key=len)
print(shortest)  # Muestra: pear


# Lista de palabras en español.
palabras = ['Manazana', 'Uva', 'Banana', 'arándanos']

# Selecciona las reglas de idioma español para todas las categorías regionales.
# El nombre exacto del locale depende del sistema operativo y de los locales instalados.
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # En algunos sistemas puede usarse otro nombre.

# locale.strxfrm prepara cada texto para compararlo según las reglas del locale configurado.
# min devuelve la palabra que queda primero con ese criterio de ordenamiento.
menor = min(palabras, key=locale.strxfrm)
print(menor)


# max devuelve el elemento mayor según el criterio indicado por key.
# str.lower convierte temporalmente cada texto a minúsculas para compararlos
# sin distinguir entre mayúsculas y minúsculas.
mayor = max(palabras, key=str.lower)

# Aquí se comparan las palabras por su longitud.
mayor2 = max(palabras, key=len)
print(mayor)
print(mayor2)


# max y min sin key comparan los números directamente.
max_int = max(numbers)
min_int = min(numbers)
print(max_int)  # Muestra: 40
print(min_int)  # Muestra: 10


# Lista de diccionarios: cada diccionario representa a una persona
# y guarda su nombre y su edad.
people = [
    {'name': 'Ana', 'age': 28},
    {'name': 'Luis', 'age': 35},
    {'name': 'Carlos', 'age': 30}
]

# lambda p: p['age'] es una función breve que recibe una persona (p)
# y devuelve su edad.
# max usa esa edad para encontrar el diccionario de la persona mayor.
oldest = max(people, key=lambda p: p['age'])

# oldest es el diccionario completo; ['name'] obtiene su valor asociado a la clave 'name'.
print(oldest['name'])  # Muestra: Luis


# Otra lista de palabras.
palabras = ['Zorro', 'abeja', 'Mono']

# sorted devuelve una lista nueva con los elementos ordenados.
# key=str.upper compara las palabras como si estuvieran en mayúsculas.
# reverse=True invierte el orden, de mayor a menor según ese criterio.
palabras_ordenadas = sorted(palabras, key=str.upper, reverse=True)
print(palabras_ordenadas)


# Ordena las personas por edad, de mayor a menor.
# lambda k: k['age'] le indica a sorted que use la edad como criterio.
a = sorted(people, key=lambda k: k['age'], reverse=True)

# Ordena las personas alfabéticamente por nombre.
b = sorted(people, key=lambda i: i['name'])

# len(i['name']) calcula la cantidad de caracteres del nombre.
# Por eso esta lista queda ordenada desde el nombre más corto al más largo.
c = sorted(people, key=lambda j: len(j['name']))

print(a)
print(b)
print(c)


# Suma las edades.
# La expresión entre paréntesis recorre people y toma la edad de cada persona.
d = sum(p['age'] for p in people)
print(d)  # Muestra: 93


# reduce combina los elementos de people uno por uno hasta producir un resultado.
#
# En cada paso:
# - initial es el acumulador, donde se guarda la suma parcial.
# - current es el diccionario de la persona actual.
# - initial + current['age'] agrega la edad actual al acumulador.
#
# El 0 final es el valor inicial del acumulador.
e = reduce(
    lambda initial, current: initial + current['age'],
    people,
    0
)
print(e)  # Muestra: 93