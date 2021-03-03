pizza = []
prompt = "\nPlease enter the pizza topping you'd like to add."
prompt += "\nEnter 'quit' when you're finished. "
topping = ""

while True:
    topping = input(prompt)
    if topping == 'quit':
        break

    print(f"Adding {topping.lower()} to your pizza.")
    pizza.append(topping)

print("\nThe ingredients of your pizza are:")
for topping in pizza:
    print(topping)
