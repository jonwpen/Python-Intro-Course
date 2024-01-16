# Functions are similar to methods, except that they are not associated with any class. They are independent.
# Use the def keyword as the function header. The function can take in parameters and have return values.
# Syntax:
def directions_to_times_sq():  # Indentation defines the method body instead of curly braces.
    print("Walk 4 mins to 34th St Herald Square train station")
    print("Take the Northbound N, Q, R, or W train 1 stop")
    print("Get off the Times Square 42nd Street stop")


directions_to_times_sq()  # < call the function


def generate_trip_instructions(location):  # Using parameters and passing arguments
    print("Looks like you are planning a trip to visit " + location)


generate_trip_instructions("Central Park")

# Python has three types of arguments: 1 positional, 2 keyword, and 3 default.
# 1 args are defined based on where there are positioned in the function parenthesis
def calculate_taxi_price(miles_to_travel, rate, discount):
    print(miles_to_travel * rate - discount )
# 2 args are explicitly defined in the function call:
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)
# 3 args are explicitly defined in the function declaration:
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
    print(miles_to_travel * rate - discount)
# with default args, you can either leave it out of the function call or you can overwrite it.

# There are user-defined functions and built-in functions like print() and len()
# There is a variable scope similar to in Java
# There is a return keyword that works just like Java

# sample code with return statement example:
current_budget = 3500.75

def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
    return budget - expense

shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

# You can have multiple returns:
def top_tourist_locations_italy():
    first = "Rome"
    second = "Venice"
    third = "Florence"
    return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

# Another example:
def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("John")

def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time

estimate = estimated_time_rounded(3.2)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
    print("Your trip starts off in " + origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("city2", "city3", "boat")

# Final example:

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = f_to_c(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)
print("The GE train does " + str(train_work) + " Joules of work over Y meters.")


