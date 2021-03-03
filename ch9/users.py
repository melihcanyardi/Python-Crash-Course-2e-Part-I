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


# user_1 = User('Ahmet', 'Yılmaz', 36, 'İstanbul')
# user_1.describe_user()
# user_1.greet_user()

# user_2 = User('Ali', 'Durmaz', 23, 'Berlin')
# user_2.describe_user()
# user_2.greet_user()
