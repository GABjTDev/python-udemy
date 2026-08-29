
count = 1
min_value = float('inf')  # Initialize to positive infinity
print('Vamos a encontrar el valor mínimo')

while(count <= 10):

    value = int(input('Introduce un numero: '))

    if value <= min_value:
        min_value = value

    count = count + 1


if min_value < 10:
    print("El número menor es menor que 10!")
else:
    print("el numero menor es igual o mayor que 10!")