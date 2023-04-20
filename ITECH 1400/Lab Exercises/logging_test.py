import logging

logging.basicConfig(level=logging.DEBUG,format='\x1b[31m%(asctime)s - %(levelname)s - %(message)s\x1b[0m',)
logging.debug('Start of program')

def factorial(n):
	logging.debug('Start of factorial ' + str(n))
	total = 1
	for i in range(1, n + 1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
	logging.debug('Final value: ' + str(total))
	return total
	
print( factorial(5) )
logging.debug('End of program')
