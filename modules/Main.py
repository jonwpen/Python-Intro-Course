


# code is packaged into files or sets of files called modules. It works just like in Java.
# Modules are also called libraries or packages. A package is really a directory that holds a collection
# of modules. A library may contain a lof of unnecessary code that slows the computer down.
# Only use what you need. The syntax for importing and using a module:
from datetime import datetime

current_time = datetime.now()

print(current_time)

# example 2:
import random  # We use more than a single piece of this module, so we import the whole module

# Create random_list below:
random_list = []

# Create randomer_number below:
random_list = [random.randint(0, 101) for rand in range(101)]

# Print randomer_number below:
randomer_number = random.choice(random_list)
print(randomer_number)

# random.choice() which takes a list as an argument and returns a number from the list
# random.randint() which takes two numbers as arguments and generates a random number

# You can create an alias for the namespace when you import a module. Syntax:
# import module_name as name_you_pick_for_the_module
# It is most commonly done if the name is too long to use in functions
# Another syntax is "import *". The * is a wildcard that will import everything.
# This is considered unsafe because it can pollute your workspace.

# An example using two modules: matplotlib and random:
# This won't run because I don't have the modules. I can replace them later though.
# import codecademylib3_seaborn
# from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
print(numbers_b)
# plt.plot(numbers_a, numbers_b)
# plt.show()


# When doing math with float numbers, you need to use the Decimal module for proper formatting:
from decimal import Decimal
# This is to avoid printing a decimal with too many unnecessary decimal places.
two_decimal_points = Decimal("0.2") + Decimal("0.69")
print(two_decimal_points)

four_decimal_points = Decimal("0.53") * Decimal("0.65")
print(four_decimal_points)

# SCOPE
# A file does not have access to the functions of other files. You have to import it.
# A file is actually the same as a module. So you import the function just the same.


# A datetime is an object. We have already imported datetime above
birthday = datetime(1987, 8, 14)
with_hour = datetime(1987, 8, 14, 4, 25, 12)
# This includes hours, minutes, and seconds
print(birthday.year)
print(birthday.weekday())

print(datetime(2018, 1, 1) - datetime(2017, 1, 1))
# You can't add, divide, or multiply, only subtract

# You often have to parse a date to fit the datetime format. You use strptime.
# This stands for string parse time. Go to docs.python.org to learn about functions.
parsed_date = datetime.strptime("Jan 15, 2018", "%b %d, %Y")
print(parsed_date.year)

# strftime does the opposite of strptime. It turns a datetime into a string
date_string = datetime.strftime(datetime.now(), "%b %d, %Y")
print(date_string)

# VIRTUAL ENVIRONMENTS AND PIPENV
# If you work on multiple projects that require different versions of different libraries,
# you would need to set up a virtual environment to handle that coomplexity for you.
# pip is Python's package manager.
# check mym pip version from CLI: pip3 --version
# I have downloaded pipenv, and then I added it to my PATH

# Link to tutorial about setting up virtual environments
