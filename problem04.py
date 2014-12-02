'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

min = 100
max = 999

pali = []

for a in range(min, max+1):
	for b in range(min, max+1):
		if str(a*b) == str(a*b)[::-1]:
			p = a*b
			pali.append(p)

pali.sort()
print(pali[-1]) 
