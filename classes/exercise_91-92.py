class Restaurant1:
    """
    @author: Yulia
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} the best place if "
              f"you are looking for {self.cuisine_type} cuisine!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is open!")


my_res = Restaurant1("'Hello'", "russian")
print(my_res.restaurant_name)
print(my_res.cuisine_type)
my_res.describe_restaurant()
my_res.open_restaurant()


class Restaurant():
    """
    Restaurant should store two attributes: a restaurant_name and a cuisine_type.
    @author: Shabnam
    """

    def __init__(self, name, cuisine):
        self.name = name.title()
        self.cuisine = cuisine.title()

    def describe_restaurant(self):
        message = f"{self.name} serves wonderful {self.cuisine} ."
        print(f"\n{message}")

    def open_restaurant(self):
        message = f"{self.name} is now open!"
        print(f"\n{message}")


restaurant = Restaurant('Luigi', 'pizza')
restaurant.describe_restaurant()

applebees = Restaurant("applebees", 'salmon')
applebees.describe_restaurant()

captain_louies = Restaurant('captain louies', 'lobsters')
captain_louies.describe_restaurant()
