# Exception Handling - handle situations where you expect certain type of error

filepath = "C:/dev/2020-fall/basics/data1/students.txt"

try:
    print('trying block started....')
    with open(filepath, 'a') as students:
        print("writing to the file.. ")
        students.write(f"\nSergey")

    with open(filepath, 'r') as students:
        lines = students.readlines()
        print(lines)

except FileNotFoundError as err:
    print(err)
    print("Enter correct file path. check your file path.")

# print(5/0)

try:
    num = 5 / int(input('enter the number to divide by: '))
except ZeroDivisionError as err:
    print('You can not divide by zero')
else:  # this is dependant on try block, if try block executes else block will be executed
    print('***** this is else block')
    print(f"Result of this division : {num}")
finally:
    print("I am a Finally block, I am always executed whatever happens with try, except or else block.")

print("Program is completed!!")
