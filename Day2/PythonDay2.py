# %% [markdown]
# ## String Conversion
# * You can convert a string to a number by using the int() function. you will get an error if you try to convert a string that contains a non-numeric character.
# * You can convert a string to a float by using the float() function. You will get an error if you try to convert a string that contains a non-numeric character.
# * You can convert any data type to a string by using the str() function.
# 

# %%
# adding two strings
number = "1" # is a string
print(number + "2") # We are concatenating a string with a string that is adding a string to a string


# %%
number = "1" # is a string
print(number + 2) # We are concatenating a string with a number that is adding a string to a number will fail
                  # because the number is not a string so cannot concatenated(add) number and a string.
# To fix this we can convert the number to a integer using int() function if you want tpo add those two numbers
print(int(number) + 2) # We are adding the variable number to 2 and the result is 3 the type is temporaryconverted to integer

# %%
number = 1 # is an integer
print(number + 2) # We are adding an integer with an integer that is adding an integer to an integer

# %%
number = "1.0" # is a string
# This is a string that can be converted to a float
print(float(number) + 2) # We are adding the variable number to 2 and the result is 3.0 the type is temporaryconverted to float

# %%
# str() function converts float and int to a string
amount = 250.0 # is a float
print(str(amount) + " dollars") # We are adding the variable amount to " dollars" and the result is "250.0 dollars"
# to add the $ sign to the amount we can use the str() function
print(str(amount) + "$") # We are adding the variable amount to "$" and the result is "250$"
# or 
print("$" + str(amount)) # We are adding the variable amount to "$" and the result is "$250"

# %% [markdown]
# ## User Input
# * You can get user input by using the input() function.
# * By default, the input() function will return a string.
# * You can get user input and convert it to a number by using the int() function.
# * You can get user input and convert it to a float by using the float() function.
# 

# %%
# Using the input() function to ask the user for input
name = input("What is your name? ") # We are asking the user for input and storing it in the variable name
number = input("What is your age? ") # We are asking the user for input and storing it in the variable number

# %%
# checking the variable name type
print(name)
print(type(name)) # We are printing the type of the variable name

print("-------------------checking the number variable-----------------------------")
# checking the variable number type
print(number)
print(type(number)) # We are printing the type of the variable number


# %%
print("Hello " + name) # We are adding the variable name to "Hello" and the result is "Hello John"

# %% [markdown]
# Excercise:
# * Ask the user for their name and age. and convert their age to a number.

# %%
age = input("What is your age? ")
print("You entered " + age) 
print(type(age))


# %%
# solutiion 1
ageInt = int(age) # We are converting the variable age to an integer
print(type(ageInt))

# %%
# solution 2
age = int(age) # We are converting the variable age to an integer
print(type(age))
print(age)

# %%
# solution 3
age = int(input("What is your age? ")) # We are asking the user for input and storing it in the variable age
print(age)
print(type(age))

# %% [markdown]
# ## Conditional Execution
# ## Mathematical Operators for Comparison
# * The comparison operators are used to compare two values.
# * These operators return a boolean value.
# * The comparison operators are:
# * == (equal to): we check if the values are equal.
# * != (not equal to): we check if the values are not equal.
# * < (less than)
# * `>` (greater than)
# * <= (less than or equal to)
# * `>`= (greater than or equal to)
# Note:   
# * = operator is used to assign a value to a variable. not used to compare values.

# %%
x = 6

# %%
 # This is an assignment statement we are telling the computer to store the value 6 in the variable x
if x == 6: # This is an if statement we are telling the computer to check if the value of x is equal to 6
    print("x is 6")
    print("The condition is true")

# %%
if x < 6: # This is an if statement we are telling the computer to check if the value of x is less than 6
    print("x is less than 6")
    print("The condition is true")

# this code will not run because the condition is false

# %%
if x >= 6: # This is an if statement we are telling the computer to check if the value of x is greater than or equal to 6
    print("x is greater than or equal to 6")
    print("The condition is true")

# %%
getNumber = int(input("Enter a number: "))

print("I will tell you if the number is positive or negative")

if getNumber < 0:
    print("the number is negative")
elif getNumber > 0:
    print("the number is positive")

# %% [markdown]
# Excercise:
# * Ask the user for the number of hours they worked this week.
# * Ask the user for their hourly rate.
# * Calculate their weekly pay.
# * if the user worked more than 40 hours, calculate their overtime pay.
# * overtime pay is 1.5 times the hourly rate for the hours worked above 40.
# * print out their name and pay.
# 
# Remeber:
#     input() returns a string. you must hours and rate to the appropriate data type.

# %%
hours = input("Enter hours worked this week: ") # We are asking the user for input the hours worked  and storing it in the variable hours
rate = input("Enter your pay rate: ")
name = input("please enter your name: ")
hours = float(hours)
rate = float(rate)
overtime_rate = rate*1.5

if hours <= 40: # if the user worked less than 40hrs 
    pay = rate * hours
elif hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * overtime_rate
    pay = (40 * rate) + overtime_pay
print(name + " week's pay is: " + "$" + str(pay))
    



