import unittest
import three_max

class TmaxTest(unittest.TestCase):
	def test1(self):
		Tmax = three_max.three_max
		self.assertEqual(Tmax("input.txt"), ['9239', '8723', '6421'])

	def test2(self):
		Tmax = three_max.three_max
		self.assertEqual(Tmax("input.txt"), ['923', '872', '642'])

if __name__ == '__main__':
	unittest.main()