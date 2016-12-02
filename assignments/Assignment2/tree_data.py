"""Assignment 2: Trees for Treemap

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the basic tree interface required by the treemap
visualiser. You will both add to the abstract class, and complete a
concrete implementation of a subclass to represent files and folders on your
computer's file system.
"""
import os
from random import randint


class AbstractTree:
    """A tree that is compatible with the treemap visualiser.

    This is an abstract class that should not be instantiated directly.

    You may NOT add any attributes, public or private, to this class.
    However, part of this assignment will involve you adding and implementing
    new public *methods* for this interface.

    === Public Attributes ===
    @type data_size: int
        The total size of all leaves of this tree.
    @type color: (int, int, int)
        The RGB colour value of the root of this tree.
        Note: only the colours of leaves will influence what the user sees.

    === Private Attributes ===
    @type _root: obj | None
        The root value of this tree, or None if this tree is empty.
    @type _subtrees: list[AbstractTree]
        The subtrees of this tree.
    @type _parent_tree: AbstractTree | None
        The parent tree of this tree; i.e., the tree that contains this tree
        as a subtree, or None if this tree is not part of a larger tree.

    === Representation Invariants ===
    - data_size >= 0
    - If _subtrees is not empty, then data_size is equal to the sum of the
      data_size of each subtree.
    - colour's elements are in the range 0-255.

    - If _root is None, then _subtrees is empty, _parent_tree is None, and
      data_size is 0.
      This setting of attributes represents an empty tree.
    - _subtrees IS allowed to contain empty subtrees (this makes deletion
      a bit easier).

    - if _parent_tree is not empty, then self is in _parent_tree._subtrees
    """

    def __init__(self, root, subtrees, data_size=0):
        """Initialize a new AbstractTree.

        If <subtrees> is empty, <data_size> is used to initialize this tree's
        data_size. Otherwise, the <data_size> parameter is ignored, and this tree's
        data_size is computed from the data_sizes of the subtrees.

        If <subtrees> is not empty, <data_size> should not be specified.

        This method sets the _parent_tree attribute for each subtree to self.

        A random colour is chosen for this tree.

        Precondition: if <root> is None, then <subtrees> is empty.

        @type self: AbstractTree
        @type root: object
        @type subtrees: list[AbstractTree]
        @type data_size: int
        @rtype: None
        """
        self._root = root
        self._subtrees = subtrees
        self._parent_tree = None

        # 1. Initialize self.colour and self.data_size, according to the docstring.
        self.color = (randint(30, 255), randint(30, 255), randint(30, 255))
        if self._subtrees == []:
            self.data_size = data_size
        else:
            # 2. Properly set all _parent_tree attributes in self._subtrees
            for tree in subtrees:
                self.data_size += tree.data_size
                tree._parent_tree = self

    def is_empty(self):
        """Return True if this tree is empty.

        @type self: AbstractTree
        @rtype: bool
        """
        return self._root is None

    def generate_treemap(self, rect):
        """Run the treemap algorithm on this tree and return the rectangles.

        Each returned tuple contains a pygame rectangle and a colour:
        ((x, y, width, height), (r, g, b)).

        One tuple should be returned per non-empty leaf in this tree.

        @type self: AbstractTree
        @type rect: (int, int, int, int)
            Input is in the pygame format: (x, y, width, height)
        @rtype: list[((int, int, int, int), (int, int, int))]
        """
        # Read the handout carefully to help get started identifying base cases,
        # and the outline of a recursive step.
        #
        # Programming tip: use "tuple unpacking assignment" to easily extract
        # coordinates of a rectangle, as follows.
        # x, y, width, height = rect

        # if the size is 0:
        if self.data_size == 0:
            return []
        # if self is a leaf
        elif self._subtrees == []:
            return [(rect, self.color)]
        else:
            x, y, width, height = rect
            rect_lst = []
            pos_x = x
            pos_y = y

            for i in range(len(self._subtrees)):
                sub_tree = self._subtrees[i]

                if i < len(self._subtrees) - 1:
                    percent_area = sub_tree.data_size / self.data_size
                    if width > height:
                        new_width = int(percent_area * width)
                        rect_lst.extend(sub_tree.generate_treemap((pos_x, pos_y, new_width, height)))
                        pos_x += new_width
                    else:
                        new_height = int(percent_area * height)
                        rect_lst.extend(sub_tree.generate_treemap((pos_x, pos_y, width, new_height)))
                        pos_y += new_height
                else:
                    # this is the last sub_tree
                    if width > height:
                        rect_lst.extend(sub_tree.generate_treemap((pos_x, pos_y, width - pos_x, height)))
                    else:
                        rect_lst.extend(sub_tree.generate_treemap((pos_x, pos_y, width, height - pos_y)))

            return rect_lst

    def get_separator(self):
        """Return the string used to separate nodes in the string
        representation of a path from the tree root to a leaf.

        Used by the treemap visualiser to generate a string displaying
        the items from the root of the tree to the currently selected leaf.

        This should be overridden by each AbstractTree subclass, to customize
        how these items are separated for different data domains.

        @type self: AbstractTree
        @rtype: str
        """
        raise NotImplementedError

    def get_leaves(self):
        """Return a list of leaves of this tree
        @type self: AbstractTree
        @rtype [AbstractTree]
        """

        if self._subtrees == []:
            return [self]
        else:
            lst = []
            for tree in self._subtrees:
                lst.extend(tree.get_leaves())

            return lst

    def delete_leaf(self, leaf):
        """delete <leaf> from this tree
        @type self: AbstractTree
        @type leaf: AbstractTree
        @rtype: None
        Precondtions:
            leaf._subtrees == []
        """
        if self._root == leaf._root:
            self._parent_tree.data_size = self._parent_tree.data_size - self.data_size

            subtrees = self._parent_tree.get_subtrees()
            for tree in subtrees:
                if tree == leaf:
                    subtrees.remove(leaf)

            leaf._parent_tree = None
        else:
            for tree in self._subtrees:
                tree.delete_leaf(leaf)

    def get_subtrees(self):
        """return the list of subtrees of this tree
        @type self: AbstractTree
        @rtype [AbstractTree]
        """
        return self._subtrees


