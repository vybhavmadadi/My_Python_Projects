# Remove a defined number of characters from the start of a string and print the rest
text = input("Enter a word: ")
num = int(input("Enter a number: "))

if num > len(text):
    print("The number you have entered exceeds the length of your word")
else:
    new_word = text[num:]
    print("The remaining text from your word is: ", new_word)


def remove_chars(word, num):
    if num > len(word):
        return print("ERROR: Please a number value lower than the length of the word.")
    else:
        x = word[num:]
        return x


print(remove_chars("syntax", 7))
print(remove_chars("syntax", 3))
