import sys

def three_max(in_file):
	if in_file == '':
		in_file = sys.argv[1]

	with open(in_file, 'r+') as f:
		lines = [line[:-1] for line in f]
		result = []
		max_1 = max(lines)
		max_2 = max(n for n in lines if n != max_1)
		max_3 = max(n for n in lines if n != max_2 and n != max_1)
		result = [max_1, max_2, max_3]
	return result


