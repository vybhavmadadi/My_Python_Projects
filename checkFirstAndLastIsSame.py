# Check if a first and last number of a list is same and respond with a true or false

def checkNum(numberList):
    print('You have entered the following list of numbers: ', numberList)

    firstNum = numberList[0]    #First number of the list
    lastNum = numberList[-1]    #Last number of the list

    if firstNum == lastNum:     #Check if last number is same as first number
        return True
    else:
        return False


number_one = [10, 12, 13, 14, 15, 16, 10]
print(checkNum(number_one))

number_two = [1, 2, 3, 5, 6, 28, 48, 78]
print(checkNum(number_two))
