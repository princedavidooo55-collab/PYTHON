# Exercise 1: Write a program which repeatedly reads integers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of the
# integers. If the user enters anything other than an integer, detect their mistake
# using try and except and print an error message and skip to the next integers

total = 0
count = 0

while True:
        number = input("Enter a number: ")

        if number == "done":
                break
        try:
                num = int(number)
                total = total + num
                count = count + 1
        except:
                print("Invalid input")
                continue

        average = total/count

        print("Total:", total)
        print("Count:", count)
        print("Average:", average)



# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.