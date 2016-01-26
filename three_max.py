with open("input.txt", 'r+') as f:
	lines = [line[:-1] for line in f]
	lines.sort()
	lines.reverse()

for i in range(0,3):
	print lines[i]


