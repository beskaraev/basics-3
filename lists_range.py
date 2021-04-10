# 03/11/2021 - Lists (continue)

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
# Making Numerical list with range() functions
# range([start], stop, [step]) - Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive)


for num in range(4):
    print(f"number: {num}")
# shift + f6 - shortcut for Refactor>rename
# ctrl + Y - deletes the line

nums = range(4)  # this does not mean nums = [0, 1, 2, 3]
print(nums)

nums2 = list(range(4))  # this creates list data structure from sequence of numbers
print(nums2)
for num in nums2:
    print(num)
print(" range with start and stop ---")
for num in range(1, 4):
    print(num)

print(" range with start, stop and step ---")
for num in range(1, 20, 3):
    print(num)

print("Exercise1: print all even numbers from 1 to 16 (16 should be included)")

evens = []
for num in range(2, 17, 2):
    print(num)
    evens.append(num)
    print(evens)

print(f"This is the final list: {evens}")

print("Exercise2: print the squares of numbers from 10 to 20 ")
squares = list()
for num in range(10, 21):
    squares.append(num ** 2)
    # print(num*num)
print(f"final list: {squares}")
print(f"min(squares): {min(squares)}")
print(f"max(squares): {max(squares)}")
print(f"sum(squares): {sum(squares)}")

cars = ['bugatti', 'ferrari', 'tesla', 'lexus', 'bmw']
cars_len = len(cars)
for car in cars:
    print(car)
    print(f"index of the {car} is {cars.index(car)}")

print("looping the list using index ***************")
# for ind in range(len(cars)):
for ind in range(cars_len):
    print(ind)
    print(f"index of the {cars[ind]} is {ind}")

# ----------------
print("# List comprehension : ")
squares1 = list()
for num in range(10, 21):
    squares1.append(num ** 2)
print(squares1)

squares2 = [num ** 2 for num in range(10, 21)]  # for read only now, use later
print(squares2)  # both lists are identical since they have identical logic

print("Exercise 4-4, 4-5: One Million: ****************************")
nums = []
for num in range(1, 1000001):
    # print(num)
    nums.append(num)
# print(nums)
print(f"smallest : {min(nums)}")
print(f"biggest : {max(nums)}")
print(f"total : {sum(nums)}")
