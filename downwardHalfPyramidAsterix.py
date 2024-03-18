# Print a downward half pyramid using asterix

for i in range(6, 0, -1):
    for n in range(0, i - 1):
        print("*", end=" ")
    print(" ")
