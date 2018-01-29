# 9-10
from restaurant import Restaurant

macdonald = Restaurant('macdonald', 'western snack')
macdonald.describe_restaurant()
macdonald.open_restaurant()


# 9-11
from admin import Admin

admin = Admin('triple', 'z', 'man', ['can add post', 'can delete post',
                                     'can ban user'])
admin.describe_user()
admin.privileges.show_privileges()


# 9-12
from adminPrivileges import Admin

admin = Admin('triple', 'z', 'man', ['can add post', 'can delete post',
                                     ])
admin.describe_user()
admin.privileges.show_privileges()