import unittest
from queens import generator_size
from functools import reduce


class TestQueensGeneratorSize(unittest.TestCase):

    def test_size(self):
        self.assertEqual(0, generator_size([]))
        self.assertEqual(1337, generator_size(range(1337)))


if __name__ == '__main__':
    unittest.main()
