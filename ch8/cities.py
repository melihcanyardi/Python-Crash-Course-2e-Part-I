def describe_city(city, country='Turkey'):
    """Returns city and its country, neatly formatted."""
    print(f"{city.title()} is in {country.title()}.")


describe_city('Istanbul')
describe_city('Ankara')
describe_city('Paris', 'France')
