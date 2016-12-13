"""CSC148 Exercise 4: Recursion Practice

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 4.
It is divided into two parts:
- Task 1, which contains two functions on nested lists that you should implement
  recursively, using what you've learned this week in lecture and lab.
- Task 2, which asks you to learn about a new recursive structure, a family
  tree, and write a method that operates on this structure.
"""


##############################################################################
# Task 1: More practice with nested lists
##############################################################################


def duplicate(nested_list):
    """Return a new nested list with all numbers in <nested_list> duplicated.

    Each integer in <nested_list> should appear twice *consecutively* in the
    output nested list. The nesting structure is the same as the input,
    only with some new numbers added. See doctest examples for details.

    If <nested_list> is an int, return a list containing two copies of it.

    @type nested_list: list | int
    @rtype: list


    >>> duplicate([1, 2])
    [1, 1, 2, 2]
    >>> duplicate([1, [2, 3]])  # NOT [1, 1, [2, 2, 3, 3], [2, 2, 3, 3]]
    [1, 1, [2, 2, 3, 3]]
    """
    lst = []

    if isinstance(nested_list, int):
        lst.extend([nested_list, nested_list])
        return lst
    else:
        for item in nested_list:
            if isinstance(item, int):
                lst.extend(duplicate(item))
            else:
                lst.append(duplicate(item))

        return lst


def add_one(nested_list):
    """Add one to every number stored in <nested_list>.

    Do nothing if <nested_list> is an int.
    If <nested_list> is a list, *mutate* it to change the numbers stored.
    (Don't return anything in either case.)

    @type nested_list: list | int
    @rtype: None

    >>> lst0 = 1
    >>> add_one(lst0)
    >>> lst0
    1
    >>> lst1 = []
    >>> add_one(lst1)
    >>> lst1
    []
    >>> lst2 = [1, [2, 3], [[[5]]]]
    >>> add_one(lst2)
    >>> lst2
    [2, [3, 4], [[[6]]]]
    """
    if isinstance(nested_list, int):
        return None

    else:
        for i in range(len(nested_list)):
            if isinstance(nested_list[i], int):
                nested_list[i] += 1
            else:
                add_one(nested_list[i])


##############################################################################
# Task 2: Family trees
##############################################################################
class Person:
    """A person in a family tree.

    === Attributes ===
    @type name: str
        The name of this person.
    @type children: list[Person]
        The children of this person.
    """

    def __init__(self, new_name, new_children):
        """Create a new person with the given name and children.

        @type self: Person
        @type new_name: str
        @type new_children: list[Person]
        @rtype: None
        """
        self.name = new_name
        self.children = new_children

    def count_descendants(self):
        """Return the number of descendants of this person.

        @type self: Person
        @rtype: int
        """
        if self.children == []:
            return 0
        else:
            count = len(self.children)

            for child in self.children:
                count += child.count_descendants()

            return count


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import python_ta

    python_ta.check_all()
