print("I drink coffee")
my_name = "John"  # this is how you declare a variable
print(my_name)
print(my_name)

some_number = 14
some_float = 4.6
# arithmetic operations are + - * /
print(573 - 74 + 1)
# for division, Python converts all ints into floats
# Python operations follow the standard order of operations

# to type exponents, use ** instead of superscript. (square)
print(4 ** 4)  # 4 to the power of 4. Remember, the number after the ** is 'to the power of'

# Python has the modulo % just like Java
# Python has concatenation just like Java
# Python has += just like Java

# A multi-line string must be stored in a variable and surrounded by triple quotes

# to take user input:
likes_snakes = input("Do you like snakes? ")
print(likes_snakes)

# Python has boolean like Java. But it is called a bool type that contains the keywords True and False (capitalized).
# There are also relational operators == and != as well as > < >= <=
# Ways to create a Boolean variable:
# simply assign it true or false
set_to_true = True
# set a variable equal to a boolean expression:
boolean1 = 5 != 7
print(boolean1)
print(type(boolean1))  # 'type' <this will show the datatype of the variable

# if statement syntax:
if some_number == 14:
    print("some number is equal to true")

# There are boolean operators 'and' 'or' and 'not'
if (3 >= 2) and (2 >= 1):
    print("yes...yes it is")
if not 3 >= 4:
    print("it is not greater")
# There is an else if statement, but it is called an elif. The if is checked, then the elif, then finally the else.
grade = 86
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("C - F")

# Python has Random like Java. You say import random, then use randint(1, 9).
# To concatenate with both Strings and ints, use a comma to separate types, not a + sign. The + sign is for adding
# Strings to Strings


# ---LISTS---
# In Python, an array is called a list. Unlike Java, the list can contain mixed data types like String and int.
# You can declare an empty list and populate it later.
# Lists have built-in methods just like Java. A popular list method is .append() which will add an element to the end.
height = [34, 43, 66, 57]
height.append(88)
print(height)
# We can easily concatenate a new list into an existing list:
more_heights = height + [33, 54, 79]
print(height[1])  # <to print an element. Lists are zero indexed like Java arrays.
# You can use -1 to get the last item in the list
# Reassigning an element's value is more straightforward than Java:
height[1] = 44
# You can use .remove in a list. If there are duplicates, only the first one is removed.
height.remove(66)
print(height)
# Python has 2D lists that are just like 2D arrays.
new_list = [['a', 'b', 'c'], ['d', 'e', 'f']]  # <Python wants you to include a white space after a comma
new_list[1].remove('e')  # This is how you remove an index from a 2D list

# When you .pop() from a list, it will return the value removed. If you don't specify the index, it will remove the
# last one. But you can pop any index.

# The range() function is for populating a list with consecutive numbers.
my_range = range(10)  # <this creates a range object
print(my_range)
print(list(my_range))  # <this list function converts it to a list
# You can use two parameters to have a start and end point for your range.
# You can use 3 inputs to skip numbers:
my_range2 = range(2, 9, 2)
print(list(my_range2))

# To get the length of a list, use the len() function:
my_list3 = [1, 2, 3, 4, 5]
my_list3_len = len(my_list3)
print(len(my_list3))
# To get the length of a range:
my_range2_len = len(my_range2)
print(my_range2_len)

# Slicing is extracting a portion of a list.
letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[1:6]
print(sliced_list)
# To select the first 3 elements:
a = sliced_list[:3]  # Or you could say sliced_list[-3:] to select the end elements.
print(a)
# If a problem needs you to slice off all but the last elements, you would use negative slicing: [:-3]

# To count occurrences of an item in a list:
letters2 = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters2.count("i")
print(num_i)
# You can do the same for sub-lists of a 2D list.

# To sort items in a list:
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names)
names.sort(reverse=True)  # <sort it in reverse
print(names)
# You can also use the built in function sorted() that will store a new sorted list.
sorted_names = sorted(names)
print(sorted_names)
# 2D lists, insert, and append:
last_semester_grade_book = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
grade_book = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history, 88"]]

print(grade_book)

grade_book.append(["computer science", 100])
grade_book.append(["visual arts", 93])
grade_book[5][1] = 98
grade_book[2].remove(85)
grade_book[2].append("Pass")

full_grade_book = last_semester_grade_book + grade_book
print(full_grade_book)

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

front_display_list.insert(0, "Pineapple")
print(front_display_list)

# ---TUPLES---
# This is like a list, but it is immutable, cannot be changed once created.
# So a list is like an ArrayList and a tuple is like an array. Syntax:
my_info = ("John", 36, "analyst")
print(my_info)
# To extract the information in a tuple, you can assign new variables to the elements in the tuple:
name, age, role = my_info
print(name)
# Special case: a one element tuple must have a trailing comma after the element so Python knows it is a tuple.
one_tuple = (3,)
print(one_tuple)

# This zip() function combines two lists into a single list of pairs.
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights)
converted_list = list(names_and_heights)  # <The zip must then be converted back into a list before printing.
print(converted_list)  # Notice the inner lists are converted into tuples.
