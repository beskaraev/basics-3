# 04/03/2021 : # This file is for executing the cars.py classes
from classes.cars import Car, ElectricCar

# Execution
# greet_user()
# drive()
# drive() we will not have an access to this function yet

# mycar = Car()  # Car is the class, mycar is an object, in this line we are creating instance of the (instantiation)

mycar = Car("BMW", "530xi", "black")
yourcar = Car("Lexus", "lexus IS", "silver")

print("==================================")
mycar.get_description()
mycar.drive()
mycar.set_odometer_reader(50)
mycar.set_odometer_reader(60)
mycar.set_odometer_reader(25)
mycar.__odo_reader = 20  # this is the direct access to the instance variables
mycar.color = 'RED'  # this is the direct access to the instance variables
mycar.get_description()
# yourcar.do_something()
print("==================================")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()
print("============== increment ===================")
yourcar.increment_odometer_reader(25)
yourcar.get_description()
yourcar.increment_odometer_reader(-10)
yourcar.get_description()
# your car.increment_odometer_reader("25")  # this line will not execute, Exit code is 1 (error)
# yourcar.get_description()

# 04/03/2021
print("--- Electric car instances --------------")
# my_ev = ElectricCar("tesla", 'model x', 'blue') this is also good
my_ev = ElectricCar("tesla", 'model x', 'blue', 100)
my_ev.drive()
my_ev.get_description()
print('Battery size : ', my_ev.battery_size)
# mycar.battery_size # only child has battery_size attribute, parent does not see that attribute
# Car (state, behaviour) -> ElectricCar(state, behaviour)

# - we can create new methods(functions, available to child only)
my_ev.get_battery_info()

# - we can override the method that parent had (OOPs - Method Overriding)
my_ev.get_description()
mycar.drive()
my_ev.drive()

# HW: all exercises from chapter 9 (9-1 to 9-9)













