import unittest
import perfect_number

class perfNumTest(unittest.TestCase):
	def test1(self):
		perfN = perfect_number.is_perfect
		self.assertEqual(perfN(6), True)

	def test2(self):
		perfN = perfect_number.is_perfect
		self.assertEqual(perfN(8), False)

	def test3(self):
		perfN = perfect_number.is_perfect
		self.assertEqual(perfN(28), False)


if __name__ == '__main__':
	unittest.main()