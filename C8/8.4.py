# 8-9
def show_magicians(magicians):
    """
    Show magicians function.
    :return: null
    """
    for magician in magicians:
        print(magician)

magicians = ['test1', 'test2', 'test3', 'test4', 'test5']
show_magicians(magicians)


# 8-10
def make_great(magicians):
    for i in range(0, 5):
        magicians[i] = 'the Great ' + magicians[i]

make_great(magicians)
show_magicians(magicians)


# 8-11
def make_great(magicians):
    for i in range(0, 5):
        magicians[i] = 'the Great ' + magicians[i]
    return magicians

newMagicians = make_great(magicians[:])
show_magicians(newMagicians)
show_magicians(magicians)