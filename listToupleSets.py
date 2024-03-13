#Lists, Tuples and Sets

# courses = ['History', 'Maths', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Education']
# nums = [1,5,2,4,3]

# courses.append('Art')

# courses.insert(0, 'Art')

# courses.extend(courses_2)

# courses.remove('Maths')

#Removes last value in the list
# courses.pop()

# courses.reverse()

# courses.sort()
# nums.sort()
# courses.sort(reverse=True)
# nums.sort(reverse=True)

# sorted_courses = sorted(courses)


# for course in courses:
# 	print(course)

# for index, course in enumerate(courses):
# 	print(index, course)

# for index, course in enumerate(courses, start=1):
# 	print(index, course)

# course_str = ', '.join(courses)
# course_str = ' - '.join(courses)

# new_list = course_str.split(' - ')

# print(course_str)
# print(new_list)

# print(courses.index('CompSci'))
# print('Art' in courses)
# print('Maths' in courses)
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# print(sorted_courses)

#TUPLES
# Similar to lists but cannot be modified. They are immutable

# Example of lists which are mutable, to showcase differences to tuples
# list_1 = ['History', 'Maths', 'Physics', 'ComputerScience']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)

#Example of Tuples of the same as lists above to show how they are immutable
# tuple_1 = ('History', 'Maths', 'Physics', 'ComputerScience')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art' #Error here as tuples doe not support item assignment

# print(tuple_1)
# print(tuple_2)

#SETS
# cs_courses = {'History', 'Maths', 'Physics', 'ComputerScience'}
# Sets have no specific order in which they store the values. Duplicate values are ignored and showed as one.
# cs_couses_new = {'History', 'Maths', 'Physics', 'ComputerScience', 'Maths'}
# print('Maths' in cs_courses)
# art_courses = {'History', 'Maths', 'Art', 'Design'}

# print(cs_courses.intersection(art_courses)) #Shows intersection between two sets
# print(cs_courses.difference(art_courses)) #Shows difference between two sets
# print(cs_courses.union(art_courses)) #Shows union of two or more sets

# print(cs_courses)
# print(cs_couses_new)

#EMPTY LISTS, TUPLES and SETS
#Empty Lists
empty_list = [] #either this
empty_list = list() # or this

#Empty Tuples
empty_tuple = () # either this
empty_tuple = tuple() # or this

#Empty Sets
empty_set = {} # This isn't right! It's a dictionary and not set
empty_set = set() # Only this method can define an empty set unlike the two options available like a list and tuple