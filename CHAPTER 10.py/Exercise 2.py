# This program counts the distribution of the hour of the day for each
# of the messages. You can pull the hour from the “From” line by finding the time
# string and then splitting that string into parts using the colon character. Once
# you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below

file = open("mbox-short.txt")

hours = {}

for line in file:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]

        hours[hour] = hours.get(hour, 0) + 1

# Sort by hour and print
for hour in sorted(hours):
    print(hour, hours[hour])