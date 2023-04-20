def babylon_sqrt(n, guess, iterations):
    print(f"guess: {guess:<20} iterations: {iterations}")
    next_guess = (guess + (n/guess))/2
    if (iterations == 0 or guess == next_guess):
        return guess
    else:
        return babylon_sqrt(n, next_guess, iterations-1)
    

n = 9
guess = 9
iterations = 20
print(f"\nSquareroot of {n} is {babylon_sqrt(n, guess, iterations)}")