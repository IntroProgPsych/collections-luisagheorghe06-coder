# https://www.w3schools.com/python/python_dictionaries.asp

#  You are given this dictionary:
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
#     "Spain": "Madrid"
# }
#
# Write a function get_capital(country, capitals_dict) that:
#   - returns the capital of the given country
#   - returns "Unknown" if the country is not in the dictionary
#
# Ask the user for a country name and print the returned value.
# 
# Write your code here:
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid"
}

def get_capital(country, capitals_dict):
    # The .get() method is perfect for this.
    # Syntax: dictionary.get(key_to_find, value_if_not_found)
    return capitals_dict.get(country, "Unknown")
user_country = input("Enter a country name: ")
capital = get_capital(user_country, capitals)
print(f"The capital is: {capital}")