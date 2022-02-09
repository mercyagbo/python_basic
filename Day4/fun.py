def get_hours():
    while True:
        try:
            hours = float(input("Please enter your hours for this week: "))
            if hours < 0 or hours > 65:
                raise ValueError()
            break
        except ValueError:
            print("You did not enter a valide value for hours: Try again:")
    return hours


def get_rate():
    while True:
        try:
            rate = float(input("Please enter your hourly rate: "))
            if rate < 7.50 or rate > 50:
                raise ValueError()
            break
        except ValueError:
            print("You did not enter a valide value for rate: Try again:")
    return rate

def pay_calculator(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        overtime_rate = rate * 1.5
        overtme_hours = hours - 40
        pay = (40 * rate) + overtime_rate * overtme_hours
    return pay

def main():
    print("hello from fun")
