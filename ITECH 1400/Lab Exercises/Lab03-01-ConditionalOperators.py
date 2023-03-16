# Define and initialise two variables with integer data
print("\nWelcome to Conditional Operators\n")
num1 = int(input("Please input your first number: "))
num2 = int(input("Please input your second number: "))

# Display the value of our two variables
print("num1 is {0}, and num2 is {1}".format(num1, num2) )
print("------------------------")

# Less than
if (num1 < num2):
    # If num1 is less than num2 this block executes...
    print("num1 is less than num2.")
else:
    # ...otherwise this block executes
    print("num1 is not less than num2.")

# Less than or equal to
if (num1 <= num2):
    # If num1 is less than or equal to num2 this block executes...
    print("num1 is less than or equal to num2.")
else:
    # ...otherwise this block executes
    print("num1 is not less than or equal to num2.")

# Greater than
if (num1 > num2):
    # If num1 is greater than num2 (i.e. more than) then this block executes...
    print("num1 is greater than num2.")
else:
    # ...otherwise this block executes
    print("num1 is not greater than num2.")
# Greater than or equal to
if (num1 >= num2):
    # If num1 is greater than or equal to num2 then this block executes...
    print("num1 is greater than or equal to num2.")
else:
    # ...otherwise this block executes
    print("num1 is not greater than or equal to num2.")

# Equal to
if (num1 == num2):
    # If num1 is equal to num2 then this block executes...
    print("num1 is equal to num2.")
else:
    # ...otherwise this block executes
    print("num1 is not equal to num2.")

# Not equal to
if (num1 != num2):
    # If num1 is not equal to num2 then this block executes...
    print("num1 is not equal to num2.")
else:
    # ...otherwise (i.e. if num1 IS equal to num2) then this block executes
    print("num1 is NOT 'not equal to' num2 - so it must be EQUAL to num2!")
