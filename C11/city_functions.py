# 11-1
def city_country(city, country, population=-1):
    if population == -1:
        return city.title() + ', ' + country.title()
    else:
        return city.title() + ', ' + country.title() + ' - population ' + str(
          population)

