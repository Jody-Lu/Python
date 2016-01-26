def is_perfect(number):
	sum = 0
	for i in xrange(1, number):
		if (number % i == 0):
			sum += i;
	return sum == number

#print(is_perfect(8))