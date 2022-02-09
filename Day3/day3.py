# example
from black import main


def wageCalculator():    
    while True:
        try:
            hours = float(input("Enter hours worked this week: "))
            if hours > 60 or hours < 0:
                raise ValueError("You entered an illegal value for hours")
            
            break 
        except ValueError as error:
            print(error)


    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            if rate < 10 or rate > 50:
                raise ValueError("You entered an illegal value for rate!")
            break 
        except ValueError as error:
            print(error)

    print(hours)
    print(rate)
    name = input("please enter your name: ")

    overtime_rate = rate*1.5

    if hours <= 40: # if the user worked less than 40hrs 
        pay = rate * hours
    elif hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * overtime_rate
        pay = (40 * rate) + overtime_pay
    print(name + " week's pay is: " + "$" + str(pay))

wageCalculator()
