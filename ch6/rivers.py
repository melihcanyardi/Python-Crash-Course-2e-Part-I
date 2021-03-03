rivers = {'nile': 'egypt', 'amazon': 'peru', 'yangtze': 'china'}

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
