"""CSC148 Stack Implementation

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains an implementation of a Stack, together with a custom error
called EmptyStackError, used when pop is called on an empty stack.
"""


class EmptyStackError(Exception):
    pass


class Stack:
    """Stack implementation.

    Stores data in a first-in, last-out order.
    When removing an item from the stack, the most recently-added
    item is the one that is removed.

    === Private Attributes ===
    @type _items: list
        The items stored in the stack. The end of the list represents
        the front of the stack.
    """

    def __init__(self):
        """Initialize a new empty stack.

        @type self: Stack
        @rtype: None
        """
        self._items = []

    def is_empty(self):
        """Return whether this stack contains no items.

        @type self: Stack
        @rtype: bool
        """
        return len(self._items) == 0

    def push(self, item):
        """Add a new element to the top of this stack.

        @type self: Stack
        @type item: object
        @rtype: None
        """
        self._items.append(item)

    def pop(self):
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if the stack is empty.

        @type self: Stack
        @rtype: object
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop()
