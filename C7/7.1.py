# 7-1
car = input('What kind of car you want to rent?')
print('Let me see if I can find you a ' + car.title())

# 7-2
people = input('How many people are waiting for dinner? ')
if int(people) > 8:
    print('There is no empty table.')
else:
    print('There has empty table.')

# 7-3
number = input('Input a number')
if int(number) % 10 == 0:
    print('10 整数倍')
else:
    print('不是 10 整数倍')
