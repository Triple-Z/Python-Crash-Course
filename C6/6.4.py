# 6-7
uncleblue = {}
uncleblue['first_name'] = 'Jiang'
uncleblue['last_name'] = 'Wanshu'
uncleblue['age'] = 20
uncleblue['city'] = 'Tianjin'

triplez = {
    'first_name': 'Zhao',
    'last_name': 'Zhenzhen',
    'age': 20,
    'city': 'Guangzhou',
}

sundoge = {
    'first_name': 'Huang',
    'last_name': 'Deng',
    'age': 21,
    'city': 'Guangzhou',
}

people = [uncleblue, triplez, sundoge]

for person in people:
    print('Name: ' + person['first_name'].title() + ' '
          + person['last_name'].title())
    print('\tAge: ' + str(person['age']))
    print('\tCity: ' + person['city'].title())

# 6-8
print()
cabbage = {
    'name': 'cabbage',
    'type': 'dog',
    'host': 'uncleblue',
}
jade = {
    'name': 'jade',
    'type': 'dog',
    'host': 'uncleblue',
}
true = {
    'name': 'true',
    'type': 'cat',
    'host': 'uncleblue'
}
pets = [cabbage, jade, true]
for pet in pets:
    print('Pet name: ' + pet['name'].title())
    print('\tType: ' + pet['type'].title())
    print('\tHost: '+ pet['host'].title())

# 6-9
print()
favorite_places = {
    'triple z': ['palo alto', 'paris', 'berlin', 'berkeley'],
    'uncleblue': ['paris', 'tianjin', 'toronto'],
    'sundoge': ['tokyo'],
}
for people, places in favorite_places.items():
    print('Name: ' + people.title())
    print('Places: ')
    for place in places:
        print('\t' + place.title())

# 6-10
print()
favorite_numbers = {}
favorite_numbers['triple z'] = [1, 3, 5, 6, 7]
favorite_numbers['uncleblue'] = [8, 9, 2]
favorite_numbers['test1'] = [1]
favorite_numbers['test2'] = [2]
favorite_numbers['test3'] = [3]

for people, numbers in favorite_numbers.items():
    print(people.title() + ':')
    for number in numbers:
        print('\t' + str(number))

# 6-12
# Extent for favorite_languages.py
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
