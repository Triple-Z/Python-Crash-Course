# 6-4
from dnf.yum.misc import unlink_f

dictionary = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
}
for k, v in dictionary.items():
    print('Key: ' + k + ', Value: ' + v)

dictionary['if'] = 'Condition check'
dictionary['for'] = 'Loop'
dictionary['tuple'] = 'Unchangeable element set'
dictionary['list'] = 'Changeable dynamic element set'
print()
for key, value in dictionary.items():
    print('Key: ' + key + ', Value: ' + value)

# 6-5
print()
rivers = {
    'nile': 'egypt',
    'yellow': 'china',
    'mississippi': 'united states',
}
for k, v in rivers.items():
    print('The ' + k.title() + ' runs through ' + v.title() + '.')
print()
for river in rivers.keys():
    print(river.title() + ' River')
print()
for country in rivers.values():
    print(country.title())

# 6-6
favorite_language = {
    'triple z': 'python',
    'uncleblue': 'c++',
    'sundoge': 'javascript',
    'foxwest': 'python',
    'hugo': 'python',
}
survey_list = ['triple z', 'uncleblue', 'sundoge', 'user1', 'user2']
for user in survey_list:
    if user in favorite_language.keys():
        print(user.title() + ', Thank you for doing our survey~')
    else:
        print(user.title() + ', Please do our survey!')

