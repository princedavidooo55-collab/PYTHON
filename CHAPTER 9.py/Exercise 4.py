# Add code to the above program to figure out who has sent the most
# messages in the file. After all the data has been read and the dictionary has
# been created, look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

file = open("mbox-short.txt")

emails = {}

for line in file:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

# Find the email address with the most messages
most_messages = None
most_email = None

for email in emails:
    if most_messages is None or emails[email] > most_messages:
        most_email = email
        most_messages = emails[email]

print(most_email, most_messages)