# 03/18/2021 Dictionary - java (HashMap, HashTable)

# key/value pair data structure, since each element comes as (key: value)
# Create, access, modify (add/remove/update elements)
# looping this data structure
# some mostly used builtin functions,

my_friend = {}
my_house = dict()
my_car = {"brand": "Ford", "model": "Mustang", "year": 1964, 1: 'value of 1'}

print(my_car)
print(my_car['brand'])
print(f"the value of key 'brand' is: {my_car['brand']}.")
print(my_car[1])  # this is not an index, my_car has key=1

# adding new element
my_car['price'] = 125000.00
print("price is added -------------")
print(my_car)

# updating the value in dictionary
print("price was updated ---------------")
my_car['price'] = 120000.00
print(my_car)

# removing the values from dictionary
print("element with key 1 is being removed -----------")
del my_car[1]
print(my_car)

print("Exercise 6-1: ---------------------")
"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""

amigo = {'first_name': 'Vitaly', 'last_name': 'Didkivsky', 'age': 19, 'city': 'Florence'}

print(amigo['first_name'])
print(f"my friend's first name is : \n\t\t{amigo['first_name']}")
print(f"my friend's last name is : {amigo['last_name']}")
print(f"my friend is {amigo['age']} years old.")
print(f"my friend lives in : {amigo['city']}")

# H/W: 6-2. Favorite Numbers:
# H/W: 6-3. Glossary:
