# 10-6
while True:
    number = input("Enter a number: (Press Q to exit)")
    if number == 'q' or number == 'Q':
        break
    try:
        int_number = int(number)
    except ValueError:
        print("VALUE ERROR! You should input a integer number.")
    else:
        print("The number you have entered is: " + str(int_number))


# 10-7
# 在 10-6 中已经完成了……


# 10-8
def print_file(filename):
    """Print all the contents in a file"""
    try:
        with open(filename) as target:
            contents = target.read()
    except FileNotFoundError:
        print("FILE \"" + filename + "\" NOT FOUND!")
    else:
        print(contents)


files = ['cats', 'dogs']
for file in files:
    print("\nIn file: " + file)
    print_file(file)


# 10-9
def print_file(filename):
    """Print all the contents in a file"""
    try:
        with open(filename) as target:
            contents = target.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


files = ['cats', 'dogs']
for file in files:
    print("\nIn file: " + file)
    print_file(file)


# 10-10
with open('poems') as poems:
    contents = poems.read()

times = contents.lower().count('the')
print('\nThe times of the word "the" is: ' + str(times))