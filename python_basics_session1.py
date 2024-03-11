## Why do we learn Python as medical researchers?
# number 1 language of science and research in the world
# Statistics and data analysis for your thesis
# EEG and ERP analysis in neuroscience
# Machine Learning and AI in medicine (data science and health informatics)
# Generally, automate your work and make your life easier

# Every programming language has a syntax. Syntax is the rules of writing the code. Python's syntax is very simple and easy to learn, and yet it is very powerful.

# Variable Types
weight = 110 #numeric: integer
height = 170 #numeric: integer
age = 50 #numeric: integer
hba1c = 7.5 #numeric: float
name = "Ahmed" #string
diabetic = True # boolean
hypertensive = False # boolean

# Data Structures
rbs = [70, 100, 112, 240] # list of integers. A list can hold any type of variables, and can hold a mix of types.
patient1 = {'name':'Ahmed', 'age':50, 'diabetic': True, 'hypertensive': False} # Dictionary: key-value pairs
patient2 = {'name': 'Hassan', 'age':44, 'diabetic':False}
filter = (1, 100) # Tuples: It is a list that cannot be changed. i.e. you cannot add or remove items from it, unlike lists.

# How to recall an item in a list: List name with index between square brackets. index starts at 0 for the first item in the list. If you need the last item in the list, the index is -1.
print(rbs[-1])

# How to add an item to the list? Use the append function.
rbs.append(150)

# How to remove an item from the list? Use the remove function.
rbs.remove(100)

# How to recall an item in a dictionary: dictionary name with the key as the index. The key will get you its value.
print(patient1['name'])
print(patient2['age'])

# How to add a new key-value pair to the dictionary? Just assign a value to a new key.
# See next session

# Operations: all math operations are possible
weightInGrams = weight * 1000 # multiplication
weightInKilos = weightInGrams / 1000 # division
agePlus10 = age + 10 # addition
ageMinus10 = age - 10 # Subtraction
x = 100000 * 12
x = (1000 * 15) / 2

# Example: Calculate body mass index
heightInMeters = height/100
bmi = weightInKilos / (heightInMeters * heightInMeters)
bmi2 = weightInKilos / heightInMeters ** 2

### For loops ###
# For loops are used to repeat a block of code on a list, dictionary, or a range of numbers.
# Syntax: for item in list: # do something with the item
# Looping on a list
heightsInCm = [170, 200, 160, 300, 400, 120]
weights = [110, 120, 50, 200, 500, 200]

for height in heightsInCm: # This will loop on each item in the list called heightsInCm, and apply whatever code you write below it on each item.
    print(height) # This line is indented (i.e has a 4 spaces in front of it that we do by pressing Tab once). This is to indicate that it is part of the for loop. You can add any number of lines of code inside the for loop to apply it on each item in the list.

# Looping on two lists at the same time
index = 0
for height in heightsInCm:
    heightInMeter = height / 100
    bmi = weights[index] / heightInMeters ** 2 # ** is the power operator. So this is the height in meters to the power of 2.
    print(bmi)
    index = index + 1 # We add 1 to the index to go to the next item in the weight list.

# Another method is to have the data (weight and height) in tuples to be paired in one list from the start.
WeightAndHeightList = [(100,170), (80, 180) , (40, 180) ] # (weight, height)

for item in WeightAndHeightList:
    weight = item[0] # first item in the tuple i.e weight
    height = item[1] # 2nd item in the tuple i.e height
    height = height/100 # we convert the height to meters and save it on itself. or you can save it to a new variable. It's up to you.

    bmi = weight / height**2
    print(bmi)

    # Next time: for loops on dict, If conditions, New Function/Command
    

