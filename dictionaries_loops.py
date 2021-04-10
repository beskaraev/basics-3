# 03/20/2021 Looping through Dictionary

my_car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in my_car:
    print("--------------------------------")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is : {my_car[key]}")

print("- 2. using dict.keys() --------------------")
for key in my_car.keys():
    print("------ --------------------------")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is : {my_car[key]}")

# if 'model' in my_car.keys():
if 'model' in my_car:
    print(f"Yes my_car desc contains model information")

print("- 3. using dict.values() ---------------------")
for value in my_car.values():
    print("--------------------------------")
    print(f"value in this iteration is: {value}")
    # print(f"value of this key is : {my_car[value]}")

print("- 4. using dict.items() ---------------------")
for key, value in my_car.items():
    print("--------------------------------")
    print(f"val1 in this iteration is: {key}")
    print(f"val2 of this key is : {value}")

if 1964 in my_car.values():
    print(f"Yes my_car desc contains 1964 information")

print("**** example with list sort(), sorted(list) **************")
friends = ['john', 'jane']

print(friends)
sorted_friends = sorted(friends)
friends.sort()  # can not assign to variable since it sorts original list and does not return anything that can be assigned
print(sorted_friends)
print(friends)

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
print("******* sorted list ***********************")
for name in sorted(favorite_languages.keys()):
    print(f"{name}'s favorite language is {favorite_languages[name]}")

print(" **********  exercise 6-5 *******************")
"""6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
"""

rivers = {'nile': 'egypt', 'tigres': 'iraq', 'amazon': 'brazil', 'mississippi': 'usa'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# H/W 6-6. Polling:
