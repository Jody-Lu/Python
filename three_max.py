import sys

def readfile(file_name):
	if file_name == '':
		file_name = sys.argv[1]
	with open(file_name, 'r+') as f:
		numbers =  [int(number.rstrip()) for number in f] # rstrip() can remove the '\n' in sting

 	return numbers

def three_max(numbers):
	result = [0]*3
	for index in range(0, len(numbers)):
		if numbers[index] > result[0]:
			result.insert(0, numbers[index])
			result.pop()

	return result



if __name__ == '__main__':
	print three_max(readfile("input.txt"))


