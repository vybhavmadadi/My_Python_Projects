# Reverse an integer and print it out
def reverseInt(int_1):
    print("The number you have entered is:", int_1)

    while int_1 > 0:
        out = int_1 % 10
        int_1 = int_1 // 10
        ans = print(out, end=" ")
    return ans


print(reverseInt(7536))
