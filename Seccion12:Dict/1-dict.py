person: dict[str, str | int | dict[str, str]] = {}

person['name'] = 'Gabriel'
person['last_name'] = 'Rea'
person.update({ 'age': 30, 'email': 'gabriel.rea@example.com' })
print(person)

address = {
    'street': '123 Main St',
    'city': 'New York',
    'zip_code': '10001',
    'country': 'USA',
    'other': 'Some other value'
}

person['address'] = address

first_name = person.get('name')
last_name = person.get('last_name')

print(first_name, last_name)

email = person.pop('email')
# del person['email']
print(person)
print(f'Email borrado: {email}')


# other = person['other']
other = person.get('other')
print(f'Un valor que no existe: {other}')

print(len(person))
print('Contiene elemento: ', len(person) > 0, bool(person))
print(person.keys())
print(person.values())

has_key = 'paternal_last_name' in person
print(f'Tiene la clave: {has_key}')

has_values = 'gabriel.rea@example.com' in person.values() or 'Rea' in person.values()
print(f'Tiene el valor: {has_values}')

for value in person.values():
    print(f'Valor: {value}')

for key in person.keys():
    print(f'Clave: {key}')

for key, value in person.items():
    print(key, '=>', value)


country = person['address']['country']
print(f'El pais de persona: {first_name} es {country}')

for key in person.keys():
    value = person[key]
    if isinstance(value, dict):
        for subkey, subvalue in value.items():
            print(f'  {subkey}: {subvalue}')
    else:
        print(f'  {key}: {value}')