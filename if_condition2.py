# 03/14/2021 If statements (continue)
num = 20

if num >= 1 and num <= 10:
    print(f"number is equal or greater than 1 and less than 10")
else:
    print(f"number is less than 1 or greater than 10.")

'''
expression AND/OR expression AND/OR expression

OR:
expression OR expression = True OR False = True
where country='UK' or country='USA'>> True or False >>

OR:
True or True = True
True or False = True
False or True = True
False or False = False

AND:
True and True = True
True and False = False
False and True = False
False and False = False
'''

# age = int(input('enter the visitors age: '))
age = 3
if 0 <= age <= 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
elif age < 140:
    print("Your admission cost is $10.")
else:
    print("Invalid age was entered, bye!")

# age = int(input('enter the visitors age: '))
age = 20
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 140:
    price = 10
else:
    print("Invalid age was entered, bye!")
print(f"Your admission cost is ${price}.")

# n , 0 < n < 2000000

'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
'''

print("5-3. Alien Colors #1: *****************")
# alien_color = input('enter the alien color (green/yellow/red): ')
alien_color = 'red'
if alien_color == 'green':
    print(f"You just earned 5 points!!")
elif alien_color == 'yellow':
    print(f"You just earned 2 points, whee!")
elif alien_color == 'red':
    print(f"you just earned 10 points, you are killing it, man!!")
else:
    print("no points, sorry, take a rest, meditate.")

# ----------------------
print("======================================")
friends = ()
if friends:
    print("good for you, can I be a friend.")
else:
    print(f"Go out make some friends, only good friends.")

print("******* Using Multiple Lists **************")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['Mushrooms ', 'french fries', '    extra Cheese']

for requested_topping in requested_toppings:
    if requested_topping.lower().strip() in available_toppings:
        print(f"I am adding {requested_topping.title().strip()}")
    else:
        print(f"Sorry we dont have {requested_topping.upper().strip()}")

# exercises:
# 1. FuzzBuzz, assume user enter then integer number>0
#   print Fuzz if the number is dividable by 3
#   print Buzz if the number is dividable by 5
#   print FuzzBuzz if the number is dividable by 3 and 5
# % - modulus - operator to return remainder in division
# // - floor division - division ignoring the remainder and considering only dividable num
# num % 5 == 0 - calculates num%5 and returns a remainder, and that remainder is compared to 0, which means if remainder is 0 num is devidable by 5 without any remainder.


num = int(input("enter the number > 0 :"))
if (num % 3 == 0) and (num % 5 == 0):
    print(f"FuzzBuzz your number {num} dividable by 3 and 5")
elif num % 3 == 0:
    print(f"Fuzz your number {num} dividable by 3")
elif num % 5 == 0:
    print(f"Buzz your number {num} dividable by 5")

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 != 0:
    print ("Fuzz")
elif number % 5 == 0 and number % 3 != 0:
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0:
    print("FuzzBuzz")

# H/w:
# Implement sum() with for loop
# Double characters in a string (e.g. “abc” => “aabbcc”)
# for letter in "hello":
#     print(letter)
# Prove that a number is a prime
# Prove that a string is a palindrome (mom, dad, madam, kayak etc)

# Exercise 5-10
current_users = ['mary', 'stanley', 'joseph', 'jennifer', 'Admin']
new_users = ['sam', 'stanley', 'Mathew', 'mia', 'jennifer']
# current_users_lower =[user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")
