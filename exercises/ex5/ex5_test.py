"""CSC148 Exercise 5: Tree Practice

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Exercise 5.

NOTE: the hypothesis tests here use some helper functions to create
random instances of the data types we want (trees and binary trees).
We've provided helper functions to do this -- you don't need to
understand how they work, but we do encourage you to use them to
write your own hypothesis tests.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<http://www.teach.cs.toronto.edu/~csc148h/fall/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
import unittest
from hypothesis import given, assume
from hypothesis.strategies import integers, lists, recursive, builds, just

from ex5 import Tree, to_tree, BinaryTree


##############################################################################
# Helper functions
##############################################################################
def _binary_tree_size(bt):
    """Return the size of the given binary tree.

    @type bt: BinaryTree
    @rtype: int
    """
    if bt.is_empty():
        return 0
    else:
        return 1 + _binary_tree_size(bt._left) + _binary_tree_size(bt._right)


def _tree_size(t):
    """Return the size of the given tree.

    @type t: Tree
    @rtype: int
    """
    if t.is_empty():
        return 0
    else:
        s = 1
        for subtree in t._subtrees:
            s += _tree_size(subtree)
        return s


def item():
    """Generate an integer between -10000 and 10000."""
    return integers(min_value=-10000, max_value=10000)


def single_root():
    """Generate a tree with a single node.

    The root value is an integer between -10000 and 10000.
    """
    return builds(Tree,
                  item(),
                  just([]))


def trees():
    """Generate a non-empty tree with integer items between -10000 and 10000."""
    return recursive(single_root(),
                     lambda children:
                         builds(Tree,
                                item(),
                                lists(children)))


def bt_empty():
    """Generate an empty BinaryTree."""
    return just(BinaryTree(None, None, None))


def binary_trees():
    """Generate a BinaryTree with integer items between -10000 and 10000."""
    return recursive(bt_empty(),
                     lambda s: builds(BinaryTree, item(), s, s))


##############################################################################
# Helper functions (Hypothesis custom strategies)
##############################################################################
class TreeEqTest(unittest.TestCase):
    @given(trees())
    def test_tree_equals_itself(self, tree):
        self.assertTrue(tree == tree)

    def test_empty(self):
        tree1 = Tree(1, [])
        tree_emp = Tree(None, [])
        tree_emp2 = Tree(None, [])
        self.assertFalse(tree_emp == tree1)
        self.assertFalse(tree1 == tree_emp)
        self.assertTrue(tree_emp == tree_emp2)


class ToNestedListTest(unittest.TestCase):
    def test_one(self):
        t = Tree(1, [])
        self.assertEqual(t.to_nested_list(), [1])

    def test_list(self):
        t5 = Tree(5, [])
        t4 = Tree(4, [t5])
        t3 = Tree(3, [t4])
        t2 = Tree(2, [t3])
        t1 = Tree(1, [t2])

        self.assertEqual(t1.to_nested_list(), [1, [2, [3, [4, [5]]]]])


class ToTreeTest(unittest.TestCase):
    def test_one(self):
        t = to_tree([1])
        self.assertEqual(t._root, 1)
        self.assertEqual(t._subtrees, [])

    def test_line(self):
        t = to_tree([10, [2], [4], [5], [3]])
        self.assertEqual(t._root, 10)
        self.assertEqual(t._subtrees[0]._root, 2)
        self.assertEqual(t._subtrees[1]._root, 4)
        self.assertEqual(t._subtrees[2]._root, 5)
        self.assertEqual(t._subtrees[3]._root, 3)
        self.assertEqual(_tree_size(t), 5)


class TestTraversals(unittest.TestCase):
    def test_empty(self):
        btree = BinaryTree(None, None, None)
        self.assertEqual(btree.preorder(), [])
        self.assertEqual(btree.postorder(), [])
        self.assertEqual(btree.inorder(), [])

    @given(binary_trees())
    def test_root_position(self, btree):
        assume(not btree.is_empty())
        self.assertEqual(btree.preorder()[0], btree._root)
        self.assertEqual(btree.postorder()[-1], btree._root)

    @given(binary_trees())
    def test_orders_have_correct_length(self, btree):
        pre_len = len(btree.preorder())
        in_len = len(btree.inorder())
        post_len = len(btree.postorder())
        self.assertEqual(pre_len, _binary_tree_size(btree))
        self.assertEqual(in_len, _binary_tree_size(btree))
        self.assertEqual(post_len, _binary_tree_size(btree))


if __name__ == '__main__':
    unittest.main(exit=False)
