# If statements:
# if expression:
#     code here when expression is true
# else:
#     code here when expression is false
#

# num1_str = input("enter the num1: ")
# num1 = int(num1_str)
num1 = int(input("enter the num1: "))
num2 = 3
# if num1 < num2:
if num1 == num2:  # comparing 2 values using ==
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")
print("if statement completed here")

print(" ------ second ---------")
# msg = True
num = input("enter True/False: ")
if num:
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")

print(" ------ third ---------")
# msg = 0 # this is considered as false expression
num = 5  # this is considered as True expression
if num:
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")

print(" ------ fourth ---------")
num = 0  # this is considered as True expression
if num in range(5):
    print("expression is true, and num is within range")
    print("you can do something here")
else:
    print("expression is false")

print(" ------ fifth ---------")
num = 0  # this is considered as True expression
if num not in range(5):
    print("expression is true, and num is within range")
    print("you can do something here")
else:
    print("expression is false")

print(" ------ sixth ---------")
msg = input("enter the message: ")
if msg.strip() != '':
    print("whitespace was entered")
else:
    print(f"this message was entered: \n'{msg}'")

if msg.strip() == '':
    print(f"this message was entered: \n'{msg}'")
else:
    print("whitespace was entered")

print("----- Comparing the string values ---------")
name = input('Please enter your name')
if name.strip().lower() == 'john doe':
    print(f"We have missed you {name}")
else:
    print(f"Welcome {name}")

print("-- if statement with lists --- ")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
if 'tesla' in cars:
    print("yes, we have tesla in stock.")
else:
    print("sorry we dont have this car.")

print("-- if statement with strings --- ")
if 'sat' in "today is saturday":
    print("yes, it is part of the string.")
else:
    print("no it is not part of the string")

print("-- if statement with lists and looping --- ")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars:
    if car == 'tesla':
        print(f"This is {car.upper()}")
        break
    else:
        print(f"current car is {car.title()}")

print("exercise: ----------------- ")
nums = [45, 4, 5, 6, 3, 10, 5, 123, 346, 4, 5, 666, 5]
# print values but when you find 5 , print it and print 'completed'
for num in nums:
    if num == 5:
        print(num, 'completed')
        break
    else:
        print(num, "is not 5")
# H/w : Count how many 5s you have in the list
# hint: use additional variable to save the counts and keep incrementing it every time you encounter the 5 in the list
count = 0  # it should be declared before and outside of for-loop
count = count + 1  # count += 1 incrementing count by 1 every time

nums = [45, 4, 5, 6, 3, 10, 5, 123, 346, 4, 5, 666, 5]
cnt = 0
for num in nums:
    if num == 5:
        cnt = cnt + 1    # cnt += 1
print(cnt)
