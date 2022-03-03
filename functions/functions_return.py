# 03/25/2021  Functions with return statement

def get_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    return name


def print_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    print(name)


# full_name = get_formatted_name('john', 'doe')
# print(full_name)
# print(get_formatted_name('jane', 'doe'))
#
# print_formatted_name('ali', 'tehrani')
# student = print_formatted_name('John', 'Smith')
# print(f"value of student is : {student}")
# print(f"value of student is : {print_formatted_name('John', 'Smith')}")


# getter, setter functions
def get_desc_of_what_you_want_to_get():
    # logic
    return


def set_desc_of_what_you_want_to_update():
    pass


def get_list_of_even_numbers(num: int) -> list:
    """
    This funciton returns list of even numbers up to num (inclusive).
    :param num:
    :return:
    """
    # return [range(2, num + 1, 2)]
    return list(range(2, num + 1, 2))


# print(get_list_of_even_numbers(20))


# print(get_list_of_even_numbers("20"))


def get_list_of_odd_numbers(num):
    """
    This function returns list of odd numbers up to num (inclusive).
    :param num:
    :return: list
    """
    odds = []
    # logic here
    return odds


def get_letter_counts(text: str) -> dict:
    """
    This function returns a dictionary with letters as keys and counts as values
    """
    letter_count = {}
    # - loop through the text
    # - create a dictionary for this letters
    # - add each letter to the dictionary as a key and count (starting from 0) as a value
    # - every time you add a letter to a dictionary check if dictionary has the same key, if dictionary has a key you increment the valeu
    # if dictionary does not have you create new element and value = 1
    # a: 1+1, d: 1+1, e: 1
    return letter_count


def print_usernames(users: list):
    for user in users:
        print(f"current user is : {user}")


# print_usernames(['karim', 'ronaldo', 'roger']) # users = ['karim', 'ronaldo', 'roger']
