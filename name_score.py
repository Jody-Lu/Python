import sys
import string

def readfile(file_name):
	if file_name == '':
		file_name = sys.argv[1]
	with open(file_name, 'r+') as f:
		tmp = f.readline()
		names = [word.strip('"') for word in tmp.split(',')]
	return names


def name_score(names):
	names.sort()
	total_score = sum([sum([ord(x) - 64 for x in name]) \
					* (i + 1) for i, name in enumerate(names, 0)])

	return total_score



if __name__ == '__main__':
	print name_score(readfile("input2.dat"))
