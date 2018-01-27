# 8-16
def make_car(
        manufacturer,
        type,
        **additions):
    """
    Build a car profile.
    :param manufacturer:
    :param type:
    :param additions:
    :return car:
    """
    car = dict()
    car['manufacturer'] = manufacturer
    car['type'] = type
    for k, v in additions.items():
        car[k] = v
    return car