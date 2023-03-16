print("\nWelcome to Conditional AND Exercise\n")

with_license = input("Do you have a driver's license (Y/N)?").upper() == 'Y'
with_car = input("Do you have a car (Y/N)?").upper() == 'Y'

if (with_license and with_car):
    print("\nLet's go for a spin!\n")
else:
    print("\nWalking it is.\n")