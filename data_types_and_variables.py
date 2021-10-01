#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, 
# they love it), and Hercules (1 day, you don't know yet if they're going to like it).
#  If price for a movie per day is 3 dollars, how much will you have to pay?

#Movies['little mermaid', 'brother bead', 'hercules']
little_mermaid = 3
brother_bead = 5
Hercules = 1

total_price_owed = ((little_mermaid) + (brother_bead) + (Hercules)) * 3
print('Total Price: ', total_price_owed)

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours 
# for Google and 4 hours for Amazon.

#Companies['Google', 'Amazon', 'Facebooko']
google = 400
amazon = 380
facebook = 350

weekpay = (facebook*10) + (google*6) + (amazon*4)
print(weekpay)

#A student can be enrolled to a class only if the class is not full and the class schedule 
# does not conflict with her current schedule.
full_classroom  = False
on_schedule = False

if  not full_classroom and not on_schedule:
    print("Enrolled in Classroom")

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.
product_more_than_one =  2
offer_deal = True

premimum = False 

if (((product_more_than_one > 1) and (offer_deal and not False)) or ( premimum == True )):
    print("The offer is avaliable")


#Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:

#the password must be at least 5 characters

just_right = len(password) >= 5

#the username must be no more than 20 characters

not_too_long = len(username) <= 20

#the password must not be the same as the username

unique_pass = password != username



all_of_it_is_correct = just_right and not_too_long and unique_pass
#bonus neither the username or password can start or end with whitespace

not_itself = username.strip() != username
not_password = password.strip() != password

no_white = not_itself or not_password

# username.strip() and password.strip()