import logging

logging.basicConfig(level=logging.DEBUG,format='\x1b[33m%(asctime)s [%(levelname)s] - %(message)s\x1b[0m',)
logging.debug('Start of program')

class BadNumberException(Exception):
    logging.debug('Start of BadNumberException Class')
    pass

def babylon_sqrt(n, guess, iterations):
    if (n < 0 or guess < 0 or iterations < 0):
        logging.debug(f"n: {n} guess: {guess} iterations: {iterations}")
        raise BadNumberException("\x1b[31m[ERROR] n, guess, and iterations MUST BE INTEGERS GREATER THAN 0!\x1b[0m")
        logging.error('BadNumberException raised')

    logging.info(f"guess: {guess:<20} iterations: {iterations}")
    next_guess = (guess + (n/guess))/2
    if (iterations == 0 or guess == next_guess):
        return guess
    else:
        return babylon_sqrt(n, next_guess, iterations-1)
    

n = -9
guess = 9
iterations = 20
print(f"\nSquareroot of {n} is {babylon_sqrt(n, guess, iterations)}")

logging.debug('End of program')