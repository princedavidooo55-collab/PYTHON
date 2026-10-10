# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number
# of lines that matched the regular expression:

import re

filename = "mbox.txt"

regex = input("Enter a regular expression: ")

count = 0

file = open(filename)

for line in file:
    if re.search(regex, line):
        count = count + 1

print(filename, "had", count, "lines that matched", regex)