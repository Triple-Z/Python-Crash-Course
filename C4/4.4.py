cities = ['guangzhou', 'shanghai', 'beijing', 'nanjing', 'palo alto']
pizzas = ['pizza1', 'pizza2', 'pizza3', 'pizza4', 'pizza5']
my_foods = ['pizza', 'falafel', 'carrot cake']

# 4-10
# for city in cities[0:3]:
#     print('The first three items in the list are: ' + city.title())
#
# for city in cities[1:4]:
#     print("The items from the middle of the list are: " + city.title())
#
# for city in cities[2:]:
#     print("The lat three items in the list are: " + city.title())

# 4-11
# friend_pizzas = pizzas[:]
# pizzas.append('pizza6')
# friend_pizzas.append('pizza7')
# print("My favourite pizza are: ")
# for pizza in pizzas:
#     print(pizza)
# print("\nMy friend's favourite pizza are: ")
# for friend_pizza in friend_pizzas:
#     print(friend_pizza)

# 4-12
friend_foods = my_foods[:]

my_foods.append('test')
friend_foods.append('jjj')

print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
