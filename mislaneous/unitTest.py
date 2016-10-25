import unittest

from Ramp_up.testme import is_even
from Ramp_up.testme import findGreater


class TestDocTest(unittest.TestCase):
    def test_isEven(self):
        self.assertTrue(is_even(1000))

    def test_findGreater(self):
        self.assertEqual(findGreater(1,2),2)

if __name__ == '__main__':
    unittest.main(exit= "False")
