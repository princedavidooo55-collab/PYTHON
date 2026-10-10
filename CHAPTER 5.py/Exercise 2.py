# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

largest = None
smallest = None

while True:
    number = input("Enter a number: ")

    if number == "done":
        break

    try:
        number = int(number)

        if largest is None or number > largest:
            largest = number

        if smallest is None or number < smallest:
            smallest = number

    except:
        print("Invalid input. Please enter an integer.")

print("Maximum:", largest)
print("Minimum:", smallest)