favorite_places = {
    'eric': ['New York', 'Los Angeles', 'Chicago'],
    'jim': ['San Francisco', 'Seattle', 'Boston'],
    'bob': ['Miami', 'Atlanta', 'New Orleans']
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")