# Exercise 1: Type the following statements in the Python interpreter to see what they do:
5
x = 5
x + 1

# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
  name = input("enter your name here:\n")
  welcome = "Hello " + name
  print(welcome)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
 h = input('Enter hours:/n')
 r =  input('Enter rate:/n')
 hours= float(h)
  rate= float(r)
 pay= hours * rate
 print(pay) 
 

# Exercise 4: Assume that we execute the following assignment statements:
 # width = 17
 # height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
    width = 17
    height = 12.0
print(width//2)
print(width/2.0)
print(height/3)
print(1 + 2 * 5)

# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.
 celsius = float(input("Enter Celsius temperature:"))
 fahrenheit = ( celsius* 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
