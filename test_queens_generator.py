import unittest
from queens import queens
import types


class TestQueensGenerator(unittest.TestCase):

    def test_generator(self):
        self.assertTrue(isinstance(queens(4), types.GeneratorType))


if __name__ == '__main__':
    unittest.main()