class FileSystemTree(AbstractTree):
    """A tree representation of files and folders in a file system.

    The internal nodes represent folders, and the leaves represent regular
    files (e.g., PDF documents, movie files, Python source code files, etc.).

    The _root attribute stores the *name* of the folder or file, not its full
    path. E.g., store 'assignments', not '/Users/David/csc148/assignments'

    The data_size attribute for regular files as simply the size of the file,
    as reported by os.path.getsize.
    """

    def __init__(self, path):
        """Store the file tree structure contained in the given file or folder.

        Precondition: <path> is a valid path for this computer.

        @type self: FileSystemTree
        @type path: str
        @rtype: None
        >>> t1 = FileSystemTree('C:/Users/Sagnik/Documents/U of T/Courses/Csc165/e1.pdf')
        >>> t1.data_size
        55433
        >>> t2 = FileSystemTree('C:/Users/Sagnik/Documents/U of T/Courses/CSC148/csc148/assignments/Assignment1')
        >>> t2.data_size
        68867
        """
        # Remember that you should recursively go through the file system
        # and create new FileSystemTree objects for each file and folder
        # encountered.
        #
        # Also remember to make good use of the superclass constructor!

        # check if it is a file, it will contain a dot
        if os.path.isfile(path):
            AbstractTree.__init__(self, os.path.basename(path), [], os.path.getsize(path))
        else:
            dirs = os.listdir(path)
            sub_trees = []
            self.data_size = 0
            for sub_dir in dirs:
                tree = FileSystemTree(os.path.join(path, sub_dir))
                sub_trees.append(tree)

            AbstractTree.__init__(self, os.path.basename(path), sub_trees, 0)

    def get_separator(self):
        """
        Preconditions:
        <self> is an empty tree
        """

        if self._parent_tree is None:
            return self._root

        result = ''
        result += self._parent_tree.get_separator() + '/' + self._root

        return result


if __name__ == '__main__':
    import python_ta

    # Remember to change this to check_all when cleaning up your code.
    python_ta.check_errors(config='pylintrc.txt')
