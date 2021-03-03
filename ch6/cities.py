cities = {
    'paris': {
        'country': 'france',
        'population': 2175601,
        'fact': 'Paris was originally a Roman City called “Lutetia.”',
    },
    'istanbul': {
        'country': 'turkey',
        'population': 15460000,
        'fact': 'Istanbul is the only pan-continental city in the world situated on two continents, Europe and Asia.',
    },
    'berlin': {
        'country': 'germany',
        'population': 3769000,
        'fact': 'Berlin has the largest train station in Europe.',
    },
}

for city, information in cities.items():
    print(
        f"{city.title()} is in {information['country'].title()}. It has a population of {information['population']} people. "
        f"Here is an interesting fact about {city}: {information['fact']}\n")
