favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['sarah', 'stewart', 'john', 'edward']

for person in people:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for responding.")
    else:
        print(f"{person.title()}, please take the pool.")
