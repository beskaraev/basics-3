# 03/13/2021
# Working with part of the list
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']

# slice of the list list_name[start:stop] - start is inclusive, stop is exclusive values
# values: list_name[start], list_name[start+1] , ... , list_name[stop-1]
print("------ Slicing: first -------------")
for car in cars[1:3]:
    print(f"the car is : {car}")

print("------ second -------------")
for car in cars[:3]:  # the same thing as cars[0:3]
    print(f"the car is : {car}")

print("------ third -------------")
for car in cars[2:]:  # the same thing as cars[2:endofthelist]
    print(f"the car is : {car}")

print("------ fourth -------------")
for car in cars[2:10]:  # no Index out of range error
    print(f"the car is : {car}")

print("------ copying and linking -------------")
print("------ linking the 2 variable to the same value -------------")
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
cars.append('bmw')
print(f"cars after update: {cars}")
print(f"cars2 after update: {cars2}")

print("------ copying -------------")
cars3 = cars[:]
print(f"cars: {cars}")
print(f"cars3: {cars3}")
cars.append('toyota')
# del cars[2]
print(f"cars: {cars}")
print(f"cars3: {cars3}")

print("Exercise 4-10: slicing")
print(f"The first three items in the list are: {cars[:3]}")
print(f"Three items from the middle of the list are: {cars[2:5]}")
print(f"The last three items in the list are: {cars[3:]}")

# Lists can be modified (mutable)
# Tuples - data structure similar to list but can not be modified (immutable)
cars_t = ('bugatti', 'ferrari', 'tesla', 'lexus')
print(f"first value is : {cars_t[0]}")
cars[0] = 'honda'  # this is possible since cars is the list data structure
# cars_t[0] = 'honda' # this is not possible since the cars_t is tuple d/s
print(f"cars_t tuple: {cars_t}")

cars_t = ('honda', 'ferrari', 'tesla')
print(f"cars_t tuple: {cars_t}")
print(f"size of the tuple: {len(cars_t)}")
