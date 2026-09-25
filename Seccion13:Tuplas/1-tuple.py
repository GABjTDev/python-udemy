tuple_number = (10, 20, 30, 40, 50, 60)
tuple_number2 = 1, 2, 3, 4, 5, 6
tuple_number3 = (30,)

colors = 'red', 'green', 'blue', 'blue'
colors2 = ('yellow', 'purple')

print(colors[-1])
print(colors2[0])

for color in colors2:
    print(f'Color: {color}')


print(colors.count('blue'))
print(colors.index('red'))

position = {('x', 'y'): 3.1415}
print(position[('x', 'y')])