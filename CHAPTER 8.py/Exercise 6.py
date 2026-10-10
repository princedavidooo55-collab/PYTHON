# Rewrite the program that prompts the user for a list of numbers and prints out the
# maximum and minimum of the numbers at the end when the user enters “done”.
# Write the program to store the numbers the user enters in a list and use the max()
# and min() functions to compute the maximum and minimum numbers after the loop completes.

numbers = []

while True:
    user_input = input("Enter a number: ")

    if user_input == "done":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except:
        print("Invalid input")

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))