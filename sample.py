person = {'name':'Park Von Jae','age': 24, 'language': 'Python'}
print(person.get('language'))
person.update({'age': 25})
print(person)
person.update({'Hobby':'Coding'})
print(person)

for key,value in person.items():
    print(f'{key} : {value}')

if 'Hobby' in person:
    print('Existing in dictionary collection')

person.pop('age')
print(person)

print(person.get('gaming'))
print(help(person))