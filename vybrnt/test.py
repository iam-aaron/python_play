def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(i)
        a, b = b, a + b
    return a

print(fibonacci(10))