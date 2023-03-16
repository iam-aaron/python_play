print("\nWelcome to Conditional OR Exercise\n")

go_lunch = input("Do you want to go out for lunch (Y/N)?").capitalize()[0:1] == 'Y'

if (go_lunch):
    print("\nCool! You’re paying!\n")
else:
    print("\nBah! Beans on toast again.\n")