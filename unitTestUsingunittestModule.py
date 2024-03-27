#Unit testing your code with the unittest module
def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

# print(add(10, 5)) #Testing with print statements is hard to automate and will add a lot of hard work while testing a lot of functions at once.

#To create unit tests, you will need to create a test module by creating a new file with appending 'test_' to the name of this file

#We are going to write tests for the file employee.py
#BUT use a new file named test_employee.py. Jump to that file for the rest of this tutorial
