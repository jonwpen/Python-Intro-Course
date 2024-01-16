# For loop structure:
# for <temporary variable> in <collection>:
# # <action>
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

for i in ingredients:
    print(i)
# ---INDENTATION--- Where Java creates code blocks using semicolons, Python uses indentation instead.
# a simple for loop can be a one-liner. But it is not always good to do it:
for i in ingredients: print(i)

# Instead of iterating over a particular list, I can also just do a task multiple times using the range() function
for temp in range(6):
    print("Learning Loops!")
# This will count the steps:
for temp in range(6):
    print("Loop is on iteration number " + str(temp))
# ^The str() function converts temp(an integer) to a String. Temp increments for every iteration.
for temp in range(6):
    print("Loop is on iteration number ", temp)  # This will also work. Leave temp as an int.

# This will print '5' three times. Because you are not printing i. You are printing 5 for that range length.
for i in range(3):
    print(5)

# ---WHILE LOOPS---:
count = 0
while count <= 3:
    print(count)
    count += 1
# One-line elegant version:
count = 0
while count <= 3: print(count); count += 1  # A semicolon is used to denote a new line

# Iterate over a list with a while loop:
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0
while index < length:
    print("I am learning about " + python_topics[index])
    index += 1

# HOTKEYS - control + r to run the program. Control + c to end it.

# ---LOOP CONTROL: BREAK---
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
    print(item)
    if item == "knit dress":
        print("That's the one!")
        break

print("End of search!")

# ---LOOP CONTROL: CONTINUE---
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
    if i <= 0:
        continue  # This will skip over any index that meets the condition
    print(i)

# ---NESTED LOOPS---
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
# Loop through each sublist
for team in project_teams:
    # Loop elements in each sublist
    for student in team:
        print(student)

# ---LIST COMPREHENSIONS--- These are like lambda expressions in Java
# These are used to write more elegant code. An example:
# To create a new list based on an existing list. The verbose way:
numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
    doubled.append(number * 2)

print(doubled)
# The list comprehension one-liner:
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]  # new_list = [<expression> for <element> in <collection>]
print(doubled)

# ---List Comprehensions: Conditionals---
# Verbose way:
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
    if num < 0:
        only_negative_doubled.append(num * 2)

print(only_negative_doubled)

# List Comprehension way:
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

# More syntax examples:
numbers = [2, -1, 79, 33, -45]

no_if = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]
# One more simple example:
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [i for i in heights if i > 161]
print(can_ride_coaster)

# A  program with a more complex list comprehension:
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for i in prices:
    total_price += i
print(total_price)

average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

new_prices = [i - 5 for i in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue:", total_revenue)
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)
# ^ You are creating a new list. You are iterating over the length of the hairstyles list(integers). You are NOT
# iterating over the list itself because 'i' needs to be an int in order to compare the prices integer. The
# hairstyles[i] in the beginning is what will be populating the new list.
