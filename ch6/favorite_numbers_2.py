favorite_numbers = {
    'John': [5, 8, 3],
    'Joe': [3, 6, 7],
    'Sophia': [2, 5, 8],
    'Charlotte': [1, 3, 7],
    'Oliver': [3, 6, 9], }

for person, numbers in favorite_numbers.items():
    print(f"\n{person}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")
