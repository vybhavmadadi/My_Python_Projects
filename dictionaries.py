#Dictionaries
# Will be based on key value pair

student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'ComputerScience']}

print(student)
# print(student['name']) 
# print(student.get('name'))
# print(student.get('phone')) #Using get method returns a value of 'None' instead of an error when an unknown key is passed
# print(student.get('phone', 'Not Found')) #For unkown keys, you can define what value should be shown instead of the default 'None'

student['phone'] = '555-5555' #Adding new keys and values without adding them directly to the original definition
student['name'] = 'Jane' #Updating existing values

print(student.get('phone'))
print(student)

student.update({'name': 'Jane', 'age': 26, 'phone': '555-6666'}) #Update method allows for multiple key value pair update or additions.

print(student)

# del student['age'] #Delete keys and values

# print(student)

age = student.pop('age') #Also used to delete and then assign that value to a variable

print(age)
print(student)

#Looping through all the keys and values
student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'ComputerScience']}

print(len(student)) #Shows the length of the dictionary or the number of keys
print(student.keys()) #Shows all the keys in the dictionary
print(student.values()) #Shows all the values in the dictionary
print(student.items()) #Shows all the keys and values in the dictionary

#Looping through
for key in student:
	print(key)

for key, value in student.items():
	print(key, value)