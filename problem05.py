'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import time
start = time.time()
n = 20

nums =[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def divi(x):
	for i in nums:
		if x % i != 0:
			return False
	return True

while divi(n) == False:
	n = n+ 20


print (n)
elapsed = (time.time() - start)
print ("This took %s seconds" % (elapsed))