# 03/25/2021

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""


def favorite_book(book_title: str):
    print(f"One of my favorite books is '{book_title.upper()}'....")


def test_function(par1: str):
    print(f"hello {par1.lower()}")


favorite_book("Sun also rises")


# function that prints multiplication of 2 numbers
def multi_num(a: int, b: int):
    c = a * b
    print(f"product of {a} and {b} is {c}.")


"""
public void multi_num(int a, int b)
    {
    int c = a * b
    print(f"product of {a} and {b} is {c}.")
    }
"""

multi_num(5, 6)
multi_num(0, 6)
# multi_num('a', 'bob') # TypeError: can't multiply sequence by non-int of type 'str'
multi_num(4.5, 5.666)
# multi_num(4.5, 5.666, 34) # TypeError: multi_num() takes 2 positional arguments but 3 were given
# multi_num(4.5) # TypeError: multi_num() missing 1 required positional argument: 'b'
multi_num(True, True)
multi_num(True, False)

# multi_num([2, 3, 55, 0], [1, 2, 1, 1]) # TypeError: can't multiply sequence by non-int of type 'list'
# multi_num('\n', '\t')  # TypeError: can't multiply sequence by non-int of type 'str'
# multi_num('', 'sd')


a = 45
b = 78

temp = a
# a is 45
# b is 78
# temp is 45

a = b
# a is 78
# b is 78
# temp is 45

b = temp
# a is 78
# b is 45
# temp is 45


print("the value a : {}".format(a))
print("the value b : {}".format(b))


def swap(a, b):
    print(f"the value of a is: {a}")
    print(f"the value of b is: {b}")
    # logic here
    temp = a
    a = b
    b = temp
    print(f"the value of a is: {a}")
    print(f"the value of b is: {b}")

swap(546, 1234)

# swapping the values without using a variable
print("___________________________________")
num1 = 'number one'
num2 = 'number two'
print(num1,"---",  num2)
num1, num2 = num2, num1
print(num1,"---",  num2)

