# Exercise1:Run the program on your system and see what numbers you get.Run
# the program morethan once and see what numbers you get.
for i in range(10):
x = random.random()
print(x)
0.3981375407938532
0.27283094038396527
0.24515343686068702
0.012992786446969551


# Exercise 2: Move the last line of this program to the top, so the function call
# appears before the definitions. Run the program and see what error message you get.

# Exercise 3: Move the function call back to the bottom and move the definition
# of print_lyrics after the definition of repeat_lyrics. What happens when you
# run this program?


# Exercise 4: What is the purpose of the “def” keyword in Python?
# The purpose of a "def" keyword in python
# a) It is slang that means “the following code is really cool”
# b) It indicates the start of a function
# c) It indicates that the following indented section of code is to be stored for later
# d) b and c are both true
# e) None of the above
# ans:  D ( b and c are both true)

# Exercise 5: What will the following Python program print out?
def fred():
print("Zap")

def jane():
print("ABC")

jane()
fred()
jane()