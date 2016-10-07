"""CSC148 Lab 4: Abstract Data Types

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
In this module, you will develop an implementation of a new ADT, the Queue.
It will be helpful to review the stack implementation from lecture.

After you've implemented the Queue, you'll write two different functions that
operate on a Queue, paying attention to whether or not the queue should be
modified.
"""


class Queue:
    """Queue implementation.

    Stores data in a first-in, first-out order.
    When removing an item from the queue, the one which was added first
    is removed.

   ==== Private attributes ===
   @type _items: []
   stores the items of the qeue
    """

    def __init__(self):
        """Initialize a new empty queue.

        @type self: Queue
        @rtype: None
        """
        self._items = []

    def is_empty(self):
        """Return whether this queue is empty.

        @type self: Queue
        @rtype: bool
        """
        if len(self._items) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        """Add <item> to the back of this queue.

        @type self: Queue
        @type item: object
        @rtype: None
        """
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of this queue.

        TODO: make sure to specify what will happen when the queue is empty.

        @type self: Queue
        @rtype: Object
        """
        return self._items.pop(0)


def product(integer_queue):
    """Remove all items in <integer_queue> and return their result.

    Precondition: <integer_queue> contains only integers.

    @type integer_queue: Queue
    @rtype: int
    """
    result = 1

    while not integer_queue.is_empty():
        result *= integer_queue.dequeue()

    return result


def product_star(integer_queue):
    """Return the result of integers in <integer_queue>.

    Leave <integer_queue> unchanged when this function returns.

    Precondition: <integer_queue> contains only integers.

    @type integer_queue: Queue
    @rtype: int
    """
    q2 = Queue()
    result = 1
    while not integer_queue.is_empty():
        item = integer_queue.dequeue()
        result *= item
        q2.enqueue(item)

    while not q2.is_empty():
        integer_queue.enqueue(q2.dequeue())

    return result


if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    prime_line = Queue()
    for prime in primes:
        prime_line.enqueue(prime)

    assert 6469693230 == product_star(prime_line)
    assert not prime_line.is_empty()
    assert 6469693230 == product(prime_line)
    assert prime_line.is_empty()
