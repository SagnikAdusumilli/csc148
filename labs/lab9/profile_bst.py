"""Lab 9: Binary Search Trees

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains some code for running some timing experiments on
binary search trees.

You'll want to review the documentation of the timer.py module for this part.
"""
import random
import sys

from bst import BinarySearchTree
from timer import Timer


def profile_bst(lst):
    """Print the time an empty BinarySearchTree takes to insert items from
    <lst>, and the time it takes to then delete items from <lst>.

    Note: you'll need to first create your own BinarySearchTree here,
    and then call insert and delete on it.

    @type lst: list
    @rtype: None
    """
    # TODO: implement this function!
    # Note: first, insert ALL the items in <lst> into an empty BST.
    # Then, delete them all.
    pass


if __name__ == '__main__':
    # Python limits recursion by default. Don't change this line!
    sys.setrecursionlimit(10000)

    SIZES = [500, 1000, 2000, 4000]

    # Sorted insert and delete.
    print('--- Sorted ---')
    for size in SIZES:
        # TODO: Time insertion and deletion of a sorted list.
        # Use list(range(n)) to create a sorted list of length n.
        pass

    # Random insert and delete.
    print('\n--- Random ---')
    for size in SIZES:
        # TODO: Time insertion and deletion of a random list.
        # Use random.shuffle(lst) to get a random ordering of lst.
        pass
