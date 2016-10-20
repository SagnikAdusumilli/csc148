"""Lab 6: Linked List Exercises, Part 2

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.

All of the code from lecture is here, as well as some exercises to work on.
"""


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one
    which is only meant to be used in this module by the
    LinkedList class, but not by client code.

    === Attributes ===
    @type item: object
        The data stored in this node.
    @type next: _Node | None
        The next node in the list, or None if there are
        no more nodes in the list.
    """
    def __init__(self, item):
        """Initialize a new node storing <item>, with no next node.

        @type self: _Node
        @type item: object
        @rtype: None
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.

    === Private Attributes ===
    @type _first: _Node | None
        The first node in the list, or None if the list is empty.
    @type _iter_node: _Node | None
        The node used to keep track of iteration in __iter__ and __next__.
    """
    def __init__(self, items):
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.

        @type self: LinkedList
        @type items: list
        @rtype: None
        """
        if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            current_node = self._first
            for item in items[1:]:
                current_node.next = _Node(item)
                current_node = current_node.next

        # Initialize a node for the iterator
        self._iter_node = None

    # ------------------------------------------------------------------------
    # Non-mutating methods: these methods do not change the list
    # ------------------------------------------------------------------------

    def is_empty(self):
        """Return whether this linked list is empty.

        @type self: LinkedList
        @rtype: bool
        """
        return self._first is None

    def __str__(self):
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        @type self: LinkedList
        @rtype: str

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '[1 -> 2 -> 3]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __getitem__(self, index):
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.

        @type self: LinkedList
        @type index: int
        @rtype: object
        """
        curr = self._first
        curr_index = 0

        # Iterate to (index)-th node
        # Note: the two STOPPING conditions are
        # (1) curr is None (gone past the end of the list)
        # (2) curr_index == index (reached the correct node)
        # The loops stops when (1) or (2) is true,
        # so it *continues* when both are false.
        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1

        if curr is None:
            raise IndexError
        else:
            return curr.item

    # ------------------------------------------------------------------------
    # Mutating methods: these methods modify the list
    # ------------------------------------------------------------------------

    # --- Lab Exercises ---

    def clear(self):
        """Remove all items from this list.

        @type self: LinkedList
        @rtype: None

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '[1 -> 2 -> 3]'
        >>> lst.clear()
        >>> str(lst)
        '[]'
        """
        self._first = None

    def append(self, item):
        """Append <item> to the end of this list.

        @type self: LinkedList
        @type item: object
        @rtype: None

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '[1 -> 2 -> 3]'
        >>> lst.append(4)
        >>> str(lst)
        '[1 -> 2 -> 3 -> 4]'
        """
        if self._first is None:
            self._first = _Node(item)

        else:
            curr = self._first

            while curr.next is not None:
                curr = curr.next

            curr.next = _Node(item)

    def __setitem__(self, index, item):
        """Store item at position <index> in this list.

        Raise IndexError if index is >= the length of self.

        @type self: LinkedList
        @type index: int
        @type item: object
        @rtype: None

        >>> lst = LinkedList([1, 2, 3])
        >>> lst[0] = 100  # Equivalent to lst.__setitem__(0, 100)
        >>> lst[1] = 200
        >>> lst[2] = 300
        >>> str(lst)
        '[100 -> 200 -> 300]'
        """
        if index == 0:
            if self._first is None:
                self._first = _Node(item)
            else:
                self._first.item = item

        else:
            curr = self._first

            for i in range(index-1):
                curr = curr.next

            if curr.next is None:
                curr.next = _Node(item)
            else:
                curr.next.item = item

    def extend(self, items):
        """Extend this list by appending elements from <items>.

        @type self: LinkedList
        @type items: list
        @rtype: None

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '[1 -> 2 -> 3]'
        >>> lst.extend([4, 5, 6, 7])
        >>> str(lst)
        '[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7]'
        """
        if self._first is None:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next

        else:
            curr = self._first

            while curr.next is not None:
                curr = curr.next

            curr.next = _Node(items[0])

            for item in items[1:]:
                curr = curr.next
                curr.next = _Node(item)


    # --- Additional Exercises ---

    def map(self, f):
        """Return a new LinkedList whose nodes store items that are
        obtained by applying f to each item in this linked list.

        Does not change this linked list.

        @type self: LinkedList
        @type f: Function
        @rtype: None

        >>> func = str.upper
        >>> func('hi')
        'HI'
        >>> lst = LinkedList(['Hello', 'Goodbye'])
        >>> str(lst.map(func))
        '[HELLO -> GOODBYE]'
        >>> str(lst.map(len))
        '[5 -> 7]'
        """
        items = []
        if self._first is not None:
            curr = self._first

            while curr is not None:
                items.append(f(curr.item))
                curr = curr.next

            return LinkedList(items)

    def __iter__(self):
        """Return a linked list iterator.

        Hint: the easiest way to implement __iter__ and __next__ is to
        make the linked list object responsible for its own iteration.

        In other words, __iter__(self) should simply return <self>.
        However, in order to make sure the loop always starts at the beginning
        of the list, you'll need a new private attribute for this class which
        keeps track of where in the list the iterator is currently at.

        @type self: LinkedList
        @rtype: LinkedList
        """
        self._iter_node = self._first

        return self

    def __next__(self):
        """Return the next item in the iteration.

        Raise StopIteration if there are no more items to return.

        Hint: If you have an attribute keeping track of the where the iteration
        is currently at in the list, it should be straight-forward to return
        the current item, and update the attribute to be the next node in
        the list.

        @type self: LinkedList
        @rtype: object

        >>> lst = LinkedList([1, 2, 3])
        >>> iter = lst.__iter__()
        >>> lst.__next__()
        1
        >>> lst.__next__()
        2
        >>> lst.__next__()
        3
        """
        if self._iter_node is None:
            raise StopIteration

        item = self._iter_node.item
        self._iter_node = self._iter_node.next
        return item
if __name__ == '__main__':

    linky = LinkedList([1, 2, 3, 4])

    print(linky)

    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all()
