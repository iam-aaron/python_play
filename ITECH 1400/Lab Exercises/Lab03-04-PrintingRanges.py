
list_1 = [] #0 to 10 inclusive (i.e. including the final 10 value)
for i in range(10+1):
    list_1.append(i)

print("\nPART 1 - 0 to 10 inclusive (i.e. including the final 10 value)")
print(list_1)

list_2 = [] #50 to 74 with a step-size of 1
for i in range(50,74):
    list_2.append(i)

print("\nPART 2 - 50 to 74 with a step-size of 1")
print(list_2)

list_3 = [] #50 to 90 with a step size of 5 (make sure the final 90 value is included!)
for i in range(50,90+1,5):
    list_3.append(i)

print("\nPART 3 - 50 to 90 with a step size of 5 (make sure the final 90 value is included!)")
print(list_3)

list_4 = [] #30 to 0 inclusive with a step-size of -6 (minus six)
for i in range(30,-1,-6):
    list_4.append(i)

print("\nPART 4 - 30 to 0 inclusive with a step-size of -6 (minus six)")
print(list_4)
