# 10-1
with open('learning_python') as file:
    print('\nFirst print:')
    print(file.read())

with open('learning_python') as file:
    print('\nSecond print:')
    for line in file:
        print(line.rstrip())

with open('learning_python') as file:
    print('\nThird print:')
    lines = file.readlines()

for line in lines:
    print(line.rstrip())


# 10-2
with open('learning_python') as file:
    print('\n10-2:')
    lines = file.readlines()

for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())

