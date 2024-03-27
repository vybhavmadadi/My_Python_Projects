#Tutorial of sorting lists, tuples and objects

# li = [9,1,8,2,7,3,6,4,5]

# s_li = sorted(li) #Sorting list function. Will create a new list that is sorted. This also works on other than lists
# print('Sorted Variable:\t', s_li)

# li.sort() #Sorted method. Sorts the existing list, but cannot be assigned to a variable. Will work only on lists
# print('Original Variable:\t', li)

# s_li = sorted(li, reverse=True) #Sort descending
# li.sort(reverse=True)
# print(s_li)
# print(li)

# tup = (9,1,8,2,7,3,6,4,5)

# s_tup = sorted(tup)
# # tup.sort() #WILL FAIL as touples do not have a sort.

# print(s_tup)
# print(tup)

# di = {'name' : 'Corey', 'job' : 'programming', 'age' : None, 'os' : 'Mac'}
# s_di = sorted(di) #Sort only the keys
# print('Dict\t', s_di)

# #How to use absolute value function to sort negative numbers as absolutes
# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li) #Sorts normally where negative numbers are lesser than 1
# print(s_li)
# s_li = sorted(li, key=abs) #Sorts all numbers as absolute numbers, ignores negative signs while sorting but the output still have the negative sign when the list is sorted
# print(s_li)

#The key parameter used above is very useful when sorting objects with name attributes
#Example here is a class

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter #Import attrgetter for sort key definition

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

# def e_sort(emp): #Define sorting on a key. Here it is name. Can be chaned to age or salary
#     return emp.name

# s_employees = sorted(employees) #Cannot be sorted like without the function above
# s_employees = sorted(employees, key=e_sort, reverse=True)

# s_employees = sorted(employees, key=lambda e: e.name) # Using lambda, which will not need the e_sort function

#Sort using attrgetter, look at the import above to get attrgetter

s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)