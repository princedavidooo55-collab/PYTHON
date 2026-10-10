# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. 
# Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

fname = input("Enter file name: ")

fh = open(fname)

total = 0
count = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        value = float(line.split(":")[1])
        total = total + value
        count = count + 1

average = total / count

print("Average spam confidence:", average)