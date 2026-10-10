# Download a copy of the file
# www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# Open the file
file = open("words.txt")

# Create an empty dictionary
words = {}

# Read each line in the file
for line in file:
    word = line.strip()
    words[word] = True

# Ask the user for a word
search = input("Enter a word: ")

# Check if the word is in the dictionary
if search in words:
    print("Word found")
else:
    print("Word not found")