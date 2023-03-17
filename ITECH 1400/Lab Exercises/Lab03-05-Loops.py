print("\nWelcome to Loops Exercise\n")

user_name = input("Please input your name: ")

print("\nSECTION 1 - Print name 10x using FOR LOOP")
for i in range(10):
    print(user_name)


print("\nSECTION 2 - Print name 10x using WHILE LOOP")
ctr = 0
while (ctr<10):
    print(user_name)
    ctr += 1

print("\nSECTION 3 - Print name 10x using DO WHILE LOOP implementation in python")
ctr = 0
while (True):
    print(user_name)
    ctr += 1
    if (ctr==10):
        break