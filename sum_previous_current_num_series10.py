# Print the sum of the current number and previous number for a set of 10 consecutive numbers

print("Printing current and pervious number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(0, 11):
    x_sum = previous_num + i
    print(
        "Current Number: ",
        i,
        ". Previous Number: ",
        previous_num,
        ". Sum: ",
        x_sum,
        ".",
    )
    previous_num = i
