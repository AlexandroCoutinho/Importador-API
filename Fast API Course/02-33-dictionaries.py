"""
Dictionaries
"""
print()
print("Initial dictionary")
user_dictionary = {
    "username": "codingwithroby",
    "name": "Eric",
    "age": 32
}
print(user_dictionary)

print()
print("Print username only")
print(user_dictionary.get("username"))

print()
print("Adding Marital Status")
user_dictionary["married"]= True
print(user_dictionary)

print()
print("Removing Age")
user_dictionary.pop("age")
print(user_dictionary)
