def is_perfect(number):
	return number == sum([i for i in xrange(1, number//2 + 1) if number % i == 0])
print(is_perfect(28))
