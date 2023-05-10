#create a function that prints the factoriak of a number example 4! = 4 x 3 x 2 x 1

def factorial(n):
    if n == 1:
        return "1"
    else:
        return f"{n} X {factorial(n-1)}" 
n = 4
print(f"{n}! = {factorial(4)}")