# 9-4
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('\nRestaurant name: ' + self.restaurant_name.title())
        print('Cuisine type: ' + self.cuisine_type.title())
        print('Served: ' + str(self.number_served))

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open')

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, increment_number):
        if increment_number < 0:
            print('You cannot put negative numbers!')
        else:
            self.number_served += increment_number

macdonald = Restaurant('macdonald', 'western snack')
macdonald.describe_restaurant()
macdonald.number_served = 15
macdonald.describe_restaurant()

macdonald.set_number_served(80)
macdonald.describe_restaurant()

macdonald.increment_number_served(10)
macdonald.describe_restaurant()


# 9-5
class User:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print('\nUser name:' + self.first_name.title() + ' ' +
              self.last_name.title())
        print('User gender: ' + self.gender.title())
        print('User login attempts: ' + str(self.login_attempts))

    def greet_user(self):
        print("\nHello, " + self.first_name.title() + ' ' +
              self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

triplez = User('triple', 'z', 'man')
triplez.increment_login_attempts()
triplez.increment_login_attempts()
triplez.increment_login_attempts()
triplez.increment_login_attempts()
triplez.increment_login_attempts()
triplez.describe_user()
triplez.reset_login_attempts()
triplez.describe_user()

