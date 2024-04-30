country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # Create list from formatted ..

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
  
]

def add_new_country(country, visits, list_of_cities):
    new_entry = {}
    new_entry["country"] = country
    new_entry["visits"] = visits
    new_entry["cities"] = list_of_cities
    travel_log.append(new_entry)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")

