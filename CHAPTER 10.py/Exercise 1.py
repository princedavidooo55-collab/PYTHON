# Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the list in
# reverse order and print out the person who has the most commits.

file = open("mbox-short.txt")

emails = {}

for line in file:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

# Create a list of (count, email) tuples
email_list = []

for email, count in emails.items():
    email_list.append((count, email))

# Sort the list in reverse order
email_list.sort(reverse=True)

# Print the person with the most messages
print(email_list[0])