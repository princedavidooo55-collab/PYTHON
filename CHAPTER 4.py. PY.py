# Exercise1:Run the program on your system and see what numbers you get.Run
# the program more than once and see what numbers you get.

for i in range(10):
x = random.random()
print(x)
0.3981375407938532
0.27283094038396527
0.24515343686068702
0.012992786446969551


# Exercise 2: Move the last line of this program to the top, so the function call
# appears before the definitions. Run the program and see what error message you get.

repeat_lyrics()

def print_lyrics():
        print("I'm a lumberjack, and I'm okay.")
        print('I sleep all night and I work all day.')

 def repeat_lyrics():
        print_lyrics()
        print_lyrics()

# Exercise 3: Move the function call back to the bottom and move the definition
# of print_lyrics after the definition of repeat_lyrics. What happens when you
# run this program?

def repeat_lyrics():
        print_lyrics()
        print_lyrics()

def print_lyrics():
        print("I'm a lumberjack, and I'm okay.")
        print('I sleep all night and I work all day.')

repeat_lyrics()

# When i run the program, it printed the lyrics twice 


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

# d) ABC Zap ABC

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def compute_pay(hours, rate):
       if hours> 40:
              regular = 40 * rate
              overtime = (hours - 40) * rate * 1.5
              return regular + overtime 
       else:
              return hours * rate

       hours = float(input("Enter Hours: "))
       rate =  float(input("Enter Rate: "))
       pay = compute_pay(hours, rate)
       print("Pay:", pay)

# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a string.
Score   Grade
>= 0.9   A
>= 0.8   B
>= 0.7   C
>= 0.6   D
< 0.6    F

def computergrade(score):
       if score >= 0.9:
              return "A"
       elif score >= 0.8:
              return "B"
       elif score >= 0.7:
              return "C"
       elif score >= 0.6:
              return "D"
       else:
              return "F"

       score = float(input("Enter score: "))

       grade = computergrade(score)
       print(grade)
       

