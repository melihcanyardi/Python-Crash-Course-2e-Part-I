from users import User


class Privileges():
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        """A method to show administrator's privileges."""
        for privilege in self.privileges:
            print("Admin " + privilege + ".")


class Admin(User):
    """A simple attempt to model an Admin."""

    def __init__(self, first_name, last_name, age, location):
        """Inheriting from the User class and adding privileges attribute."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


# admin = Admin('Ahmet', 'Yılmaz', 36, 'İstanbul')
# admin.privileges.show_privileges()
