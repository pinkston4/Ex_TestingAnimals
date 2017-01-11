import unittest
from animals import *

class TestDog(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		print('set up class')
		self.dog = Dog(Animal)

	def test_isDogInstanceOfDog(self):
		self.assertIsInstance(self.dog, Dog)

if __name__ == '__main__':
	unittest.main()