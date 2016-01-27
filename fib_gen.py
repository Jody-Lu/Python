def fib():
	a = 1
	yield a
	b = 1
	yield b

	while 1:
   		c = a + b
    	yield c
    	a, b = b, c
