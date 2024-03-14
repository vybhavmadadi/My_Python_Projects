word = input("Enter a word ")
print("You have entered ", word)

# Solution using range
size = len(word)

print("The length of the word is ", size)
print("Printing the characters at even indexes")

for i in range(0, size, 2):
    print("Index[", i, "]", word[i])

# Solution using list
x_list = list(word)
x = 0
for i in x_list[0::2]:
    print("The letter at position", x, " is ", i)
    x += 2
