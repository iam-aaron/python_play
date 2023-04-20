import time

while True:
    try:
        # some code that may raise an exception
        divisor = int(input("Enter a number to divide 10 by: "))
        print(10 / divisor)
        break  # exit the loop if successful
    except ZeroDivisionError:
        print("You can't divide by zero!")
        # wait for a few seconds before retrying
        time.sleep(5)
    except ValueError:
        print("You must enter a number!")
        # wait for a few seconds before retrying
        time.sleep(5)