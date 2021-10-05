
# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == 2 or x == '2':
        return True

print(is_two(2))
print(is_two('2'))
print(is_two(5))

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(x):
    vowels = set('aeiouAEIOU')
    
    if x in vowels:
        return True
    else:
        return False

print(is_vowel("o"))
print(is_vowel("z")) 


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonat(x):

    if is_vowel(x) != True:
        return True
    else:
        return False

print(is_consonat("a"))
print(is_consonat("z"))

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def is_capital_first_word(x):

    x = x.lower()
    if is_consonat(x[0]) == True:
        print(x.capitalize())
    else:
        print(x)

is_capital_first_word("zebra")
is_capital_first_word("owl")

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(x, y):
    total = ((x+1) * y) 
    tip_amount = total - y
    return tip_amount

calculate_tip(.25, 40)


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(x,y):
    discount_perc = (y/100)
    discount = x * discount_perc
    return discount

apply_discount(50,25)


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(x):
    x = x.replace(",", "")

    return int(x) 

handle_commas("787,,3")

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    while not x >= 100 and not x < 0:
        if x > 90:
            return print("A")
        elif x > 80:
            return print("B")
        elif x > 70:
            return print("C")
        elif x > 60:
            return print("D")
        else:
            return print("F")

get_letter_grade(99)
get_letter_grade(85)
get_letter_grade(75)
get_letter_grade(66)
get_letter_grade(33)
get_letter_grade(129)
get_letter_grade(-6)

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(x):

    for i in x:
        if is_vowel(i) == True:
            x = x.replace(i, "")
            
    return x

remove_vowels("moo")
# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
#for example:
#Name will become name
#First Name will become first_name
#% Completed will become completed

def normalize_name(x):

    non_python_identifiers = set('.!@#$%^&*()?><+=')

    for j in non_python_identifiers:
        x = x.replace(j, "")
    
    x = x.strip()
    x = x.lower()
    
    for i in x:
        if i == " ":
            x = x.replace(i,"_")
    return x

print(normalize_name("Paige"))
print(normalize_name("Paige Guajardo"))
print(normalize_name("#$! Paige"))
    

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(x):
    output = []
    y = 0
    for i in range(x):
        y += i

        output.append(y)
        

    return output

cumulative_sum([1,2,3])
cumulative_sum([1,2,3,4])

