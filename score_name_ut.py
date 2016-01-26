import unittest
import name_score

class NameScoreTest(unittest.TestCase):
	def test1(self):
		read = name_score.readfile
		Nscor = name_score.name_score
		self.assertEqual(Nscor(read("input2.dat")), 150)

	def test2(self):
		read = name_score.readfile
		Nscor = name_score.name_score
		self.assertEqual(Nscor(read("input2.dat")), 100)

if __name__ == '__main__':
	unittest.main()
