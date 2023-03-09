import datetime as dt

print("Hello, user! Welcome to our lab. We will be needing a couple of information from you\n\n")
input("Press any key to continue...")

birth_year = int(input("\nPlease input your BIRTH YEAR: "))
birth_month = int(input("Please input BIRTH MONTH: "))
birth_day = int(input("Please input BIRTH DAY: "))

date = dt.date(birth_year, birth_month, birth_day) # Create a date from user data
formattedDate = date.strftime("%d/%m/%Y")
day_of_year = date.timetuple().tm_yday             # Get day number from date


print("If you were born",formattedDate,"then that was day",day_of_year,"of the year.\n")
