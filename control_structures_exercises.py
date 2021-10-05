# 1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not

print("What is the day of the week?\n")

user_day = input("Enter day of the week: ")

day_of_the_week = "Monday"

while day_of_the_week != user_day:
    print("Thats Not the day of the week try again!\n")
    user_day = input("Enter here: ")

print("Thats right! It's Freaking monday!")

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

print("What is the day of the week?\n")

user_day = input("Enter day of the week: ")

if user_day == "Saturday" or user_day == "Sunday":
    print("This is a weekend! \n")
else:
    print("This is a weekday!")
# c. create variables and make up values for

#  - the number of hours worked in one week
hours_weekly = 40
#  - the hourly rate
hourly_rate = 30
#  - how much the week's paycheck will be
weeks_pay = hours_weekly * hourly_rate
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
clocked_in_hours = input("Enter your hours for the week: ")
clocked_in_hours = int(clocked_in_hours)
if clocked_in_hours > 40:
    r = clocked_in_hours % 40
    overtime = (r * 30) * 1.5

overtime_pay = weeks_pay + overtime

""""
2. Loop Basics

While

Create an integer variable i with a value of 5.
Create a while loop that runs so long as i is less than or equal to 15
Each loop iteration, output the current value of i, then increment i by one.
"""
i = 5

while i <= 15:
    print(i)
    i = i + 1

"""
Your output should look like this:


5
6
7
8
9
10
11
12
13
14
15
"""

"""
Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
Alter your loop to count backwards by 5's from 100 to -10.
Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

 2
 4
 16
 256
 65536
 """
 #1a
i = 0
while i in range(100):
    i = i + 2
    print(i)
#2a
i = 100
while i > -15:
    print(i)
    i = i - 5
#3a
i = 2
while i < 1000000:
    print(i)
    i = i*i
#4a
i = 100

while i > 0:
    print(i)
    i = i-5

 """"
Write a loop that uses print to create the output shown below.


100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
"""

"""
For Loops

Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

For example, if the user enters 7, your program should output:


7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
"""
user_number = input("Enter your number: ")
user_number = int(user_number)

for i in range(1, user_number+1):
    multiply = user_number * i
    table = "{} x {} = {}"
    print(table.format(user_number, i, multiply))
    



"""
Create a for loop that uses print to create the output shown below.


1
22
333
4444
55555
666666
7777777
88888888
999999999
"""
row = 9

for i in range(row+1):
    for j in range(i):
        print(i, end='')
    print("")

""""
4. break and continue

Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
(Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50,
 except for the number the user entered.

Your output should look like this:


Number to skip is: 27

Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
Here is an odd number: 7
Here is an odd number: 9
Here is an odd number: 11
Here is an odd number: 13
Here is an odd number: 15
Here is an odd number: 17
Here is an odd number: 19
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
Here is an odd number: 37
Here is an odd number: 39
Here is an odd number: 41
Here is an odd number: 43
Here is an odd number: 45
Here is an odd number: 47
Here is an odd number: 49



"""

user_odd_number  = input("Enter a odd number between 1 and 50: ")

while user_odd_number.isdigit() != True or int(user_odd_number) % 2 == 0 or int(user_odd_number) > 50 or int(user_odd_number) < 0:
    print("Not a valid number! \n")
    user_odd_number  = input("Enter a odd number between 1 and 50: ")

user_odd_number = int(user_odd_number)    
    
for i in range(1, 50+1):
   # if user_odd_number > 50 or user_odd_number < 0:
    #    break
    if i % 2 == 0:
        continue
    elif i == user_odd_number:
        print(f"Yikes skipping this number: {user_odd_number}")
    else:
        print(f'Here is an odd number: {i}') 






"""
The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive 
number and write a loop that counts from 0 to that number. 

(Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this 
to a numeric type.)

Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
"""
user_positive_number = input("Please input a even number: ")

while user_positive_number.isdigit() != True or int(user_positive_number) <= 0:
    print("This is not a positive number!")
    user_positive_number = input("Please input a even number: ")

user_positive_number = int(user_positive_number)

for i in range(user_positive_number+1):
    print(i)



user_positive_number2 = input("Enter a positive number: ")

