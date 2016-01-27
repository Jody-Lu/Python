import sys

def readfile(file_name):
	if file_name == '':
		file_name = sys.argv[1]
	with open(file_name, 'r+') as f:
		numbers =  [int(number.rstrip()) for number in f] # rstrip() can remove the '\n' in sting

 	return numbers

def three_max(numbers):
	result = [0]*4
	for index in range(len(numbers)):
		result[-1] = numbers[index]

		for j in range(len(result) - 1, 0, - 1):
			if result[j] > result[j - 1]:
				result[j], result[j - 1] = result[j - 1], result[j]
			else:
				break


	return result[:len(result) - 1]



if __name__ == '__main__':
	print three_max(readfile("input.txt"))



