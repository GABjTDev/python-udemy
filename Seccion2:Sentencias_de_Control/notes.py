promedio_mayor_5 = 0
promedio_menor_4 = 0
notes_1 = 0

for i in range(20):
    note = float(input("Introduce la nota del estudiante: "))

    if(note > 5):
        promedio_mayor_5 += note
    elif(note < 4):
        promedio_menor_4 += note
    elif(note == 1):
        notes_1 += 1

    if(note <= 0):
        print('Hubo un error!')
        break


print(f'Promedio de notas mayores a 5: {promedio_mayor_5 / 20}')
print(f'Promedio de notas menores a 4: {promedio_menor_4 / 20}')
print(f'Cantidad de notas iguales a 1: {notes_1}')