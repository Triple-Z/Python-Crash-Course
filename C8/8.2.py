# 8-3
def make_shirt(size, string):
    """Make shirt"""
    print('Size: ' + size + ', String: ' + string)

make_shirt('M', 'Hello, World')
make_shirt(size='M', string='Hello, World again')


# 8-4
def make_shirt(size='L', string='I love Python'):
    """Make python shirt"""
    print('Size: ' + size + ', String: ' + string)

make_shirt()
make_shirt(size='M')
make_shirt(string='Hello, World')


# 8-5
def describe_city(name='guangzhou', country='china'):
    """Describe a city you lived in"""
    print(name.title() + ' is in ' + country.title())

describe_city('Nanjing')
describe_city(country='united states')
describe_city('palo alto', 'united states')
