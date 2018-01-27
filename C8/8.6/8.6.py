# 8-15
import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_designs = []

printing_functions.print_models(unprinted_designs, completed_designs)
printing_functions.show_completed_models(completed_designs)


# 8-16
import car
car_ = car.make_car('subaru', 'outback', color='blue', tow_package=True)
print()
print(car_)


