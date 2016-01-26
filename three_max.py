with open("input.txt", 'r+') as f:
	lines = [line[:-1] for line in f]

for i in range(0,3):
	print lines[i]


