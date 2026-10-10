# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other
# than the letters a-z. Find text samples from several different languages and see
# how letter frequency varies between languages. Compare your results with the
# tables at https://wikipedia.org/wiki/Letter_frequencies.

file = open("text.txt")

letters = {}

for line in file:
    line = line.lower()

    for char in line:
        if char >= 'a' and char <= 'z':
            letters[char] = letters.get(char, 0) + 1

# Create a list of (count, letter) tuples
letter_list = []

for letter, count in letters.items():
    letter_list.append((count, letter))

# Sort from highest frequency to lowest
letter_list.sort(reverse=True)

# Print the letters and their frequencies
for count, letter in letter_list:
    print(letter, count)  