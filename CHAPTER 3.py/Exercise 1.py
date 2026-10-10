# Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.
hours= float(input("Enter Hours: "))
rate= float(input("Enter Rate: "))
if hours <= 40:
        pay = hours * rate
else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        pay = regular_pay + overtime_pay
print("Pay:", pay)