"""CSC148 Exercise 7: Recursion Wrap-Up

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Exercise 7.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<http://www.teach.cs.toronto.edu/~csc148h/fall/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
import unittest
from ex7 import kth_smallest, anagrams
from hypothesis import given
from hypothesis.strategies import integers, lists


class KthSmallestTest(unittest.TestCase):

    def test_sorted(self):
        sorted_list = list(range(0, 1000, 10))
        for i in range(100):
            self.assertEqual(kth_smallest(sorted_list, i), i * 10)

    def test_empty(self):
        self.assertRaises(IndexError, kth_smallest, [], 0)

    @given(lists(integers(), min_size=1, unique=True))
    @given(integers(min_value=0, max_value=10000))
    def test_correct_given_valid_k(self, lst, index):
        k = index % len(lst)
        self.assertEqual(kth_smallest(lst, k), sorted(lst)[k])


class AnagramsTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(anagrams(''), [''])

    def test_dormitory(self):
        self.assertEqual(anagrams('dormitory'),
                         ['dirty room', 'dormitory', 'room dirty'])


if __name__ == '__main__':
    unittest.main(exit=False)
