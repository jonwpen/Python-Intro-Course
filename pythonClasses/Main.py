# Use the type() function to check the type of a variable
print(type(5))

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))

# A class is a template for a datatype. An object is an instance of a class.
class Facade:
  pass
# The pass keyword tells Python that the class is left blank to avoid an error

# Like Java, you must create an instance of a class
facade_1 = Facade()

# A class instance is an object. This leads into OOP.
facade_1_type = type(facade_1)
print(facade_1_type)  # prints __main__
# ^ __main__ is keyword that means this is the class that is currently running

# A class variable in Python:
class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints "Rockstar"

# METHODS
# While functions can be standalone, methods are functions that belong to a class

# keyword .self in Python is the same as keyword .this in Java
# But it is used differently when defining methods as seen below...
class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."
# Conventionally, methods always has self as the first argument when defined

# Methods with arguments:
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)  # The self argument is implicitly passed
print(kms_in_5_miles)
# prints "8.045"

# Another example of the above. Methods with arguments:
class Circle:
  pi = 3.14

  def area(self, radius):
    area = self.pi * radius ** 2
    return area

circle = Circle()

pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(11460 / 2)

# CONSTRUCTORS - In python, the constructor is the __init__() methods
# It has double underscores. It can take arguments. Example:
class Shouter:
  def __init__(self, phrase):
# make sure phrase is a string
    if type(phrase) == str:

# then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

# INSTANCE VARIABLES: aren't shared by all instances of a class
# They are specific to an object of the class:
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# There are functions to check if an object has an attribute and to get the value of an attribute:
# hasattr(object, "attribute") and getattr(object, "attribute", default value)
# The default value to be returned is optional in the getattr() function
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")


# A powerful mechanic to objects is when you pass arguments to a constructor to make instance variables
# Writing classes and methods to structure and interact with various data that we need:
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"

# EXAMPLE 2:
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"

# EXAMPLE 3:
class Circle:
  pi = 3.14

  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    circumference = 2 * self.pi * self.radius
    return circumference


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# EVERYTHING IS AN OBJECT - all data types are also objects. Functions are also objects. Creating an object is creating a new data type
# Python automatically adds a lot of attributes to every object that is created.
# Use the dir() function to see all the attributes of an object. Short for directory.
fun_list = [10, "string", {'abc': True}]
type(fun_list)
# Prints <class 'list'>
print(dir(fun_list))
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# The method __repr__() is the same as toString() in Java.
# It prints the string representation of the object instead of the useless memory hashcode
class Circle:
  pi = 3.14

  def __init__(self, diameter):
    self.radius = diameter / 2

  def __repr__(self):
    return "Circle with radius " + str(self.radius)

  def area(self):
    return self.pi * self.radius ** 2

  def circumference(self):
    return self.pi * 2 * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

# Last project example of OOP:
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):  # Always pass self as the first arg in a method
    if type(grade) == Grade:
      self.grades.append(grade)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

pieter.add_grade(Grade(100))
