def prod_or_sum(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2


result = prod_or_sum(20, 30)
print("The product of the numbers is: ", result)

result = prod_or_sum(40, 30)
print("The sum of the numbers is: ", result)
