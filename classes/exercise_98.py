class Userlog:
    def __init__(self, first_name, last_name, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.age = age

    def describe_user(self):
        print(f"Meet our guest {self.first_name + ' ' + self.last_name}!"
              f"\n{self.first_name} is {self.age} and lives in {self.country}")

    def greet_user(self):
        print(f"Welcome {self.first_name + ' ' + self.last_name}")


class Privileges:
    def __init__(self, privileges):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"The user has following privileges: {self.privileges}")


class Admin(Userlog):
    def __init__(self, first_name, last_name, country, age):
        super().__init__(first_name, last_name, country, age)
        self.privileges = Privileges()
