"""Lab 7: Recursion, Task 2

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a few nested list functions for you to practice
implementing recursively.
"""


def nested_max(obj):
    """Return the maximum item stored in <obj>.

    You may assume all the items are positive, and calling
    nested_max on an empty list returns 0.

    @type obj: int | list
    @rtype: int

    >>> nested_max(17)
    17
    >>> nested_max([1, 2, [1, 2, [3], 4, 5], 4])
    5
    >>> nested_max([1, 2, 3, 4])
    4

    """
    max_ =0
    if isinstance(obj, int):
        return obj

    for item in obj:

        local_max = nested_max(item)
        max_ = max(local_max, max_)

    return max_





def length(obj):
    """Return the length of <obj>.

    The *length* of a nested list is defined as:
    1. 0, if <obj> is a number.
    2. The maximum of len(obj) and the lengths of the nested lists contained
       in <obj>, if <obj> is a list.

    @type obj: int | list
    @rtype: int

    >>> length(17)
    0
    >>> length([1, 2])
    2
    >>> length([1, 2, [1, 2], 4])
    4
    >>> length([1, 2, [3], 4, 5])
    5
    >>> length([1, 2, [1, 2, [3], 4, 5], 4])
    5
    """
    len_ = 0

    if isinstance(obj, int):
        return len_

    len_ = len(obj)
    for item in obj:

        len_ = max(length(item), len_)

    return len_



def equal(obj1, obj2):
    """Return whether two nested lists are equal, i.e., have the same value.

    Note: order matters.

    @type obj1: int | list
    @type obj2: int | list
    @rtype: bool

    >>> equal(17, [1, 2, 3])
    False
    >>> equal([1, 2, [1, 2], 4], [1, 2, [1, 2], 4])
    True
    >>> equal([1, 2, [1, 2], 4], [4, 2, [2, 1], 3])
    False
    """
    if isinstance(obj1, int) and isinstance(obj2, int):
        return obj1 == obj2

    elif  isinstance(obj1, int) and not isinstance(obj2, int):
        return False

    elif not isinstance(obj1, int) and isinstance(obj2, int):
        return False

    elif len(obj1) != len(obj2):
        return False

    else:
        for i in range(len(obj1)):

            if not equal(obj1[i], obj2[i]):
                return False

        return True





