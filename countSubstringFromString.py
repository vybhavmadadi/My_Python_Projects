# Count the number of times a substring is used within a string

def subStringInString(Str, Substr):
    print('The string you have entered is', Str)
    print('The substring you have entered is', Substr)
    count = Str.count(Substr)
    return count


print(subStringInString('My name is Emma and Emma is my name', 'Emma'))
print(subStringInString('My name is Emma and Emma is my name', 'None'))

