n = 12 #13195
f = 0
i = 1

while i <= n:
	if n % i == 0:
		f = n / i
		print(f)
	i = i + 1
