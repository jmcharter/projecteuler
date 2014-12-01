def FibonacciEvens(limit):
	fibo = [0, 1, 1]

	while fibo[-1] + fibo[-2] < limit:
		fibo.append(fibo[-1] + fibo[-2])
	fiboEven = [i for i in fibo if i%2==0]
	return(sum(fiboEven))

print (FibonacciEvens(4000000))