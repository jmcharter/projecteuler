'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of 
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''
import time
start = time.time()

sumsqr = []

for x in range (1, 101):
	sumsqr.append(x)

a = (sum(sumsqr)**2)
print(a)

sqrsum = []

for x in range (1, 101):
	sqrsum.append(x**2)

b =(sum(sqrsum))
print(b)

answer = (a-b)
print(answer)
elapsed = time.time() - start



print("This took %s seconds" % elapsed)
