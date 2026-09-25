my_set = {'Pera', 'Manzana', 'Naranja'}
my_set.add('Uva')
print(my_set)

my_set.update(['Pera', 'Manzana', 'Tomate', 'Cebolla'])
print(my_set)

my_set |= {'Durazno', 'Kiwi'}
print(my_set)

new_fruits = {'mango', 'papaya'}
for fruit in new_fruits:
    my_set.add(fruit)
print(my_set)