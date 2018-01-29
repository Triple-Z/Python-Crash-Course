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