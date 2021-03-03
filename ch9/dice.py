from random import randint


class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initializing the side attribute."""
        self.sides = sides

    def roll_die(self):
        """Simulating the roll of die."""
        print(f"{randint(1, self.sides)}")


# die = Die()
# for i in range(10):
#     die.roll_die()

# die = Die(sides=10)
# for i in range(10):
#     die.roll_die()

die = Die(sides=20)
for i in range(10):
    die.roll_die()
