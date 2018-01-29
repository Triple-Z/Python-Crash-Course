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
