"""CSC148 Exercise 5: Tree Practice

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 5.
It is divided into three parts:
- Task 1, which contains one Tree method to implement.
- Task 2, which asks you to implement two operations that allow you
  to convert between trees and nested lists.
- Task 3, which asks you to learn about and use a more restricted form of
  trees known as *binary trees*.
"""


class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and LinkedListRec
    from Lab 7; the only major difference is that _rest
    has been replaced by _subtrees to handle multiple
    recursive sub-parts.

    === Private Attributes ===
    @type _root: object | None
        The item stored at the tree's root, or None if the tree is empty.
    @type _subtrees: list[Tree]
        A list of all subtrees of the tree.

    === Representation Invariants ===
    - If self._root is None then self._subtrees is empty.
      This setting of attributes represents an empty Tree.
    - self._subtrees does not contain any empty Trees.
    """

    def __init__(self, root, subtrees):
        """Initialize a new Tree with the given root
        value and subtrees.

        If <root> is None, the tree is empty.

        @type self: Tree
        @type root: object
        @type subtrees: list[Tree]
        @rtype: None
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self):
        """Return True if this tree is empty.

        @type self: Tree
        @rtype: bool
        """
        return self._root is None

##############################################################################
    # Task 1: Another tree method
###############################################################################

    def __eq__(self, other):
        """Return whether <self> and <other> are equal.

        @type self: Tree
        @type other: Tree
        @rtype: bool
        >>> t1 = Tree(1, [Tree(2,[]), Tree(3,[])])
        >>> t2 = Tree(1, [Tree(2,[]), Tree(3,[])])
        >>> t1 == t2
        True
        >>> t3 = Tree(1, [])
        >>> t1 == t3
        False
        """
        if self.is_empty() and not other.is_empty():
            return False
        if not self.is_empty() and other.is_empty():
            return False
        if self.is_empty() and other.is_empty():
            return True
        if self._subtrees == [] and other._subtrees != []:
            return False
        if self._subtrees != [] and other._subtrees == []:
            return False
        if self._root == other._root:
            return True
##############################################################################
            # Task 2: Trees and nested lists
##############################################################################

    def to_nested_list(self):
        """Return the nested list representation of this tree.

        @type self: Tree
        @rtype: list
        """
        if self.is_empty():
            return []
        else:
            lst = [self._root]

            for tree in self._subtrees:
                lst.append(tree.to_nested_list())

            return lst


def to_tree(obj):
    """Return the Tree which <obj> represents.

    Precondition: <obj> is a valid nested list representation of a tree.
                  (In particular, <obj> is not an int.)

    You may not access Tree attributes directly. This function can be
    implemented only using the Tree constructor.

    @type obj: list
    @rtype: Tree
    """

    if len(obj) == 1:
        return Tree(obj[0], [])

    lst = []
    for index in range(1, len(obj)):
        lst.append(to_tree(obj[index]))

    return Tree(obj[0], lst)


##############################################################################
# Task 3: Binary trees
##############################################################################
class BinaryTree:
    """A class representing a binary tree.

    A binary tree is either empty, or a root connected to
    a *left* binary tree and a *right* binary tree (which could be empty).

    === Private Attributes ===
    @type _root: object | None
    @type _left: BinaryTree | None
    @type _right: BinaryTree | None

    === Representation Invariants ===
    _root, _left, _right are either ALL None, or none of them are None.
      If they are all None, this represents an empty BinaryTree.
    """

    def __init__(self, root, left, right):
        """Initialise a new binary tree with the given values.

        If <root> is None, this represents an empty BinaryTree
        (<left> and <right> are ignored in this case).

        Precondition: if <root> is not None, then neither <left> nor <right>
                      are None.

        @type self: BinaryTree
        @type root: object | None
        @type left: object | None
        @type right: object | None
        @rtype: None
        """
        if root is None:
            # store an empty BinaryTree
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = left
            self._right = right

    def is_empty(self):
        """Return True if this binary tree is empty.

        Note that only empty binary trees can have left and right
        attributes set to None.

        @type self: BinaryTree
        @rtype: bool
        """
        return self._root is None

    def preorder(self):
        """Return a list of this tree's items using a *preorder* traversal.

        @type self: BinaryTree
        @rtype: list
        """
        if self.is_empty():
            return []

        else:
            lst = [self._root]

            if self._left is not None:
                lst.extend(self._left.preorder())

            if self._right is not None:
                lst.extend(self._right.preorder())

        return lst

    def inorder(self):
        """Return a list of this tree's items using an *inorder* traversal.

        @type self: BinaryTree
        @rtype: list
        """
        if self.is_empty():
            return []

        lst = []
        if self._left is not None:
            lst.extend(self._left.inorder())
            lst.append(self._root)

        if self._right is not None:
            lst.extend(self._right.inorder())

        return lst

    def postorder(self):
        """Return a list of this tree's items using a *postorder* traversal.

        @type self: BinaryTree
        @rtype: list
        """
        if self.is_empty():
            return []

        lst = []
        if self._left is not None:
            lst.extend(self._left.postorder())

        if self._right is not None:
            lst.extend(self._right.postorder())

        lst.append(self._root)
        return lst


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='pylintrc.txt')
