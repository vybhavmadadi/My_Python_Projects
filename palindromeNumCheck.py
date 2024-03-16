#Check if a number is a palindrome

def palindromeCheck(num):
    print('You have the following number:', num)
    orig_num = num

    #reverse the original number
    reverse_num = 0
    while num > 0:
        reminder = num % 10
        reverse_num = (reverse_num * 10) + reminder
        num = num // 10
    
    if orig_num == reverse_num:
        return(print('The number you have entered', orig_num, 'is INDEED a palindrome!'))
    else:
        return(print('The number you have entered', orig_num, 'is NOT a palindrome'))

palindromeCheck(121213)
palindromeCheck(1010101)
