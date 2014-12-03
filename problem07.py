'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import time
start = time.time()

def isItPrime(x):
	for i in range(2, x):
		if x%i == 0:
			return False
	return True

def primeN(n):
	prime = 2
	count = 1
	step = 3

	while count < n:
		if isItPrime(step):
			prime = step
			count += 1	
		step += 2	
	return prime

print (primeN(10001))


elapsed = time.time() - start

print ("This took %s seconds" % elapsed)