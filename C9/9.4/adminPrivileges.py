from user import User

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