# INPUT OUTPUT CODE CHALLENGES

# # 1. Accept numbers from user and multiply them
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))

# print("The product of ", num1, "and", num2, "is:", num1 * num2)

# # 2. Display three strings "Name", "Is", "Kratos" as "Name**Is**Kratos"
# str1, str2, str3 = input("Enter a sentence containing three words: ").split()
# print(str1, str2, str3, sep="**")

# # 3. Convert decimal number to octal number using %o formatting code within print() function
# num = int(input("Enter a decimal number: "))
# print("The octal number of the decimal number", num, "is", "%o" % num)

# # 4. Display float number with two decimal places using print() using %.2f formatting code
# num = float(input("Enter a float number: "))
# print(num, "rounded to two digits is", "%.2f" % num)

# 5. Accept a list of 5 float numbers as an input from the user and display them as a list
# fnum = []
# for i in range(5):
#     if i == 0:
#         num = float(input("Enter a float number:"))
#     elif i == 4:
#         num = float(input("Enter the last float number:"))
#     else:
#         num = float(input("Enter the next float number:"))

#     fnum.append(num)
# print("The numbers you have entered are:", fnum)

# # 6. Write all content on a given file to a new file by skipping line number 5
# with open("test.txt", "r") as input_file:
#     with open("copy_text.txt", "w") as output_file:
#         n = 0
#         for i in input_file:
#             if n == 4:
#                 n += 1
#                 continue
#             else:
#                 output_file.write(i)
#             n += 1

# # 7. Accept any three strings from one input() call
# str1, str2, str3 = input("Enter a three word sentence separated by space:").split()
# print("Name 1 is", str1)
# print("Name 2 is", str2)
# print("Name 3 is", str3)

# # 8. Format variables using a string.format() method
# quantity = input("Enter the quantity purchased:")
# totalMoney = int(input("Enter the total money paid for the said quantity:"))
# price = float(input("Enter the price of each product:"))
# statement = "I have ${1} so that I can buy {0} football for ${2:.2f}."
# print(statement.format(quantity, totalMoney, price))

# # 9. Check if a file is empty or not
# import os

# size = os.stat("emptyFile.txt").st_size
# if size == 0:
#     print("The file is empty.")
