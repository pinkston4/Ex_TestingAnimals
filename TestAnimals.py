import unittest
from animals import *

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('set up class')
        self.animal = Animal()

    def test_AnimalHasCorrectNameProp(self):
        self.assertEqual(self.animal.name, None)

    def test_speciesPropHasCorrectValueWhenSet(self):
        self.animal.set_species('lion')
        self.assertEqual(self.animal.species, 'lion')

    def test_invokeWalkSetSpeed(self):
        self.animal.set_legs(4)
        self.animal.walk()
        self.assertEqual(self.animal.speed, 0.4)

    def test_isAnimalInstanceOfAnimal(self):
        self.assertIsInstance(self.animal, Animal)

if __name__ == '__main__':
    unittest.main()