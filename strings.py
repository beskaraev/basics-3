# 03/04/2021   String(str)

fullname = "john doe"
msg = "we are looking at string functions in python.        "

# # Functions available for string
# print(fullname)
# print(fullname.upper())
# print(fullname.lower())
# print(fullname.title())
# print(msg.replace('.', '!!!!!').title())
# print(msg.replace('python', 'java'))
print(f"fullname.isdigit() >> {fullname.isdigit()}")
print(f"fullname.islower() >> {fullname.islower()}")
print(f"fullname.isupper() >> {fullname.isupper()}")
print(f"467.isdigit() >> {'467'.isdigit()}")

# Concatenation
msg1 = fullname.title() + ", " + msg
print(msg1)
print(fullname.upper() + ", " + msg)

# working with whitespaces in string: \t, \n, etc
msg2 = fullname.upper() + "\n\t\t\t, " + msg
print(msg2)
msg3 = '\n\t\t\t' + fullname.upper() + ", " + msg
# str.strip() - removes leading and preceding whitespace
print(msg3 + '!!!')
print(msg3.strip() + '!!!')

# fstring
msg3 = fullname.upper() + ", " + msg
msg4 = f"     {fullname.title()}, {msg}   \t\n new word 'abc' 'bca'  "

print("fstring")
last_name = f'brown'
print(msg4 + '!!!')

print("Integers: ********************************")
num = 456
num2 = 600
# print(num.strip()) - strip() is only used for string data type

message = "One of Python's strengths is its diverse community."
# print(message)

print(f"num + num2 = {num + num2}")
print(f"num - num2 = {num - num2}")
print(f"num * num2 = {num * num2}")
print(f"num / num2 = {num / num2}")
# str(expression) - this will convert the data type to str
print("Value of num is : " + str(num))
print("num + num2 = " + str(num + num2))

num3 = "753"  # it is a string(str) not integer (int)
print(f"num + num3 = {num + int(num3)}")
# ctrl + click - will take you where the specific variable is defined.

print(f"3**2 = {3 ** 2}")  # 3**2 means 3*3 , or square of 3, '**' - exponent

num4 = "45.55"
print(f"num + num2 = {num + float(num4)}")

print(int(45.4988))

# Exercise 2-5:
print("# Exercise 2-5: ")
author = "Albert Einstein"
quote = f'\t\t\t{author} once said, “A person who never made a \n\t\t\tmistake never tried anything new.”'

print(quote)

# H/W : all in chapter 2
print(int(16 / 2))
