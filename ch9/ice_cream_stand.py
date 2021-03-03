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


class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inheriting from Restaurant class and adding flavors attribute."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        """A method to display ice cream flavors."""
        print("The flavors are:")
        for flavor in self.flavors:
            print('- ', flavor.title())


icecreamstand = IceCreamStand('Ice Cream World', 'Ice Cream')

icecreamstand.display_flavors()
