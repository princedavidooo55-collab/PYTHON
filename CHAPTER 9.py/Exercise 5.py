# This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from (i.e., the whole email
# address). At the end of the program, print out the contents of your dictionary.

file = open("mbox-short.txt")

domains = {}

for line in file:
    if line.startswith("From "):
        words = line.split()
        email = words[1]

        domain = email.split("@")[1]

        domains[domain] = domains.get(domain, 0) + 1

print(domains)