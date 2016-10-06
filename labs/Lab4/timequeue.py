"""CSC148 Lab 4: Abstract Data Types

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===

This module runs timing experiments to determine how the time taken
to enqueue or dequeue grows as the queue size grows.

To complete this code, you will use the Timer class.  Here is a template
for how to use it.

    with Timer('message to print when the with-block is over') as tm:
        # A block of code to be timed goes here.
        # The timer is "on" the whole time.

    # After the block ends, the attribute tm.interval now stores the
    # total time taken to run the block of code.
"""
from myqueue import Queue
from timer import Timer


def profile_enqueue(queue_size, n):
    """Return the average time taken (averaging over <n> repetitions) to
    enqueue a single item into a Queue of size <queue_size>.

    @type queue_size: int
    @type n: int
    @rtype: float
    """
    # TODO: Make a list containing <n> queues of size <queue_size>.

    # TODO: For each of the <n> queues, enqueue a single item.
    # (Wrap the code in a Timer to measure the total time taken.)

    # TODO: Return the average time taken.


def profile_dequeue(queue_size, n):
    """Return the average time taken (averaging over <n> repetitions) to
    dequeue a single item from a Queue of size <queue_size>.

    @type queue_size: int
    @type n: int
    @rtype: float
    """
    # TODO: Complete this function in the same way as profile_enqueue.


if __name__ == '__main__':
    # TODO: Profile enqueue and dequeue on various queue sizes.
    # We recommend having queue sizes in the 10 000's to see some
    # noticeable growth in the time taken.
    pass
