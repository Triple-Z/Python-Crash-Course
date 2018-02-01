# 10-11
# import json
#
# number = input('\nWhat\'s your favorite number? ')
# with open('number.json', 'w') as file:
#     json.dump(int(number), file)
#
# with open('number.json') as file:
#     number = json.load(file)
# print("I know your favorite number! It's " + str(number) + '.')


# 10-12
# import json
#
# try:
#     with open('number.json') as file:
#         number = json.load(file)
# except FileNotFoundError:
#     number = input('\nWhat\'s your favorite number? ')
#     with open('number.json', 'w') as file:
#         json.dump(int(number), file)
# else:
#     print("I know your favorite number! It's " + str(number) + '.')


# 10-13
import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        isRight = input("Are you " + username + '? (y/n) ')
        if isRight == 'n' or isRight == 'N':
            username = get_new_username()
            print("We'll remember you when you come back, " + username + '!')
        elif isRight == 'y' or isRight == 'Y':
            print('Welcome back, ' + username + '!')
        else:
            print('INPUT ERROR!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')

greet_user()
