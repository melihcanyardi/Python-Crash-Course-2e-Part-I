def city_country(city, country):
    """Returns city and its country neatly formatted."""
    return f"{city.title()}, {country.title()}"


print(city_country('istanbul', 'turkey'))
print(city_country('berlin', 'germany'))
print(city_country('paris', 'france'))
