number_1 = int(input("Introduce el primer número: "))
number_2 = int(input("Introduce el segundo número: "))

number_heigher = str(number_1) + ', ' + str(number_2) if number_1 > number_2 else str(number_2) + ', ' + str(number_1)

print(f"El orden de los numeros es: {number_heigher}")
