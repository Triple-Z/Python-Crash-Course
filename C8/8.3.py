# 8-6
def city_country(name, country):
    return name.title() + ', ' + country.title()

print(city_country('santiago', 'chile'))
print(city_country('guangzhou', 'china'))
print(city_country('palo alto', 'united states'))


# 8-7
def make_album(singer, name, total=''):
    album = {
        'singer': singer.title(),
        'name': name.title(),
    }
    if total:
        album['total'] = int(total)
    return album

print(make_album('linkin park', 'a thousand suns', '12'))
print(make_album('danger kids', 'collapse'))
print(make_album('the first', 'take courage'))


# 8-8
def make_album(singer, name, total=''):
    album = {
        'singer': singer.title(),
        'name': name.title(),
    }
    if total:
        album['total'] = int(total)
    return album

while True:
    print('\nInput the info of a album:')
    print('Press \'q\' if you want to exit')
    singer = input('Input singer name: ')
    if singer == 'q':
        break
    name = input('Input album name: ')
    if name == 'q':
        break
    album = make_album(singer=singer, name=name)
    print(album)


