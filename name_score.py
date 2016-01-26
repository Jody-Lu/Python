import sys
import string

def readfile(file_name):
	if file_name == '':
		file_name = sys.argv[1]
	with open(file_name, 'r+') as f:
		tmp = f.readline()
		lines = tmp.split(',')
	return lines


def name_score(lines):
	score = [0]*len(lines)
	total_score = 0
	lines.sort()
	for word, i in zip(lines, range(0,3)):
		words = list(word[1: len(word) - 1])
		for x in words:
			score[i] += (ord(x) - 64)
	for i in range(0, len(score)):
		total_score += (i+1)*score[i]

	return total_score

print name_score(readfile("input2.dat"))
