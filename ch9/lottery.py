from random import choice

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

print("Any ticket matching these four numbers or letters wins a prize:")
for i in range(4):
    print(choice(lst))
