# 1. A List of Lists
# 2. A List of Dictionaries
# 3. A List in a Dictionary
# 4. A Dictionary in a Dictionary

print("")
countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = [companies, cities, countries]
print(customers)
print(customers[0])
print(customers[0][0])
print(f"printing barcelona: {customers[1][2]}")

multi_dim_nums = [
    [3, 9, 0],
    [2, 7, 1],
    [0, 1, 0, 2]
]
print(f"printing the middle value {multi_dim_nums[2][3]}")

print("Nested Loops: Looping through multidimensional list(array).")
for column in customers:
    print(column)
    # ['level up', 'abc company', 'ola company']
    for value in column:
        print(value.upper())

for city in customers[1]:
    print(city, end='\t')

# H/W print multiplication table

print("************* list of dictionaries *************")
user_0 = {'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 = {'name': 'mark', 'age': 35, 'city': 'tokyo'}

users = [user_1, user_0, user_2]

print(users[0])
print(users[2]['name'])
print(users[2]['age'])
print(users[2]['city'])

print("----- looping -------------")
for user in users:
    print(user['name'], end=' || ')
    print(user['age'], end=' || ')
    print(user['city'])

print("********** List in a Dictionary *******************")
countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = {
    'countries': ['usa', 'russia', 'spain'],
    'cities': ['new york', 'moscow', 'barcelona'],
    'companies': ['level up', 'abc company', 'ola company']
}

print(customers['cities'])
print(customers['cities'][1])  # second element from cities

print("********** Dictionary in a Dictionary ************")
user_0 = {'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 = {'name': 'mark', 'age': 35, 'city': 'tokyo'}

users = {
    'user_0': {'name': 'john', 'age': 25, 'city': 'brooklyn'},
    'user_1': {'name': 'jane', 'age': 20, 'city': 'paris'},
    'user_2': {'name': 'mark', 'age': 35, 'city': 'tokyo', 'fact': 'nerd'}
}

print(users)
print(users['user_0'])
print(users['user_0']['name'])
print(users['user_2']['city'])

# for user in users.keys():
#     print(user)
#     print(users[user])
for username, details in users.items():
    print(username)
    # print(details['name'])
    for key, value in details.items():
        print(f"details key is : {key}")
        print(f"details value is : {value}")

for username in users.keys():
    mySql_Create_Table_Query = f"insert into users (firstName, userAge) " \
            f"values(users[{username}]['name'], users[{username}]['age'])"
    # connect to db
    # execute the db
    #  you can read more details here: https://pynative.com/python-mysql-database-connection/
    # result = cursor.execute(mySql_Create_Table_Query)
    # [{
    #         "ProductName": "Chocolade",
    #         "TotalUnits": 138
    #     },
    #     {
    #         "ProductName": "Genen Shouyu",
    #         "TotalUnits": 122
    #     },
    #     {
    #         "ProductName": "Gravad lax",
    #         "TotalUnits": 125
    #     },
    #     {
    #         "ProductName": "Laughing Lumberjack Lager",
    #         "TotalUnits": 184
    #     },
    #     {
    #         "ProductName": "Mishi Kobe Niku",
    #         "TotalUnits": 95
    #     }
    # ]
    #
    # result[4]['ProductName'] # it will return "Mishi Kobe Niku"
    # result[4]['TotalUnits']
