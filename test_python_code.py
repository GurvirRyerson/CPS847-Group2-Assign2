import unittest
from code_to_test import multiply_numbers, sum_numbers


class SimpleTests(unittest.TestCase):
	def test_sum(self):
		list_of_nums = []
		for i in range(0,9):
			for j in range(0,9):
				self.assertEqual(sum_numbers(list_of_nums), sum(list_of_nums))
				list_of_nums.append(j)

	def test_multiply(self):		
		for i in range(0,9):
			for j in range(0,9):
				self.assertEqual(multiply_numbers(i,j), i*j)


if __name__ == "__main__":
	#Retesting code coverage 
	unittest.main()
