class User():
    """A simple attempt to model a user profile."""

    def __init__(self, first_name, last_name, age, location, login_attempts):
        """Initialize first_name, last_name, age, and location attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        """Print a summary of the user's information"""
        print(
            f"User's name: {self.first_name} {self.last_name}\nUser's age: {self.age}\nUser's location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        """Increments login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0."""
        self.login_attempts = 0


user_1 = User('Ahmet', 'Yılmaz', 36, 'İstanbul', 0)

print(user_1.login_attempts)

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)
