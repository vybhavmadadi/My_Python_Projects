# Calculate income tax


def itCalc(income):
    print("Your income is:", income)

    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.1
    else:
        tax = 1000 + ((income - 20000) * 0.2)

    return tax


print("The tax on your income is: $", itCalc(8000))
print("The tax on your income is: $", itCalc(16000))
print("The tax on your income is: $", itCalc(40000))
