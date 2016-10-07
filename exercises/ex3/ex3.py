"""CSC148 Exercise 3: Stacks and a Chain of People

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 3.
It is divided into two parts:
- Task 1, which contains two functions you should implement using only
  the public interface of Stacks (constructor, is_empty, push, pop)
- Task 2, which contains the definition of two new classes, Person and
  PeopleChain. You'll have to read their documentation carefully to understand
  how to use them.
"""
from stack import Stack


##############################################################################
# Task 1: More Stack Exercises
##############################################################################
def reverse(stack):
    """Reverse all the elements of <stack>.

    Do nothing if the stack is empty.

    @type stack: Stack
    @rtype: None

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """

    if stack.is_empty():
        return None
    else:
        list = []
        while not stack.is_empty():
            list.append(stack.pop())

        for item in list:
            stack.push(item)




def merge_alternating(stack1, stack2):
    """Return a stack by merging two stacks in alternating order.

    Precondition: <stack1> and <stack2> have the same size.

    The new stack's top element should be the top element of <stack1>,
    followed by the top element of <stack2>, followed by the next element
    of <stack1>, then <stack2>, etc.

    If <stack1> and <stack2> are both empty, the new stack should also be empty.

    <stack1> and <stack2> should be unchanged when the function ends.
    In other words, this function should not mutate either input stack.

    @type stack1: Stack
    @type stack2: Stack
    @rtype: Stack

    >>> s1 = Stack()
    >>> s2 = Stack()
    >>> s1.push('a')
    >>> s1.push('b')
    >>> s1.push('c')
    >>> s2.push(1)
    >>> s2.push(2)
    >>> s2.push(3)
    >>> merged = merge_alternating(s1, s2)
    >>> merged.pop()
    'c'
    >>> merged.pop()
    3
    >>> merged.pop()
    'b'
    >>> merged.pop()
    2
    >>> merged.pop()
    'a'
    >>> merged.pop()
    1
    >>> merged.is_empty()
    True
    >>> s1.is_empty()
    True
    >>> s2.is_empty()
    True
    """
    merged_stack = Stack()

    reverse(stack1)
    reverse(stack2)

    while not stack1.is_empty() and not stack2.is_empty():

        merged_stack.push(stack2.pop())
        merged_stack.push(stack1.pop())


    return merged_stack


##############################################################################
# Task 2: A Chain of People
##############################################################################
class ShortChainError(Exception):
    """Exception that is raised when PeopleChain is too short."""
    pass


class Person:
    """A person in a chain of people.

    === Attributes ===
    @type name: str
        The name of the person.
    @type next: Person | None
        The next person in the chain, or None if this person is not holding
        onto anyone.
    """
    def __init__(self, name):
        """Create a person who is initially not holding onto anyone.

        @type self: Person
        @type name: str
        @rtype: None
        """
        self.name = name
        self.next = None  # Initially holding onto no one


class PeopleChain:
    """A chain of people.

    === Attributes ===
    @type leader: Person | None
        The first person in the chain, or None if the chain is empty.
    """
    def __init__(self, names):
        """Create people linked together in the order provided in <names>.

        The leader of the chain is the first person in <names>.

        @type self: PeopleChain
        @type names: list[str]
        @rtype: None
        """
        if len(names) == 0:
            # No leader, representing an empty chain!
            self.leader = None
        else:
            # Set leader
            self.leader = Person(names[0])
            current_person = self.leader
            for name in names[1:]:
                # Set the link for the current person
                current_person.next = Person(name)
                # Update the current person
                # Note that current_person always refers to
                # the LAST person in the chain
                current_person = current_person.next

    # TODO: Implement the following four methods!
    def get_leader(self):
        """Return the name of the leader of the chain.

        Raise ShortChainError if chain has no leader.

        @type self: PeopleChain
        @rtype: str

        >>> chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        >>> chain.get_leader()
        'Iron Man'
        """
        return self.leader.name

    def get_second(self):
        """Return the name of the second person in the chain.

        That is, return the name of the person the leader is holding onto.
        Raise ShortChainError if chain has no second person.

        @type self: PeopleChain
        @rtype: str

        >>> chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        >>> chain.get_second()
        'Janna'
        """
        return self.leader.next.name

    def get_third(self):
        """Return the name of the third person in the chain.

        Raise ShortChainError if chain has no third person.

        @type self: PeopleChain
        @rtype: str

        >>> chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        >>> chain.get_third()
        'Kevan'
        """
        return self.leader.next.next.name

    def get_nth(self, n):
        """Return the name of the n-th person in the chain.

        Precondition: n >= 1 (indexing starts at 1, not 0)

        Raise ShortChainError if chain doesn't have n people.

        @type self: PeopleChain
        @type n: int
        @rtype: str

        >>> chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        >>> chain.get_nth(3)
        'Kevan'
        """
        # Remember: you must use a for or while loop in this function body!
        # If you use a for loop but don't need to use the index, use an
        # underscore for the variable name:
        #
        # for _ in range(10):
        #     <code that doesn't use the index>
        current_person = self.leader
        for _ in range(n-1):
            if current_person is None:
                raise ShortChainError
            current_person = current_person.next


        if current_person is None:
            raise ShortChainError
        else:
            return current_person.name



if __name__ == '__main__':
    import python_ta
    python_ta.check_errors(config='.pylintrc')
    # python_ta.check_all(config='.pylintrc')

    # import doctest
    # doctest.testmod()
