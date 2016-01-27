import sys

def readfile(file_name):
	if file_name == '':
		file_name = sys.argv[1]
	with open(file_name, 'r+') as f:
		lines =  [int(line.rstrip()) for line in f] # rstrip() can remove the '\n' in sting

 	return lines

def three_max(nums):
	print nums
	result = [0]*3
	for i in range(0, len(nums)):
		for j in range(0, len(result) - 1):
			if nums[i] > result[j]:
				result = [nums[i], result[j], result[j+1]]
				print result
				break

	return result



if __name__ == '__main__':
	print three_max(readfile("input.txt"))


