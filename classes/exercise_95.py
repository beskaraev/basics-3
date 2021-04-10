# H/W:
# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User:
    login_attempts = 0

    def __init__(self):
        pass  # pass means do nothing, it is just place holder
        # self.login_attempts = 0 # this is the alternate way of creating global variable

    def increment_login_attempts(self):
        print("incrementing the value by 1 ...")
        self.login_attempts += 1

    def reset_login_attempts(self):
        print("resetting the value to 0 ...")
        self.login_attempts = 0


user1 = User()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts: ", user1.login_attempts)
user1.reset_login_attempts()
print("Login attempts: ", user1.login_attempts)
