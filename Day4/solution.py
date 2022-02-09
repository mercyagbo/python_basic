import fun
def main():
    names = ["Bob", "Sue", "Joe", "Mary", "James"]
    hours = [30, 45, 50, 40, 35]
    rates = [30, 45, 50, 40, 35]
    index = 0
    for hour in hours:
       pay = fun.pay_calculator(hour, rates[index])
       print(names[index] + " Weeks pay is : $" +str(pay))
       index = index + 1

if __name__ == '__main__':
    main()
