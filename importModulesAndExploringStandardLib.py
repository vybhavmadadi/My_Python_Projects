# Import Modules and Exploring the standard library
# import my_module as mm # Import module as a whole and as a shorter name
# from my_module import find_index # Import specific functions
# from my_module import find_index as fi, test # Import specific functions as a shorter name and/strings from the module
# from my_module import find_index, test # Import specific functions from a module and also string
# from my_module import * # Gets everything from the module. ***NOT USED AS MUCH AS TRACKING WILL BE HARD***
# STANDARD LIBRARIES are available for all python paths.

# All modules are stored in sys.path, let's import sys module to see this.
# import sys
# import random # Standard Library for random values picker
import math # Match standard library

courses = ["History", "Maths", "Physics", "ComputerScience"]

# index = mm.find_index(courses, 'Maths')
# index = find_index(courses, "Physics")
# print(index)
# print(sys.path) #path where the modules are sourced from. If your modules are in a different location on your local, use sys.path.append('Location of your modules').
                #rather add env variables in your ~/.bash_profile. Adding export PYTHONPATH="path to your modules location" using mac terminal. Restart the terminal.

# random_course = random.choice(courses)

# print(random_course)

rads = math.radians(90)
# print(rads)
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

import os # Current OS module

print(os.getcwd())
print(os.__file__) #Shows the file location directory
