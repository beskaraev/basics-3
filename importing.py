# 03/27/2021 Importing the modules


import sys
# import time
from time import *

from functions.functions_return import *
# import functions.functions_return as ft
# import functions.functions_return


print(sys.platform)
sleep(5)  # use this when you 'from time import *'
# time.sleep(5) # use this when 'import time'

print_formatted_name("akmal", 'husanov') # if from functions.functions_return import *
# ft.print_formatted_name("akmal", 'husanov') # if import functions.functions_return as ft
# functions.functions_return.print_formatted_name("akmal", 'husanov') # if # import functions.functions_return


full_name = get_formatted_name('john', 'doe')
print(full_name)
print(get_formatted_name('jane', 'doe'))

print_formatted_name('ali', 'tehrani')
student = print_formatted_name('baur', 'eskara')
print(f"value of student is : {student}")
print(f"value of student is : {print_formatted_name('baur', 'eskara')}")

print(get_list_of_even_numbers(20))

print_usernames(['karim', 'ronaldo', 'roger'])
