# Function to print out of base and exponent
def exponent(base, exp):
    print("The base value you have entered is:", base)
    print("The exponent value you have entered is:", exp)

    result = 1
    num = exp

    while num > 0:
        result = result * base
        num -= 1
    print(base, "raises to the power of", exp, "is: ", result)


exponent(2, 5)
exponent(5, 4)
