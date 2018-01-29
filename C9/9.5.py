# 9-13
from collections import OrderedDict

dictionary = OrderedDict()

dictionary['a'] = 'A'
dictionary['b'] = 'B'
dictionary['c'] = 'C'
dictionary['d'] = 'D'
dictionary['e'] = 'E'

for k, v in dictionary.items():
    print('Key: ' + k + ', Value: ' + v)

dictionary['if'] = 'Condition check'
dictionary['for'] = 'Loop'
dictionary['tuple'] = 'Unchangeable element set'
dictionary['list'] = 'Changeable dynamic element set'
print()
for key, value in dictionary.items():
    print('Key: ' + key + ', Value: ' + value)


# 9-14
from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

die6 = Die()
print('\n6 sides die:')
for i in range(0, 10):
    print(die6.roll_die())

die10 = Die(10)
print('\n10 sides die:')
for i in range(0, 10):
    print(die10.roll_die())

die20 = Die(20)
print('\n20 sides die: ')
for i in range(0, 10):
    print(die20.roll_die())
