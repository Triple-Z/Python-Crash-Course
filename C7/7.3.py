# 7-8
sandwich_orders = ['pastrami', 'reuben', 'club', 'pastrami', 'smoked',
                   'chicken breast', 'pastrami']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print('I made your tuna sandwich')
print(finished_sandwiches)

# 7-9
sandwich_orders = ['pastrami', 'reuben', 'club', 'pastrami', 'smoked',
                   'chicken breast', 'pastrami']
finished_sandwiches = []
print('\nPastrami is sold out!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print('I made your tuna sandwich')
print(finished_sandwiches)

# 7-10
responses = {}
polling_active = True
while polling_active:
    name = input('\nWhat is your name? ')
    response = input('If you could visit one place in the world, where would '
                     'you go? ')
    responses[name] = response
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False
print('\n ---- Poll Results ----')
for name, response in responses.items():
    print(name.title() + ' would like to go to ' + response.title() + '.')
