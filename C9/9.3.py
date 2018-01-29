# 9-6
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


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def get_ice_cream_flavors(self):
        print('Ice cream flavors: ')
        for flavor in self.flavors:
            print('\t' + flavor)


test = IceCreamStand('test name', 'sweet food', ['strawberry', 'tea', 'milk'])
test.describe_restaurant()
test.get_ice_cream_flavors()


# 9-7
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


# class Admin(User):
#
#     def __init__(self, first_name, last_name, gender, privileges):
#         super().__init__(first_name, last_name, gender)
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print('\nAdmin privileges:')
#         for privilege in self.privileges:
#             print('\t- ' + privilege.title())
#
# admin = Admin('triple', 'z', 'man', ['can add post', 'can delete post',
#                                      'can ban user'])
# admin.describe_user()
# admin.show_privileges()


# 9-8
class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('\nPrivileges:')
        for privilege in self.privileges:
            print('\t- ' + privilege.title())


class Admin(User):

    def __init__(self, first_name, last_name, gender, privileges):
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges(privileges)


admin = Admin('triple', 'z', 'man', ['can add post', 'can delete post',
                                     'can ban user'])
admin.describe_user()
admin.privileges.show_privileges()


# 9-9
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        print('\n' + str(self.year) + ' ' + self.make.title() + ' ' +
                  self.model.title())


class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        msg = 'This car can go approximately ' + str(range)
        msg += ' miles on a full charge.'
        print(msg)

    def update_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_descriptive_name()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()