while user_positive_number2.isdigit() != True or int(user_positive_number2) <= 0:
    print("This is not a positive number!")
    user_positive_number2 = input("Please input a even number: ")


user_positive_number2 = int(user_positive_number2)

i = 1
while user_positive_number2  >= i:
    print(user_positive_number2)
    user_positive_number2 = user_positive_number2 - i

""""
3. Fizzbuzz

One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic 
looping and conditional logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

"""

for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print("Fizz Buzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    




"""
Display a table of powers.
Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
Example Output

What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
"""
table_power_input = input("What number would you like ot go up to? ")

while table_power_input.isdigit() != True:
            print("Not a valid grade number!\n")
            table_power_input = input("Enter your number: ")

table_power_input = int(table_power_input)
consent = "y"

while consent != "n":

    print("\nHere is your table! \n")
    print("number  | squared |  cubed")
    print(" -----     ------    -----")

    for i in range(1, table_power_input+1):
        print("{:<3d}     |{:<3d}      |{:<3d}".format(i,i**2,i**3))

    consent = input("Want to try again? y/n: ")

    while consent != 'n' and consent !='y':
        print("Invalid consent number!\n")
        consent = input("Would you like to continue ? y/n ")
    
    if consent == "y":
        table_power_input = input("What number would you like ot go up to? ")

        while table_power_input.isdigit() != True:
            print("Not a valid grade number!\n")
            table_power_input = input("Enter your number: ")

        table_power_input = int(table_power_input)




"""
Bonus: Research python's format string specifiers to align the table

Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0


"""
grades_inputed_to_letter = input("Enter your grade: ")

while grades_inputed_to_letter.isdigit() != True or int(grades_inputed_to_letter) > 100 or int(grades_inputed_to_letter) < 0:
    print("Not a valid grade number!\n")
    grades_inputed_to_letter = input("Enter your grade: ")
    
grades_inputed_to_letter = int(grades_inputed_to_letter)


consent = "y"
    
while  consent != "n":
    if grades_inputed_to_letter > 97:
        print("A+")
    elif grades_inputed_to_letter > 93:
        print("A")
    elif grades_inputed_to_letter > 87:
        print("A-")
    elif grades_inputed_to_letter > 85:
        print("B+")
    elif grades_inputed_to_letter > 83:
        print("B")
    elif grades_inputed_to_letter > 79:
        print("B-")
    elif grades_inputed_to_letter > 75:
        print("C+")
    elif grades_inputed_to_letter > 70:
        print("C")
    elif grades_inputed_to_letter > 66:
        print("C-")
    elif grades_inputed_to_letter > 63:
        print("D+")
    elif grades_inputed_to_letter > 60:
        print("D")
    elif grades_inputed_to_letter > 59:
        print("D-")
    else:
        print("F")
    

    consent = input("Would you like to continue ? y/n ")
    
    while consent != 'n' and consent !='y':
        print("Invalid consent letter!\n")
        consent = input("Would you like to continue ? y/n ")

    if consent == "y":
        grades_inputed_to_letter = input("Enter your grade: ")
        
        while grades_inputed_to_letter.isdigit() != True or int(grades_inputed_to_letter) > 100 or int(grades_inputed_to_letter) < 0:
            print("Not a valid grade number!\n")
            grades_inputed_to_letter = input("Enter your grade: ")
            
        grades_inputed_to_letter = int(grades_inputed_to_letter)



"""
Bonus

Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
"""


"""
Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, 
author, and genre. Loop through the list and print out information about each book.

Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
"""

books = [{'title': 'Gunslinger', 'author': 'Stephen King', 'genre': 'Fantasy'},
           {'title': 'Eragon', 'author': 'cant remember', 'genre': 'Fantasy'},
           {'title': 'Harry Potter', 'author': 'That one crazy lady','genre': 'Magic'},
           {'title': 'Cthulu', 'author': 'HP', 'genre': 'Spooky'},
           {'title': 'Olympians', 'author': 'cool guy', 'genre': 'Gods'}]

input_genre = input("Enter a genre: ")

for i in books:
    if input_genre == i['genre']:
        print(i['title'])

#genre_entry = input("Enter a genre: ")

#for book in books:
    #if book['genre'] == genre_entry:
     #   print(f"{book['genre']}")
