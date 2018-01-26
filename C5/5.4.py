# 5-8
# users = ['triple z', 'uncleblue', 'admin', 'hugo', 'milk']
# loginUser = 'triple z'
# if loginUser in users:
#     if loginUser == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print("Hello " + loginUser.title() + ", thank you for logging in "
#                                              "again.")
#
# else:
#     print('Authorization failed!')

# 5-9
# users = []
# loginUser = 'triple z'
# if users:
#     if loginUser in users:
#         if loginUser == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print("Hello " + loginUser.title() + ", thank you for logging in "
#                                                  "again.")
#
#     else:
#         print('Authorization failed!')
# else:
#     print("We need some users!")

# 5-10
# current_users = ['triple z', 'uncleblue', 'admin', 'hugo', 'milk']
# new_users = ['triple z', 'ADMIN', 'user1', 'user2', 'user3']
# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print("This name \"" + new_user + "\" has already used!")
#     else:
#         print("This name \"" + new_user + "\" is not used!")

# 5-11
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')

