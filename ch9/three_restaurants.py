class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simulate description of the restaurant."""
        print(
            f"{self.restaurant_name} Restaurant has {self.cuisine_type} cuisine type."
        )

    def open_resturant(self):
        """Simulate the opening of the restaurant."""
        print(f"{self.restaurant_name} is open.")


restaurant_1 = Restaurant('Golden China', 'Asian')
restaurant_2 = Restaurant('Little Vietnam', 'Vietnamese')
restaurant_3 = Restaurant('Bollywood Spice', 'Indian')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
