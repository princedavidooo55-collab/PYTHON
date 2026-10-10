# Rewrite your pay program using try and except so that your program 
# handles non-numeric input gracefully by printing a message and exiting the
# program. 
try:
        hours = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
        if hours <= 40:
                pay = hours * rate
        else:
                regular_pay = 40 * rate
                overtime_pay = (hours - 40) * rate *1.5
                pay = regular_pay + overtime_pay
                print("Pay:", pay)
except:
        print("Error, please enter numeric input")