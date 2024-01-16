my_var = "dark knight"
print(my_var.title())
# Prints: Dark Knight

dinosaur = "T-Rex"
print(dinosaur.upper())
# Prints: T-REX
game = "Popular Nintendo Game: Mario Kart"

print("l" in game)  # Prints: True
print("x" in game)  # Prints: False
# The in syntax is used to determine if a letter or a substring exists in a string.

# Strings are immutable in Python. An action that modifies a String is actually just creating a new one.

str = "hello"  # < To iterate over a String, use 'for' 'in'
for c in str:
    print(c)
# h
# e
# l
# l
# o

# A String can be thought of as a list. It has indices that you can select.
my_name = "John"
first_initial = my_name[0]

# We can slice a String like we slice a list:
favorite_fruit = "blueberry"
print(favorite_fruit[4:6])
# Output: be
print(favorite_fruit[:4])
# Output: blue
print(favorite_fruit[4:])
# Output: berry

first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
print(new_account)  # prints 'Villa'
# Slices the first 5 letters from the word. Refer to the graphic to see how to place indices when slicing.

# You can use len() on a String. This is useful for finding what index you want to slice or print.
# Remember that the length of a String and the last index of it are two different
# numbers. The last index will be 1 less that the length:
favorite_fruit = "blueberry"
last_char = favorite_fruit[len(favorite_fruit)-1]
print(last_char)
# Output: y
length = len(favorite_fruit)
last_chars = favorite_fruit[length-4:]
print(last_chars)
# Output: erry

# Another example:
first_name2 = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
    return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
# ^ This line is simply using the len() function to provide an index for slicing
temp_password = password_generator(first_name2, last_name)
print(temp_password)

# Negative indexing is the easier way to get the last index of a String:
print(favorite_fruit[-1])
# => 'y'
print(favorite_fruit[-2])
# => 'r'
print(favorite_fruit[-3:])
# => 'rry'

# Escape characters: you can include a quote in a String by putting a \ before it:
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

# Because Strings are lists, we can iterate over them with for loops and while loops
def get_length(word):  # This function replicates the len() function by using a for loop
    total = 0
    for i in word:
        total += 1
    return total

# ---STRINGS AND CONDITIONALS---
def letter_check(word, letter):
    check = False
    for i in word:
        if i == letter:
            check = True
    return check

# Python can condense this letter checking conditional function even further:
print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False
print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False
print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")
# => True



def contains(big_string, little_string):
    check = False
    if little_string in big_string:
        check = True
    return check

# When iterating, I get hung up on mismatching integer and String types. One thing that will help is to always name
# variables and functions with good descriptions, like 'common' and 'char'
def common_letters(string_one, string_two):
    common = []
    for char in string_one:
        if char in string_two and char not in common:
            common.append(char)
    return common

word = common_letters("apple", "Jacks")

# recap:
# A string is a list of characters.
# A character can be selected from a string using its index string_name[index]. These indices start at 0.
# A ‘slice’ can be selected from a string. These can be between two indices or can be open-ended, selecting
# all of the
# string from a point.
# Strings can be concatenated to make larger strings.
# len() can be used to determine the number of characters in a string.
# Strings can be iterated through using for loops.
# Iterating through strings opens up a huge potential for applications, especially when combined with conditional
# statements.

# Password generator project. What I learned here, you cannot append a String like with a list. But you can use the
# += operator to concatenate an empty String. This populates it and is basically the same as appending.
def username_generator(first_name, last_name):
    user_name = first_name[0:3] + last_name[0:4]
    if len(first_name) < 3 or len(last_name) < 4:
        user_name = first_name + last_name
    return user_name

def password_generator(user_name):
    password = ""    # start with an empty string
    for i in range(len(user_name)-1):    # use range() to create a list  of integers that you can iterate over
        password += user_name[i]      # concatenate with the user_name chars except for the last one
    new_pass = user_name[len(user_name)-1] + password  # Then add the last user_name char to the front
    return new_pass  # The intended password will now be "pAbeSim"

print(password_generator("AbeSimp"))
