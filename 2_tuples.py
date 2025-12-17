# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_tuples_unpack.asp

# You are given the following tuple:
# person = ("Alice", 21)
#
# Write a function print_person(info) that:
#   - unpacks the tuple into name and age
#   - prints: "Alice is 21 years old."
#
# Call the function with person.

# Write your code here:
person = ("Alice", 21)
def print_person(info):
    (name, age) = info
    print(f"{name} is {age} years old.")
print_person(person)