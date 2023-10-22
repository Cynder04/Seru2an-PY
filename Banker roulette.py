"""
You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names.
For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
"""

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_index = len(names)
names_pay = random.randint(0, names_index - 1)
person_pay = names[names_pay]
print(f"{person_pay} is going to buy the meal today!")