# 03/21/2021 While loop, Functions

print("** incrementing the variable to reach upper boundary")
current_number = 10
while current_number <= 5:
    print(current_number)
    current_number += 1

print("** decrementing the variable to reach lower boundary")
current_number = 1
while current_number >= 5:
    print("Iteration -----")
    print(current_number)
    current_number -= 1
    print(current_number)

print("******** Game Started ************")
# enter colors , green - 15, yellow - 10, red - 5
# other colors or something you loose
# q or quit is to end the game

color = None
while color != 'quit' or color != 'q':
    color = input("Enter your color (green/yellow/red): ")
    color = color.lower().strip()
    points = 0
    if color == 'quit' or color == 'q':
        break
    elif color == 'green':
        points = 15
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points = 5
    else:
        print("Sorry, that's not right color. You lost ;)")
    print(f"You have {points} points.")
print("closing the game...")

# 'hello guys'

count = 0
for letter in 'hello guys':
    if letter == 'l':
        count += 1
print(f"number of l's is : {count}")