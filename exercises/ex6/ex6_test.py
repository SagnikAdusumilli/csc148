"""CSC148 Exercise 6: Binary Search Trees

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Exercise 6.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<http://www.teach.cs.toronto.edu/~csc148h/fall/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
import unittest
from ex6 import BinarySearchTree


class BSTNumLessThanTest(unittest.TestCase):
    def test_one(self):
        bst = BinarySearchTree(1)
        self.assertEqual(bst.num_less_than(10), 1)
        self.assertEqual(bst.num_less_than(0), 0)

    def test_bigger(self):
        bst = BinarySearchTree(1)
        bst._left = BinarySearchTree(-10)
        bst._right = BinarySearchTree(100)
        self.assertEqual(bst.num_less_than(5), 2)
        self.assertEqual(bst.num_less_than(-100), 0)
        self.assertEqual(bst.num_less_than(1000), 3)


class BSTItemsTest(unittest.TestCase):
    def test_one(self):
        bst = BinarySearchTree(1)
        self.assertEqual(bst.items_at_depth(1), [1])

    def test_empty(self):
        bst = BinarySearchTree(None)
        self.assertEqual(bst.items_at_depth(1), [])


class BSTLevelsTest(unittest.TestCase):

    def test_one(self):
        bst = BinarySearchTree(1)
        self.assertEqual(bst.levels(), [(1, [1])])


if __name__ == '__main__':
    unittest.main(exit=False)
