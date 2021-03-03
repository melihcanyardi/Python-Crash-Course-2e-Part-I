sandwich_orders = ['bacon', 'tuna', 'pastrami',
                   'cheese', 'pastrami', 'chicken', 'pastrami']
print("The deli has ran out of pastrami.")
finished_sandwiches = []


while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches are made:")
for sandwich in finished_sandwiches:
    print(sandwich)
