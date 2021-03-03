class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize restaurant_name, cuisine_type, and number_served attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Simulate description of the restaurant."""
        print(
            f"{self.restaurant_name} Restaurant has {self.cuisine_type} cuisine type."
        )

    def open_resturant(self):
        """Simulate the opening of the restaurant."""
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number):
        """Sets the number served."""
        self.number_served = number

    def increment_number_served(self, increment_number):
        """Increments the number served."""
        self.number_served += increment_number


restaurant = Restaurant('Golden China', 'Asian')

print(restaurant.number_served)

# restaurant.number_served = 3
# print(restaurant.number_served)

# restaurant.set_number_served(5)
# print(restaurant.number_served)

restaurant.increment_number_served(7)
print(restaurant.number_served)
