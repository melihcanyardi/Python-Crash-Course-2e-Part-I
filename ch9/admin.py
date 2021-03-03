class User():
    """A simple attempt to model a user profile."""

    def __init__(self, first_name, last_name, age, location):
        """Initialize first_name, last_name, age, and location attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        """Print a summary of the user's information"""
        print(
            f"User's name: {self.first_name} {self.last_name}\nUser's age: {self.age}\nUser's location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello {self.first_name}!")


class Admin(User):
    """A simple attempt to model an Admin."""

    def __init__(self, first_name, last_name, age, location):
        """Inheriting from the User class and adding privileges attribute."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """A method to show administrator's privileges."""
        for privilege in self.privileges:
            print("Admin " + privilege + ".")


admin = Admin('Ahmet', 'Yılmaz', 36, 'İstanbul')
admin.show_privileges()
