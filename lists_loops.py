# Loops - process of iterating, going through the elements
# Flow control
# syntax in python language (for loop):

# for temp_variable in iterable(list):
#     some code to execute repetitively
#     some code to execute repetitively
#     some code to execute repetitively
#     some code to execute repetitively
#     some code to execute repetitively
#     some code to execute repetitively

# some code to execute outside of for loop

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
print("********* Exercises: 3-3 *********************")
# car = 'zaparaj'

for car in cars:
    print(f"I would like to own a {car.title()} car.")

print("This dreaming help me to motivate and work harder.")
print(car)
# print(f"I would like to own a {cars[1].title()} car.")
# print(f"I would like to own a {cars[2].title()} car.")
# print(f"I would like to own a {cars[3].title()} car.")

# java example that is not sensitive to spaces but requires {}
# for car in cars {
#     print(f"I would like to own a {car.title()} car.")
#     print(f"I would like to own a {car.title()} car.")
#    print(f"I would like to own a {car.title()} car.")
# }
# scope of your variable - life of your variable
