# Write a program which repeatedly reads integers until the user enters integers   If the user enters anything other than an integer,detect their mistake “done”. Once “done” is entered, print out the total,count, and average of the
# using try and except and print an error message and skip to the next integers.  

total = 0
count = 0

while True:
    number = input("Enter a number: ")

    if number == "done":
        break

    try:
        number = int(number)
        total = total + number
        count = count + 1
    except:
        print("Invalid input. Please enter an integer.")

if count > 0:
    average = total / count
else:
    average = 0

print("Total:", total)
print("Count:", count)
print("Average:", average)