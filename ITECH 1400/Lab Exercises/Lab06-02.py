import logging

class BadNumberException(Exception):
    pass

def babylon_sqrt(n, guess, iterations):
    if (n < 0 or guess < 0 or iterations < 0):
        print("IN HERE!")
        raise BadNumberException("\x1b[31mERROR: n, guess, and iterations MUST BE INTEGERS GREATER THAN 0!\x1b[0m")

    print(f"guess: {guess:<20} iterations: {iterations}")
    next_guess = (guess + (n/guess))/2
    if (iterations == 0 or guess == next_guess):
        return guess
    else:
        return babylon_sqrt(n, next_guess, iterations-1)
    

n = -9
guess = 9
iterations = 20
print(f"\nSquareroot of {n} is {babylon_sqrt(n, guess, iterations)}")