# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to 
# hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = []
for i in fruits:
    uppercased_fruits.append(i.upper())

uppercased_fruits

# OR

uppercased_fruits = [fruits.upper() for fruit in fruits]
uppercased_fruits

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like 
# ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = []
for i in fruits:
    capitalized_fruits.append(i.title())

capitalized_fruits

# OR

capitalized_fruits = [fruits.title() for fruit in fruits]
capitalized_fruits

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.

fruits_with_more_than_two_vowels = []

vowels = set('aeiou')
# counter to counts vowels
c = 0
# counter to count first item
word = 0
# counter for word with 2 letters i it
extra_word = 0

for i in fruits:
    word = word + 1
    for k in i:
        if k in vowels and (extra_word == word):
            c = c + 1
            if c > 2:
                fruits_with_more_than_two_vowels.append(i)
                extra_word = extra_word + 1

fruits_with_more_than_two_vowels

# OR

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (len([letter for letter in fruit if letter.lower() in 'aeiou'])> 2)]
fruits_with_more_than_two_vowels

fruits_with_more_than_two_vowels = fruits
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = []

vowels = set('aeiou')
c = 0
    
for i in fruits:
    for k in i:
        if k in vowels:
            c = c + 1
            if c == 2:
                fruits_with_only_two_vowels.append(i)

fruits_with_only_two_vowels

# OR 

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (len([letter for letter in fruit if letter.lower() in 'aeiou']) == 2)]
fruits_with_more_than_two_vowels

# Exercise 5 - make a list that contains each fruit with more than 5 characters

five_letter_fruit = []

for i in fruits:
        if len(i) > 5:
            five_letter_fruit.append(i)

five_letter_fruit

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

exact_five_letter_fruit = []

for i in fruits:
        if len(i) == 5:
            exact_five_letter_fruit.append(i)

exact_five_letter_fruit

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

less_five_letter_fruits = []

for i in fruits:
    if len(i) < 5:
        less_five_letter_fruits.append(i)

less_five_letter_fruits

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

length_of_char_fruits = []

for i in fruits:
    c = len(i)
    length_of_char_fruits.append(c)

less_five_letter_fruits

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain 
# the letter "a"

fruits_with_letter_a = []

c = set('a')

for i in fruits:
    for c in i:
        if c == 'a':
            fruits_with_letter_a.append(i)

fruits_with_letter_a


# OR

def contains_a(fruit):
    
    return len([letter for letter in fruit if letter == 'a']) > 0

fruits_with_letter_a = [fruit for fruit in fruits if contains_a(fruit)] #if true goes through if false it does not

fruits_with_letter_a

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

even_number = [number for number in numbers if (number % 2 == 0)]
even_number

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_number = [number for number in numbers if number % 2 != 0]
odd_number

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_num = [number for number in numbers if number > 0]
positive_num

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_num = [number for number in numbers if number < 0]
negative_num

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

[number for number in numbers if len(str(abs(number))) >= 2]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared.
#  Output is [4, 9, 16, etc...]

numbers_squared = [number**2 for number in numbers]
numbers_squared

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_num = [number for number in numbers if (number % 2 != 0) and (number < 0)]
odd_negative_num

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers_plus_5 = [number + 5 for number in numbers]
numbers_plus_5

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
 
 def is_prime(number):
    if number <= 0:
        return False
    else:
        dividers = [r for r in range(2, number)]
        return (len([divider in dividers if (number % divider == 0)]) == 0)
    
[number for number in numbers if is_prime(number)]
