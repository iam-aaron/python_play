print("\nWelcome to Loops Exercise\n")

user_name = input("Please input your name: ")

print("\nSECTION 1 - Print name 10x using for loop")
for i in range(10):
    print(user_name)


print("\nSECTION 2 - Print name 10x using while loop")
ctr = 0
while (ctr<10):
    print(user_name)
    ctr += 1

print("\nSECTION 3 - Print name 10x using do while loop implementation in python")
ctr = 0
while (True):
    print(user_name)
    ctr += 1
    if (ctr==10):
        break