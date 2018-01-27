# 8-12
def add_toppings(*toppings):
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping.title())

add_toppings('pepperoni')
add_toppings('mushrooms', 'green peppers')
add_toppings('pepperoni', 'extra cheese', 'mushrooms')


# 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile('triple', 'z',
              location='guangzhou',
              field='internet of things',
              girlfriend='uncleblue')
print()
print(my_profile)


# 8-14
def make_car(manufacturer, type, **additions):
    """
    Build a car profile.
    :param manufacturer:
    :param type:
    :param additions:
    :return car:
    """
    car = dict()
    car['manufacturer'] = manufacturer
    car['type'] = type
    for k, v in additions.items():
        car[k] = v
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
