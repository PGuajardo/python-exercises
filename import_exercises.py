# 1) Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
"""
a.) Run an interactive python session and import the module. Call the is_vowel function using the . syntax.

b.) Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. 
 Call this function with values you choose and print the result.

c.)Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. 
Test this function in your notebook.


### Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.
"""

import function_exercises as fe
print(fe.is_vowel("o"))
#-----------
#-----------
#-----------
from function_exercises import calculate_tip as ct
print(ct(.40,20))
#-----------
#-----------
#-----------
from function_exercises import get_letter_grade as glg
glg(99)
#-----------
#-----------
#-----------
# 2) Read about and use the itertools module from the python standard library to help you solve the following problems:

"""
How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
How many different combinations are there of 2 letters from "abcd"?
How many different permutations are there of 2 letters from "abcd"?
"""
#-----------
#-----------
#-----------
from itertools import combinations as comb, permutations as permu, product as pro
#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# Must be put in a list, to call as interger set "123" = [1,2,3]
print(list(pro("abc", [1,2,3])))


print("\n")


print(len(list(pro("abc", "123"))))
print("\n")

# In the for loop we can print it line by line the combinations of the "abc" and "123"
for i in pro("abc", "123"):
    print(i)


#-----------
#-----------
#-----------
# How many different combinations are there of 2 letters from "abcd"?


print(list(comb("abcd", 2)))
print("\n")

print("There are this many combinations: ",len(list(comb("abcd",2))))
print("\n")

for k in comb("abcd", 2):
    print(k)

#-----------
#-----------
#-----------
print(list(permu("abcd", 2)))
print("\n")

print("There are this many permutations: ", len(list(permu("abcd", 2))))


# 3) Save this file as profiles.json inside of your exercises directory (right click -> save file as...).

"""
Use the load function from the json module to open this file.

import json

json.load(open('profiles.json'))
Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

Total number of users
Number of active users
Number of inactive users
Grand total of balances for all users
Average balance per user
User with the lowest balance
User with the highest balance
Most common favorite fruit
Least most common favorite fruit
Total number of unread messages for all users
"""
# Total number of users
# --------------------
import json

JL = json.load(open('profiles.json')) 


amount_users = []

for i in JL:
    amount_users.append(i["_id"])
    
print("Total number of users: ", len(amount_users))


# Number of active users
# --------------------

number_active = []

for k in JL:
    if k["isActive"] == True:
        number_active.append(k["isActive"])

print("Number of active users: ", len(number_active))

# Number of inactive users
# --------------------

number_inactive = []

for k in JL:
    if k["isActive"] == False:
        number_inactive.append(k["isActive"])

print("Number of inactive users: ", len(number_inactive))

# Grand total of balances for all users
# --------------------
from function_exercises import normalize_name as nn

grand_balance = []


for amount in JL:
    # Remove dollar sign and comma
    amount = nn(amount["balance"])
    
    # Turn into a float now
    turn_into_int = float(amount)
    grand_balance.append(turn_into_int)
    
print("Grand total of balances for all users: ", sum(grand_balance))

# Average balance per user
# --------------------

import statistics
print("Grand total of balances for all users: ", statistics.mean(grand_balance))

#User with the lowest balance
# --------------------

print(min(grand_balance))

#User with the highest balance
# --------------------

print(max(grand_balance))


#Most common favorite fruit
# --------------------

list_of_favorites = []

for fruit in JL:
    
    fruit = fruit["favoriteFruit"]
    list_of_favorites.append(fruit)
    
print(list(list_of_favorites))


from collections import Counter


counting = Counter(list_of_favorites)

print("\nThe most common fruit is: ", counting.most_common()[0])

# --------------------
#Least most common favorite fruit
# --------------------

print("\nThe least most common fruit is: ", counting.most_common()[-1])


#Total number of unread messages for all users


list_of_unread = []

total_of_unread = []

for unread in JL:
    
    unread = unread["greeting"]
    list_of_unread.append(unread)

print("This is the list of messages: \n", list(list_of_unread))

for takingoutDigit in list_of_unread:
    for split_number in takingoutDigit.split():
        if split_number.isdigit():
            total_of_unread.append(int(split_number))

#unread_sum = sum(total_of_unread)
print("\n")

print("\n Total of unread messages: ",sum(total_of_unread))