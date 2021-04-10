print()
print('----------------')
print("# 9-3 Users: Make a class called User")


class User:
    """
    @author: Sergey
    """

    def __init__(self, first_name, last_name, occupation, address, phone=""):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.address = address
        self.phone = phone

    def describe_user(self):
        """print summary of user info"""
        print(f"User profile details: \n\t{self.first_name.title()} {self.last_name.title()}")
        # print(self.first_name.title())
        # print(self.last_name.title())
        print(f"Occupation: {self.occupation}")
        print(f"Address: {self.address}")
        print(f"Phone number: {self.phone}")

    def greet_user(self):
        """Print personalized greeting to a user"""
        print(f"Hello {self.first_name.title()}, nice to see you!")


# create several instances, and use both methods for each:
person1 = User("tom", "jefferson", "programmer", "NYC", "212-0000")
person2 = User("george", "jefferson", "programmer", "NYC", "212-0000")
person3 = User("jessica", "thomson", "programmer", "NYC", "212-0000")
person4 = User("jessica", "thomson", "programmer", "NYC")

person1.describe_user()
person2.describe_user()
person3.describe_user()

person1.greet_user()
person2.greet_user()
person3.greet_user()

print()
print('----------------')
