import sys
import string

def readfile(file_name):
	if file_name == '':
		file_name = sys.argv[1]
	with open(file_name, 'r+') as f:
		tmp = f.readline()
		lines = [word.strip('"') for word in tmp.split(',')]
	return lines


def name_score(lines):
	score = [0] * len(lines)
	total_score = 0
	lines.sort()

	for i, word in enumerate(lines, 0):
		score[i] = sum([ord(x) - 64 for x in word])

	total_score = sum([(i + 1) * score[i] for i in range(0, len(score))])

	return total_score

if __name__ == '__main__':
	print name_score(readfile("input2.dat"))
