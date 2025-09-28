"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""

def create_dictionary(first_name, last_name, age):
    dictionary = {}
    dictionary["first_name"] = first_name
    dictionary["last_name"] = last_name
    dictionary["age"] = age
    return dictionary

dictionary = create_dictionary("Alexandro", "Coutinho", 38)
print(dictionary)
