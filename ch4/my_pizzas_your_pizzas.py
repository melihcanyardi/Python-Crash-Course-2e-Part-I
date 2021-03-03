pizzas = ['broccoli', 'pineapple', 'bbq']
friend_pizzas = pizzas[:]

pizzas.append('margarita')
friend_pizzas.append('neopolitan')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
