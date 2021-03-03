from random import choice

my_ticket = [3, 6, 'a', 'd']

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

winning = []
counter = 0

while winning != my_ticket:
    winning = []
    for i in range(4):
        winning.append(choice(lst))
    counter += 1

print(counter)
