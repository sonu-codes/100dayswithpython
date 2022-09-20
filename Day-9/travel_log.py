# 9.2 : Dictionaries in list

travel_log = [
    {
        "country" :"India",
        "city_visited" : ["Mumbai", "Kolkata", "Delhi"],
        "total_visit" : 4
    },
    {
        "country" : "UAE",
        "city_visited" : ["Dubai", "Sarjah", "Qwait"],
        "total_vist" : 3
    },
]

# Add a new travel vist details
def add_new_vist (country, vist_total, city_list):
    new_entry = {}
    new_entry["country"] = country
    new_entry["city_visited"] = city_list
    new_entry["total_visit"] = vist_total
    travel_log.append(new_entry)

add_new_vist("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
