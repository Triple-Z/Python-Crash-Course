# 10-3
# name = input("What's your name? ")
# with open('guest', 'a') as guest:
#     guest.write(name + '\n')
#     print('Add name successfully!')


# 10-4
while True:
    name = input("What's your name? (Press Q to exit) ")
    if name == 'q' or name == 'Q':
        break
    else:
        with open('guest_book') as read_guests:
            guests = read_guests.read()
            if name in guests:
                print("Welcome back, " + name)
            else:
                print("Welcome, " + name)
        with open('guest_book', 'a') as guest_book:
            guest_book.write(name + " logged into the system.\n")


# 10-5
isActive = True
while isActive:
    reason = input("Why are you like programming? (Press Q to quit) ")
    if reason == 'q' or reason == 'Q':
        isActive = False
    else:
        with open('programming_reasons', 'a') as reasons:
            reasons.write(reason + '\n')