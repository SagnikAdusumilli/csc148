"""CSC148 Exercise 6: Binary Search Trees Practice

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 6.

You are responsible for completing three BinarySearchTree methods in this file.
"""


class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every node, its value is >= all items stored in its left
    subtree, and < all items stored in its right subtree.

    === Private Attributes ===
    @type _root: object
        The item stored at the root of the tree, or None if the tree is empty.
    @type _left: BinarySearchTree | None
        The left subtree, or None if the tree is empty
    @type _right: BinarySearchTree | None
        The right subtree, or None if the tree is empty

    === Representation Invariants ===
     - If _root is None, then so are _left and _right.
       This represents an empty BST.
     - If _root is not None, then _left and _right are BinarySearchTrees.
     - (BST Property) All items in _left are <= _root,
       and all items in _right are >= _root.
    """
    def __init__(self, root):
        """Initialize a new BST with a given root value.

        If <root> is None, the BST is empty.

        @type self: BinarySearchTree
        @type root: object | None
        @rtype: None
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def is_empty(self):
        """Return whether this tree is empty.

        @type self: BinarySearchTree
        @rtype: bool
        """
        return self._root is None

    def __contains__(self, item):
        """Return whether <item> is in this BST.

        @type self: BinarySearchTree
        @type item: object
        @rtype: bool
        """
        if self.is_empty():
            return False
        elif self._root == item:
            return True
        elif self._root > item:
            return self._left.__contains__(item)
        else:  # self._root < item
            return self._right.__contains__(item)

    def height(self):
        """Return the height of this BST.

        @type self: BinarySearchTree
        @rtype: int

        >>> BinarySearchTree(None).height()
        0
        >>> bst = BinarySearchTree(7)
        >>> bst.height()
        1
        >>> bst._left = BinarySearchTree(5)
        >>> bst.height()
        2
        >>> bst._right = BinarySearchTree(9)
        >>> bst.height()
        2
        """
        if self.is_empty():
            return 0
        else:
            return max(self._left.height(), self._right.height()) + 1

##############################################################################
# Task 1: More BST practice
##############################################################################
    # TODO: Implement this method!
    def num_less_than(self, item):
        """Return the number of items in this BST that are less than <item>.

        @type self: BinarySearchTree
        @type item: object
        @rtype: int
        """

        if self.is_empty() or self._root > item:
            return 0
        else:
            count = 1

            count += self._left.num_less_than(item)

            if not self._right.is_empty() and self._right._root < item:
                count += self._right.num_less_than(item)

            return count



    # TODO: Implement this method!
    def items_at_depth(self, d):
        """Return a sorted list of all items in this BST at depth <d>.

        Precondition: d >= 1.

        Reminder: you should not have to use the built-in 'sort' method
        or do any sorting yourself.

        @type self: BinarySearchTree
        @type d: int
        @rtype: list
        """
        if self.is_empty():
            return []
        elif d == 1:
            return [self._root]
        else:
            lst = []

            lst.extend(self._left.items_at_depth(d-1))
            lst.extend(self._right.items_at_depth(d-1))

            return lst

    # TODO: Implement this method!
    def levels(self):
        """Return a list of items in the tree, separated by level.

        You may wish to use 'items_at_depth' as a helper method,
        but this also makes your code less efficient. Try doing
        this method twice, once with 'items_at_depth', and once
        without it!

        @type self: BinarySearchTree
        @rtype: list[(int, list)]
        """
        lst = []
        for i in range(1, self.height()+1):
            lst.append((i, self.items_at_depth(i)))

        return lst

    def get_level(self, lvl):
        """ return a list containging list of items in that level

        @type self: BinarySearchTree
        @rtype: list[int]
        """

        if self.is_empty():
            return []
        else:
          lst = [self._root]


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
