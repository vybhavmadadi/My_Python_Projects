#Conditionals, Booleans

#Conditionals

# Comparisons:
# Equal: 				==
# Not Equal: 			!=
# Greater Than:		>
# Less Than:			<
# Greater or Equal:	>=
# Less or Equal:		<=
# Object Identity:	is

#Boolean operators
# and
# or
# not


# Indentation matters!
if True:
	print('Conditional was True') # For true condition

if False:
	print('Conditional was False') # For false condition

language = 'Python'

if language == 'Python':
	print('This statement is True!') # Example of if


if language == 'Python':	# Example of else
	print('This statement is True!')
else:
	print('Not True!')

language = 'Java'

if language == 'Python':	# Example of elif
	print('Python indeed!')
elif language == 'Java':
	print('Java indeed!')
else:
	print('Not True!')


# using boolean operators
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in: # Example of and
	print('Admin Page')
else:
	print('Invalid')

if user == 'Admin' or logged_in: # Example of or
	print('Admin Page')
else:
	print('Invalid')

if not logged_in: # Example of not
	print('Please login')
else:
	print('Welcome')

#Example of using the 'is' operator. This is to compare two objects that might appear same but might be different in the memory
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # This will result true as the values are compared
print(id(a))
print(id(b))
print(a is b) # This will result false as the IDs in the memory are compared and not the values

c = a # Here we are copying the values and ID of the variable a
print(id(a))
print(id(c))
print(id(a) == id(c))
print(a is c) # This will result true as the IDs are also same as c was copied from a

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

# Conditional tests to evalute when the condiation can be defined as a False value.

# condition = False
# condition = None
# condition = 0
# condition = ()
condition = {}

if condition:
	print('Evalated to True')
else:
	print('Evaluated to False')



