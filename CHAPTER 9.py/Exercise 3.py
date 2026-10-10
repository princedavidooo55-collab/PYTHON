# Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address,
# and print the dictionary

file = open("mbox-short.txt")

emails = {}

for line in file:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

print(emails)