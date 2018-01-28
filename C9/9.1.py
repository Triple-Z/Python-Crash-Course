# 9-1
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('\nRestaurant name: ' + self.restaurant_name.title())
        print('Cuisine type: ' + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open')


restaurant = Restaurant('guangzhou restaurant', 'canteen')
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2
macdonald = Restaurant('macdonald', 'western snack')
macdonald.describe_restaurant()
kfc = Restaurant('kfc', 'western snack')
kfc.describe_restaurant()


# 9-3
class User():
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def describe_user(self):
        print('\nUser name:' + self.first_name.title() + ' ' +
              self.last_name.title())
        print('User gender: ' + self.gender.title())

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + ' ' +
              self.last_name.title())

triplez = User('triple', 'z', 'man')
uncleblue = User('uncle', 'blue', 'woman')
triplez.describe_user()
triplez.greet_user()
uncleblue.describe_user()
uncleblue.greet_user()
