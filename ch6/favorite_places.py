favorite_places = {
    'John': ['Paris', 'Istanbul'],
    'Charlotte': ['Rome'],
    'Ali': ['Berlin', 'Tokyo', 'Singapore'],
}

for person, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{person}'s favorite places are:")
        for place in places:
            print(f"\t{place}")
    else:
        print(f"\n{person}'s favorite place is:")
        for place in places:
            print(f"\t{place}")
