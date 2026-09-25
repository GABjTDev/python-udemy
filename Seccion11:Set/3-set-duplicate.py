
fish = ['trucha', 'salmon', 'bacalao', 'trucha', 'salmon', 'bacalao']
print(fish)


unique = set() # type: ignore
duplicates = set() # type: ignore

for f in fish:
    if f in unique:
        print('Elemento duplicado:', f)
        duplicates.add(f) # type: ignore
    else:
        unique.add(f) # type: ignore

print('Elementos únicos:', unique) # type: ignore
print('Elementos duplicados:', duplicates) # type: ignore