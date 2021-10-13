students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]



# 1. How many students are there?
print(len(students))
# 2. How many students prefer light coffee? For each type of coffee roast?

search_light = "light"
search_medium = "medium"
search_darl = "dark"
coffee_people = []
for i in students:
    coffee_people.append(i["coffee_preference"])
    
print(coffee_people)

count1 = 0
for i in coffee_people:
    if i == search_light:
        count1 += 1
        
count2 = 0
for i in coffee_people:
    if i == search_medium:
        count2 += 1
        
count3 = 0
for i in coffee_people:
    if i == search_darl:
        count3 += 1
        
print("\nPeople who prefer light: ", count1)
print("\nPeople who prefer medium: ", count2)
print("\nPeople who prefer dark: ", count3)

# 3. How many types of each pet are there?

animal_keepers = [ i["pets"] for i in students if i["pets"] != [] ]

#for i in students:
#    if i["pets"] != []:
#        animal_keepers.append(i["pets"])


print(animal_keepers)
print("\nThere are this many pets: ",len(animal_keepers))
print("\n",animal_keepers[0][0])

#print(type(animal_keepers[0]))

count = 0
good_boy = "dog"
# For every element in the list animal_keepers
for animal in animal_keepers:
    #For every element in animals
    for i in animal:
        #Access the first item in the list which is a dictionary, so we access the key "species" for that value to equal
        # good_boy which is a "dog"
        if animal[0]["species"] == good_boy:
            #add to the counter if true
            count += 1     
print("\nThere this many people with dogs: ",count)


# 4. How many grades does each student have? Do they all have the same number of grades?

list_of_grades = [grades["grades"] for grades in students]

    
print(list_of_grades)

print("\nThere are this many grades per student: ",len(list_of_grades[0]))
print("\nThey are not the same!")

# 5. What is each student's grade average?

from statistics import mean
#list_of_grades2 = []
list_of_grades2 = [mean(grades["grades"]) for grades in students]

#for grades in students:
#    list_of_grades2.append(mean(grades["grades"]))
    
print("This is a list of averages: ",list_of_grades2)

# 6. How many pets does each student have?

list_of_pets = []

for i in students:
    if i["pets"] == []:
        list_of_pets.append(0)
    else:
        list_of_pets.append(i["pets"])

print(list_of_pets)


list_of_num_pets = []
for num in list_of_pets:
    if num != 0:
        list_of_num_pets.append(len(num))
    else:
        list_of_num_pets.append(0)
    
print("\n\nThis is a list of how many pets a student has :",list_of_num_pets)

# 7. How many students are in web development? data science?

what_course = []

for i in students:
    what_course.append(i["course"])

    
count = 0
    
for i in what_course:
    if i == "web development":
        count += 1
        
print("There are this many students in web development: ", count)

# 8. What is the average number of pets for students in web development?

#list of all students in web dev
#web_pets = [i for i in students if i["course"] == "web development"]

web_pets = []
for i in students:
    if i["course"] == "web development" and i["pets"] != []:
        web_pets.append(i)
            
print("\n\n",web_pets)

num_web_pets = []
for i in web_pets:
    num_web_pets.append(i["pets"])
    
list_of_num_pets = []
for num in num_web_pets:
    list_of_num_pets.append(len(num))
    
print("\n\n", list_of_num_pets)
print("\n\nThis is the average number for web developments students with pets: ", mean(list_of_num_pets))
#print("Average number of web development pets: ", (sum(num_web_pets)/len(num_web_pets)) )

# 9. What is the average pet age for students in data science?

data_pets = []
for i in students:
    if i["course"] == "web development" and i["pets"] != []:
        data_pets.append(i)

print(data_pets)
        
num_data_pets = []
for i in data_pets:
    num_data_pets.append(i["pets"])
    
print("\n\n", num_data_pets)

pet_ages = []
for i in num_data_pets:
    for k in i:
        pet_ages.append(k["age"])
        #print("\n\n",k)
        #pet_ages.append(k)
    
print("\n\n",pet_ages)
print("\n\nAverage pet age for all students in data science: ",mean(pet_ages))

# 10. What is most frequent coffee preference for data science students?
# 11. What is the least frequent coffee preference for web development students?
# 12. What is the average grade for students with at least 2 pets?
# 13. How many students have 3 pets?
# 14. What is the average grade for students with 0 pets?
# 15. What is the average grade for web development students? data science students?
# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?