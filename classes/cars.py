# 03/28/2021 Object-oriented Programming Concepts: Class and Object

class Car:
    """This class describes model of the car."""

    def __init__(self, brand, model, color):
        """this is the constructor, with required parameters."""
        self.brand = brand  # assigning the local brand variable to a global variable (self.brand)
        self.model = model
        self.color = color
        self.__odo_reader = 0  # encapsulation - hiding data from object(users)

    def set_odometer_reader(self, miles):
        """Function to update the value of the odo_reader global variable."""
        if miles > self.__odo_reader:
            self.__odo_reader = miles
        else:
            print("miles can not be less than odometer miles.")

    def increment_odometer_reader(self, miles: int):
        """Function to increment the value of the odo_reader global variable."""
        if miles > 0:
            self.__odo_reader += miles
            # self.__odo_reader = self.__odo_reader + miles
        else:
            print("Expected positive value for miles, negative is entered.")

    def drive(self):
        """driving action"""
        if self.brand.lower() == "bmw":
            print(f"You are driving FAST car even without DL! isn't it awesome!")
        else:
            print(f"You are driving the car even without DL! isn't it awesome!")

    def do_something(self):
        print("I want to do something .....")
        print("let me drive this car ;) ")
        self.drive()
        # motor = Motorcycle()
        # motor.drive()

    def get_description(self):
        """ """
        # print(f"Brand of the car: {self.model}") # we are using here local variable that is only inside __init__ method
        # greet_user()
        print(f"Model of the car: {self.model}")
        print(f"Color of the car: {self.color}")
        print(f"Brand of the car: {self.brand}")
        print(f"You have {self.__odo_reader} miles on your car.")


def greet_user():
    print("hello master!")


class ElectricCar(Car):
    """This is the child class of Car. ElectricCar class inherits from Car class."""

    def __init__(self, brand, model, color, battery_size=60):
        """this is the constructor, with required parameters."""
        super().__init__(brand, model, color)
        self.battery_size = battery_size

    def get_battery_info(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_description(self):
        super().get_description()
        print(f"Battery size of the car: {self.battery_size}")

    def drive(self):
        print("You are driving EV! it is way awesome than just a car, maybe")


class A:

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"name: {self.name}")


class B(A):
    """
    old and stable code is in A class. B class is working copy of A for April changes
    """

    def __init__(self, name):
        super().__init__(name)

