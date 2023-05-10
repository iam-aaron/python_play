from fractions import Fraction
import logging

logging.basicConfig(level=logging.DEBUG,format='\x1b[33m%(asctime)s [%(levelname)s] - %(message)s\x1b[0m',)
logging.debug('Start of program')

fraction_sum = 0
seq_size = 10
for i in range(1, seq_size+2): # 1/2 is excluded in the sequence size
    denom = 2**i
    fraction_sum += Fraction(1, denom)
    logging.debug(f"{i} {denom}")

print(f"\nThe sum of the fraction with {seq_size} is: {fraction_sum}\n")
logging.debug('End of program')








