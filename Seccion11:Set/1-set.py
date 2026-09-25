
s = {'uno', 'dos', 'tres'}
print(s)

s.add('tres')
b = 'Tres' not in s
print(f'El elemento "Tres" no está en el conjunto: {b}')

if b:
    s.add('Tres')

print(s)

for n in s:
    print(n, end=' ')

# print()
# for element in sorted(s):
#     print(element)

for i, element in enumerate(sorted(s)):
    print(f'{i}: {element}')


sorted_lista = sorted(s)
print(sorted_lista)
print(sorted_lista[0])

set_to_list = list(s)
print(set_to_list[0])