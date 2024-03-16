# Display numbers that are divisible by 5 from a list

def divByFive(numberList):

    if len(numberList) == 0:
        return(print('You have not entered any number. There should be atleast one number to have a valid result for this function'))
    else:
        print('The list of numbers that you have entered are :', numberList)

        output_list = []

        i = 0
        for num in numberList:
            if num % 5 == 0:
                if i == 0:
                    print('These are the numbers from your list that are divisible by 5:')
                output_list.append(num)
                i += 1
    
        if len(output_list) == 0:
            return(print('None of the numbers in your list are divisible by 5'))
        else:
            return output_list

numlist1 = [10, 15, 16, 17, 20, 22, 25]
numlist2 = [11, 12, 13, 14, 16, 17, 21]
numlist3 = []

print(divByFive(numlist1))
print(divByFive(numlist2))
print(divByFive(numlist3))
