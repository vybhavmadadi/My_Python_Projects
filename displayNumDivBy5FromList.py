# Display numbers that are divisible by 5 from a list

def divByFive(numberList):
    print('The list of numbers that you have entered are :', numberList)

    i = 0
    for num in numberList:
        if num % 5 == 0:
            if i == 0:
                print('These are the numbers from your list that are divisible by 5:')
            print(num)
            i += 1



numlist1 = [10, 15, 16, 17, 20, 22, 25]
numlist2 = [11, 12, 13, 14, 16, 17, 21]

print(divByFive(numlist1))
print(divByFive(numlist2))
