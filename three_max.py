import sys

def readfile(file_name):
	if file_name == '':
		file_name = sys.argv[1]
	with open(file_name, 'r+') as f:
		lines = [line[:-1] for line in f]
	return lines

def three_max(lines):
	tmp = lines
	result = ['']*3
	result[0] = max(tmp)

	del tmp[tmp.index(max(tmp))]

	if tmp[0] > tmp[1]:
		result[1], result[2] = tmp[0], tmp[1]
	else:
		result[1], result[2] = tmp[1], tmp[0]

	for x in tmp[2:]:
		if x > result[2]:
			if x > result[1]:
				result[2], result[1] = result[1], x
			else:
				result[2] = x
	return result


