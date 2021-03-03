from users import User
from privileges import Privileges, Admin

admin = Admin('Ahmet', 'Yılmaz', 36, 'İstanbul')
admin.privileges.show_privileges()
