# ALL ABOUT FUNCTIONS

def hello_func(): #def is the keyword to define functions. The variables will go inside the brackets ().
	pass # pass keyword is required to use this function without any code in it.

print(hello_func) # If used without parenthesis, it prints of the location of the function in the memory
print(hello_func()) # If used with parenthesis, it will run the function and print out the result

# Lets define code in the same function as above
def hello_func_new():
	print('Hello Function!')

hello_func_new() # No need to use print as the result of the function is a print of string

# A function can be called many number of times in a code or program. While a change can be made only in the function which reduces modifying the code at multiple places.

# Returning a value as a result of the function execution
def hello_func_return():
	return 'Hello Function.'

print(hello_func_return()) # Print or a value passage has to be used as this function result is a string.
print(hello_func_return().upper()) # As we know the output of our function is a string, we can use all the arguments that string can use.

#Adding parameters to functions
def hello_func_parameters(greeting):
	return '{} Function.'.format(greeting)

print(hello_func_parameters('Hi'))

#Default value for a parameter
def hello_func_para(greeting, name = 'You'):
	return '{}, {}'.format(greeting, name)

print(hello_func_para('Hi'))
print(hello_func_para('Hi', name = 'Corey'))

#If we do know the number of positional parameters and/or keyword parameters, it is generally defined like this in Python coding although args and kwargs can be replaced with any text
def hello_args(*args, **kwargs):
	print(args)
	print(kwargs)

hello_args('Math', 'Art', name='John', age = 22)

#
def hello_args_1(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

hello_args_1(courses, info)
hello_args_1(*courses, **info)

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""Return True for leap years, False for non-leap years.""" #Doc strings are defined by triple quotes. They are used to define what a function does

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
	# The above code calculates a leap year. First the year is checked if it is divisible by 4 and if it is not divisble buy 100 or it is divisible by 400

def days_in_month(year, month):
	"""Return number of days in that month in that year."""

	if not 1 <= month <= 12:
		return 'Invalid Month' # Checking if the month value passed is between 1 or 12, if not the output is 'Invalid Month'

	if month == 2 and is_leap(year):
		return 29 # If the month is 2 (February) and year is a leap year, return the value as 29 instead of the defined 28.

	return month_days[month]


print(is_leap(2017))
print(days_in_month(2017, 2))
print(is_leap(2024))
print(days_in_month(2024, 2))
print(days_in_month(2024, 14))
