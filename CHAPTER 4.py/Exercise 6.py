# Rewrite your pay computation with time-and-a-half for overtime and
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